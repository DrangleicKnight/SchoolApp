import os
import shutil
import img2pdf
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivymd.toast import toast
from kivymd.uix.button import MDRaisedButton, MDFlatButton, MDRoundFlatButton
from kivymd.uix.dialog import MDDialog
from pymongo import MongoClient

import mimetypes
import smtplib
from email.message import EmailMessage

client = MongoClient("localhost", 27017)
myDatabase = client.get_database("MCA")
studentsCollection = myDatabase.get_collection("Students")

check = ["unflag"]
student_detail = []
student_image = []

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
                          title="Invalid File type", text = "File should be png, jpg or gif",
                          buttons=[MDRoundFlatButton(text="Dismiss", md_bg_color=(133 / 255, 0, 0, 1),
                                                     on_press=lambda a: invalid_type.dismiss())])

    if selected.endswith(".png") or selected.endswith(".jpeg") or selected.endswith(".jpg") or selected.endswith(".gif"):
        if selected not in os.listdir("images/students/users"):
            shutil.copy(selected, "images/students/users")

            image_name = selected.split("\\")[-1]
            location.append(f"images/students/users/{image_name}")
            student_image.append(f"images/students/users/{image_name}")

            screen = self.root.get_screen("add_student").ids.img
            screen.source = "".join(location)
        else:
            dialog = MDDialog(text = "Already Exists", size_hint = (.5, .3))
            dialog.add_widget(MDRaisedButton(text = "Dismiss",
                                             size_hint = (.4, .2),
                                             pos_hint = {"center_x" : .5, "center_y" : .2},
                                             on_press = dialog.dismiss()))
            dialog.open()
    else:
        invalid_type.open()

def validate(self, roll, name, age, password, email, contact, address, classed, parent_contact, gender, date_of_birth, img):
    invalidCreds = MDDialog(size_hint=(.5, .15), pos_hint={"center_x": .5, "center_y": .5},
                            text="Fill all details",
                            buttons=[MDFlatButton(text="Dismiss", theme_text_color  = "Custom", text_color = "black",
                            on_press=lambda a: invalidCreds.dismiss())])

    already_exists = MDDialog(size_hint=(.5, .15), pos_hint={"center_x": .5, "center_y": .5},
                              title="Already Exists", text="Student with the same roll number already exists",
                              buttons=[MDFlatButton(text="Dismiss", theme_text_color="Custom", text_color="black",
                                                    on_press=lambda a: already_exists.dismiss())])

    if len(roll.text) and len(name.text) and len(age.text) and len(password.text) and len(email.text) and len(contact.text) \
            and len(address.text) and len(classed.text) and len(parent_contact.text) and len(gender.text) and \
            len(date_of_birth.text) and len(location) >= 1:

        #this block of code will be executed
        if studentsCollection.find_one({"Roll Number": roll.text}):
            already_exists.open()
        else:
            add_student(roll, name, age, password, email, contact, address, classed, parent_contact, gender, date_of_birth)
            make_id(self, roll, name, email, contact, parent_contact, classed, address, gender, date_of_birth)
            img.source = "images/icon.png"
            roll.text = ""
            name.text = ""
            age.text = ""
            password.text = ""
            email.text = ""
            contact.text = ""
            address.text = ""
            classed.text = ""
            parent_contact.text = ""
            gender.text = ""
            date_of_birth.text = ""
    else:
        invalidCreds.open()

def add_student(roll, name, age, password, email, contact, address, classed, parent_contact, gender, date_of_birth):
    student_detail.append(roll.text)
    student_detail.append(name.text)
    student_detail.append(email.text)
    student_detail.append(password.text)

    studentsCollection.insert_one({"Roll Number" : roll.text,
                                  "Name" : name.text,
                                  "Age" : age.text,
                                  "Password" : password.text,
                                  "E-mail" : email.text,
                                  "Contact" : contact.text,
                                  "Address" : address.text,
                                  "Class" : classed.text,
                                  "Parent's Contact" : parent_contact.text,
                                  "Gender" : gender.text,
                                  "Date of Birth" : date_of_birth.text,
                                  "Image" : f"images/students/users/{name.text}.png"})

    os.rename(location[0], f"images/students/users/{name.text}.png")
    location.clear()

