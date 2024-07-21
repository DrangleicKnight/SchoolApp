from kivymd.uix.button import MDFlatButton, MDRoundFlatButton
from kivymd.uix.dialog import MDDialog
from pymongo import MongoClient

from classroom import generate_students
from library import load_books

client = MongoClient("localhost", 27017)
myDb = client.get_database("MCA")
myStudentCollection = myDb.get_collection("Students")
myTeacherCollection = myDb.get_collection("Teachers")

invalidCreds = MDDialog(size_hint=(.5, .15), pos_hint={"center_x": .5, "center_y": .5},
                        title="Invalid Credentials",
                        buttons=[MDRoundFlatButton(text="Dismiss", md_bg_color = (133/255, 0, 0, 1),
                                                   on_press=lambda a: invalidCreds.dismiss())])

emptyFields = MDDialog(size_hint=(.5, .15), pos_hint={"center_x": .5, "center_y": .5},
                        title="Fill both fields",
                        buttons=[MDRoundFlatButton(text="Dismiss", md_bg_color = (133/255, 0, 0, 1),
                                                   on_press=lambda a: emptyFields.dismiss())])
doesntExist = MDDialog(size_hint=(.5, .15), pos_hint={"center_x": .5, "center_y": .5},
                        title="Account doesn't exist",
                        buttons=[MDRoundFlatButton(text="Dismiss", md_bg_color = (133/255, 0, 0, 1),
                                                   on_press=lambda a: emptyFields.dismiss())])


def validate_student(self, email, password):
    if len(email.text) and len(password.text) > 0:
        if myStudentCollection.find_one({"E-mail": email.text}):
            for student in myStudentCollection.find({"E-mail": email.text}):
                if student.get("E-mail") == email.text and student.get("Password") == password.text:
                    self.root.current = "homepage"
                    load_books(self)
                    generate_students(self)
                    self.global_roll = student.get("Roll Number")
                    self.global_name = student.get("Name")
                    self.global_email = student.get("E-Mail")
                    email.text = ""
                    password.text = ""
        else:
            doesntExist.open()
    else:
        emptyFields.open()


def validate_teacher(self, email, password):
    if len(email.text) and len(password.text) > 0:
        if myTeacherCollection.find_one({"E-mail": email.text}):
            for teacher in myTeacherCollection.find({"E-mail": email.text}):
                if teacher.get("E-mail") == email.text and teacher.get("Password") == password.text:
                    self.root.current = "teachers_dashboard"
                    email.text = ""
                    password.text = ""
                else:
                    invalidCreds.open()
        else:
            doesntExist.open()
    else:
        emptyFields.open()
