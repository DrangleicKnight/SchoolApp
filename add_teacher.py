import mimetypes
import os
import shutil
import smtplib
from email.message import EmailMessage

import img2pdf
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivymd.toast import toast
from kivymd.uix.button import MDRaisedButton, MDRoundFlatButton
from kivymd.uix.dialog import MDDialog
from pymongo import MongoClient

client = MongoClient("localhost", 27017)
myDatabase = client.get_database("MCA")
studentsCollection = myDatabase.get_collection("Teachers")

teacher_image = []
teacher_details = []

location = []

def image_select(self):
    popup = Popup(size_hint = (.8, .6), title = "Choose Image")
    fileChooser = FileChooserListView()
    fileChooser.add_widget(MDRaisedButton(text = "Select",
                                        pos_hint = {"center_x" : .5, "center_y" : .2},
                                        size_hint = (.4, .2),
                                        md_bg_color = (176/255, 71/255, 89/255, .7),
                                        on_press = lambda a : file_chooser(self, fileChooser.selection)))
    popup.add_widget(fileChooser)
    popup.open()

def file_chooser(self, selection):
    location.clear()
    selected = "".join(selection)

    invalid_type = MDDialog(size_hint=(.5, .1), pos_hint={"center_x": .5, "center_y": .5},
                            title="Invalid File type", text="File should be png, jpg or gif",
                            buttons=[MDRoundFlatButton(text="Dismiss", md_bg_color=(133 / 255, 0, 0, 1),
                                                       on_press=lambda a: invalid_type.dismiss())])

    if selected.endswith(".png") or selected.endswith(".jpeg") or selected.endswith(".jpg") or selected.endswith(".gif"):
        if selected not in os.listdir("images/students/teachers"):
            shutil.copy(selected, "images/students/teachers")
        else:
            dialog = MDDialog(title = "Already Exists", size_hint = (.5, .3))
            dialog.add_widget(MDRaisedButton(text = "Dismiss",
                                             size_hint = (.4, .2),
                                             pos_hint = {"center_x" : .5, "center_y" : .2},
                                             on_press = dialog.dismiss()))
            dialog.open()
    else:
        invalid_type.open()

    image_name = selected.split("\\")[-1]
    location.append(f"images/students/teachers/{image_name}")
    teacher_image.append(f"images/students/teachers/{image_name}")

    screen = self.root.get_screen("add_teacher").ids.img
    screen.source = "".join(location)

def validate(self, email, name, dob, age, gender, contact, address, qualifications, subject, password):
    invalidCreds = MDDialog(size_hint=(.5, .15), pos_hint={"center_x": .5, "center_y": .5},
                            title = "Fill all details",
                            buttons=[MDRoundFlatButton(text="Dismiss", md_bg_color = (133/255, 0, 0, 1),
                            on_press=lambda a: invalidCreds.dismiss())])

    if len(email.text) and len(name.text) and len(dob.text) and len(age.text) and len(gender.text) and len(contact.text) and  len(address.text)\
            and len(qualifications.text) and len(subject.text) and len(password.text) and len(location) >= 1 :
        # this block of code will be executed
        add_teachers(email, name, dob, age, gender, contact, address, qualifications, subject, password)
        make_id(self, name, email, contact, address, gender, dob)
    else:
        invalidCreds.open()

def add_teachers(email, name, dob, age, gender, contact, address, qualifications, subject, password):
    teacher_details.append(name.text)
    teacher_details.append(email.text)
    teacher_details.append(password.text)

    studentsCollection.insert_one({"Name" : name.text,
                                  "Age" : age.text,
                                  "Password" : password.text,
                                  "E-mail" : email.text,
                                  "Contact" : contact.text,
                                  "Address" : address.text,
                                  "Gender" : gender.text,
                                  "Date of Birth" : dob.text,
                                  "Qualification" : qualifications.text,
                                  "Subject" : subject.text,
                                  "Image" : "".join(location)})

    os.rename(location[0], f"images/students/teachers/{name.text}.png")
    location.clear()

def make_id(self, name, email, contact, address, gender, date_of_birth):
    card = self.root.get_screen("teacher_icard").ids

    card.img.source = teacher_image[0]
    card.name.text = name.text
    card.address.text = address.text
    card.perm_address.text = address.text
    card.contact.text = contact.text
    card.gender.text = gender.text
    card.date_of_birth.text = date_of_birth.text
    card.email.text = email.text

    self.root.current = "teacher_icard"

def generate_id(card_front, card_back):
    card_front.export_to_png(f"images/students//{teacher_details[0]}_{teacher_details[2]}1.png")
    card_back.export_to_png(f"images/students/{teacher_details[0]}_{teacher_details[2]}2.png")

    with open(f"images/students/teacher_icard/{teacher_details[0]}_{teacher_details[2]}.pdf", "ab") as file:
        file.write(img2pdf.convert([f"images/students/{teacher_details[0]}_{teacher_details[2]}1.png",
                                   f"images/students/{teacher_details[0]}_{teacher_details[2]}2.png"]))

    for files in os.listdir("images/students/"):
        if files.endswith(".png"):
            os.remove(f"images/students/{files}")


def send_mail(self):
    message = EmailMessage()
    sender = "adnanschoolofwitchcraft@gmail.com"
    recipient = teacher_details[1]

    message['From'] = sender
    message['To'] = recipient

    message['Subject'] = "Welcome to Adnan's School of Wizardry!"

    message.set_content(f"You have been appointed as a teacher in Adnan's School of WitchCraft and Wizardry, {teacher_details[0]}!"
                        f"\n\nThe course you'll be teaching in is SYMCA\n\nWe hope you prove to be a valuable asset to this institute, great things await!"
                        f"\n\nYour username is : {teacher_details[1]}\n"
                        f"Your password is : {teacher_details[2]}")
    mime_type, _ = mimetypes.guess_type(f"images/students/teacher_icard/{teacher_details[0]}_{teacher_details[2]}.pdf")
    mime_type, mime_subtype = mime_type.split('/')
    with open(f"images/students/teacher_icard/{teacher_details[0]}_{teacher_details[2]}.pdf", "rb") as file:
        message.add_attachment(file.read(),
                               maintype=mime_type,
                               subtype=mime_subtype,
                               filename=f'{teacher_details[0]}_{teacher_details[2]}.pdf"')
    print(message)
    mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
    mail_server.set_debuglevel(1)
    mail_server.login(sender, "lfpxxodpgugulbha")
    mail_server.send_message(message)
    mail_server.quit()

    teacher_details.clear()
    teacher_details.clear()
    self.root.current = "teachers_dashboard"
    toast("Teacher Added")