def make_id(self, roll, name, email, contact, parent_contact, classed, address, gender, date_of_birth):
    card = self.root.get_screen("icard").ids

    card.img.source = student_image[0]
    card.name.text = name.text
    card.classed.text = classed.text
    card.roll.text = roll.text
    card.address.text = address.text
    card.perm_address.text = address.text
    card.contact.text = contact.text
    card.par_contact.text = parent_contact.text
    card.gender.text = gender.text
    card.date_of_birth.text = date_of_birth.text
    card.email.text = email.text

    self.root.current = "icard"

def generate_id(card_front, card_back):
    card_front.export_to_png(f"images/students/{student_detail[0]}_{student_detail[1]}1.png")
    card_back.export_to_png(f"images/students/{student_detail[0]}_{student_detail[1]}2.png")

    with open(f"images/students/icard/{student_detail[0]}_{student_detail[1]}.pdf", "ab") as file:
        file.write(img2pdf.convert([f"images/students/{student_detail[0]}_{student_detail[1]}1.png",
                                   f"images/students/{student_detail[0]}_{student_detail[1]}2.png"]))

    for files in os.listdir("images/students/"):
        if files.endswith(".png"):
            os.remove(f"images/students/{files}")


def send_mail(self):
    message = EmailMessage()
    sender = "adnanschoolofwitchcraft@gmail.com"
    recipient = student_detail[2]

    message['From'] = sender
    message['To'] = recipient

    message['Subject'] = "Welcome to Adnan's School of Wizardry!"

    message.set_content(f"You have been admitted to Adnan's School of WitchCraft and Wizardry, {student_detail[1]}!"
                        f"\n\nThe course you'll be pursuing is SYMCA\n\nWe hope you learn alot through your years in this institute, great things await!"
                        f"\n\nYour username is : {student_detail[2]}\n"
                        f"Your password is : {student_detail[3]}")
    mime_type, _ = mimetypes.guess_type(f"images/students/icard/{student_detail[0]}_{student_detail[1]}.pdf")
    mime_type, mime_subtype = mime_type.split('/')
    with open(f"images/students/icard/{student_detail[0]}_{student_detail[1]}.pdf", "rb") as file:
        message.add_attachment(file.read(),
                               maintype=mime_type,
                               subtype=mime_subtype,
                               filename=f'{student_detail[0]}_{student_detail[1]}.pdf"')
    print(message)
    mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
    mail_server.set_debuglevel(1)
    mail_server.login(sender, "lfpxxodpgugulbha")
    mail_server.send_message(message)
    mail_server.quit()

    student_detail.clear()
    student_image.clear()

    self.root.current = "add_student"

def admissions_form(self, email):
    screen = self.root.get_screen("admission_form").ids.layout

    empty_mail = MDDialog(size_hint=(.5, .15), pos_hint={"center_x": .5, "center_y": .5},
                        title="Enter your E-mail",
                        buttons=[MDRoundFlatButton(text="Dismiss", md_bg_color = (133/255, 0, 0, 1),
                                                   on_press=lambda a: empty_mail.dismiss())])

    if len(email.text) > 0:
        screen.export_to_png(f"images/students/forms/{email.text}.png")

        message = EmailMessage()
        sender = "adnanschoolofwitchcraft@gmail.com"
        recipient = email.text

        message['From'] = sender
        message['To'] = recipient

        message['Subject'] = "Welcome to Adnan's School of Wizardry!"

        message.set_content(f"Here is your Admission Form!")
        mime_type, _ = mimetypes.guess_type(f"images/students/forms/{email.text}.png")
        mime_type, mime_subtype = mime_type.split('/')
        with open(f"images/students/forms/{email.text}.png", "rb") as file:
            message.add_attachment(file.read(),
                                   maintype=mime_type,
                                   subtype=mime_subtype,
                                   filename=f'{email.text}.png"')
        mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
        mail_server.set_debuglevel(1)
        mail_server.login(sender, "lfpxxodpgugulbha")
        mail_server.send_message(message)
        mail_server.quit()

        student_detail.clear()
        student_image.clear()
        toast("Admission form has been sent. Check your E-mail")
    else:
        print("Invalid")
        # empty_mail.open()


