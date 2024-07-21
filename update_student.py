from kivymd.toast import toast
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from pymongo import MongoClient

client = MongoClient("localhost", 27017)
myDatabase = client.get_database("MCA")
myCollection = myDatabase.get_collection("Students")

selected_roll = []

invalid_roll = MDDialog(size_hint=(.5, .15), pos_hint={"center_x": .5, "center_y": .5}, title="Student doesn't exist",
                        buttons=[MDFlatButton(text="Dismiss", theme_text_color  = "Custom", text_color = "black",
                        on_press=lambda a: invalid_roll.dismiss())])

def fetch_student(roll, img, name, age, email, contact, address, password, classed, parent_contact, gender, date_of_birth):
    selected_roll.clear()
    if myCollection.find_one({"Roll Number" : roll.text}):
        selected_roll.append(roll.text)

        for student in myCollection.find({"Roll Number" : roll.text}):
            img.source = student.get("Image")
            name.text = student.get("Name")
            age.text = student.get("Age")
            email.text = student.get("E-mail")
            contact.text = student.get("Contact")
            address.text = student.get("Address")
            password.text = student.get("Password")
            classed.text = student.get("Class")
            parent_contact.text = student.get("Parent's Contact")
            gender.text = student.get("Gender")
            date_of_birth.text = student.get("Date of Birth")
    else:
        invalid_roll.open()
        img.source = "images/icon.png"
        roll.text = ""
        name.text = ""
        age.text = ""
        email.text = ""
        contact.text = ""
        address.text = ""
        password.text = ""
        classed.text = ""
        parent_contact.text = ""
        gender.text = ""
        date_of_birth.text = ""

def update_student(roll, name, age, email, contact, address, password, classed, parent_contact, gender, date_of_birth):
    if len(selected_roll) > 0:
        myCollection.update_one({"Roll Number" : selected_roll[0]}, {"$set" : {"Roll Number": roll.text,
                                                                               "Name" : name.text,
                                                                               "Age" : age.text,
                                                                               "E-mail" : email.text,
                                                                               "Contact" : contact.text,
                                                                               "Address" : address.text,
                                                                               "Password" : password.text,
                                                                               "Class" : classed.text,
                                                                               "Parent's Contact" : parent_contact.text,
                                                                               "Gender" : gender.text,
                                                                               "Date of Birth" : date_of_birth.text}})
        toast("Student Updated")
    else:
        invalid_roll.open()

def delete_student(roll, img, name, age, email, contact, address, password, classed, parent_contact, gender, date_of_birth):
    if len(selected_roll) > 0:
        myCollection.delete_one({"Roll Number" : selected_roll[0]})

        img.source = "images/icon.png"
        roll.text = ""
        name.text = ""
        age.text = ""
        email.text = ""
        contact.text = ""
        address.text = ""
        password.text = ""
        classed.text = ""
        parent_contact.text = ""
        gender.text = ""
        date_of_birth.text = ""

        toast("Student Deleted")
    else:
        invalid_roll.open()
