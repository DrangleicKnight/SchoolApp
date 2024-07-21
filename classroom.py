from kivymd.uix.card import MDCard
from kivymd.uix.fitimage import FitImage
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from pymongo import MongoClient

client = MongoClient("localhost", 27017)
myDB = client.get_database("MCA")
myCollection = myDB.get_collection("Students")

def generate_students(self):
    screen = self.root.get_screen("classroom").ids.grid
    screen.clear_widgets()

    images = []
    roll_nos = []
    names = []
    classeds = []
    ages = []
    emails = []

    for student in myCollection.find():
        images.append(student.get("Image"))
        roll_nos.append(student.get("Roll Number"))
        names.append(student.get("Name"))
        classeds.append(student.get("Class"))
        ages.append(student.get("Age"))
        emails.append(student.get("E-mail"))

    def generate_cards(image, roll, name, classed, age, email):
        studentCard = MDCard(md_bg_color = (1, 1, 1, .8), size_hint = (1, None), height = "120dp", elevation = 1)
        layout = MDFloatLayout()
        image = FitImage(size_hint = (.25, .9), pos_hint = {"center_x": .15, "center_y": .5},
                         source = image, radius = [20])

        label = MDLabel(text = "Roll No. :", pos_hint = {"center_x": .82, "center_y": .85})
        label.font_name = "fonts/Poppins-SemiBold.ttf"
        label.font_size = "13sp"

        label_roll = MDLabel(text = roll, pos_hint = {"center_x": .96, "center_y": .85})
        label_roll.font_name = "fonts/Poppins-SemiBold.ttf"
        label_roll.font_size = "13sp"

        label2 = MDLabel(text = "Name :", pos_hint = {"center_x": .82, "center_y": .68})
        label2.font_name = "fonts/Poppins-SemiBold.ttf"
        label2.font_size = "13sp"

        label_name = MDLabel(text = name, pos_hint = {"center_x": .96, "center_y": .68})
        label_name.font_name = "fonts/Poppins-SemiBold.ttf"
        label_name.font_size = "13sp"

        label3 = MDLabel(text = "Class :", pos_hint = {"center_x": .82, "center_y": .51})
        label3.font_name = "fonts/Poppins-SemiBold.ttf"
        label3.font_size = "13sp"

        label_class = MDLabel(text = classed, pos_hint = {"center_x": .96, "center_y": .51})
        label_class.font_name = "fonts/Poppins-SemiBold.ttf"
        label_class.font_size = "13sp"

        label4 = MDLabel(text = "Age :", pos_hint = {"center_x": .82, "center_y": .34})
        label4.font_name = "fonts/Poppins-SemiBold.ttf"
        label4.font_size = "13sp"

        label_age = MDLabel(text = age, pos_hint = {"center_x": .96, "center_y": .34})
        label_age.font_name = "fonts/Poppins-SemiBold.ttf"
        label_age.font_size = "13sp"

        label5 = MDLabel(text = "E-Mail :", pos_hint = {"center_x": .82, "center_y": .17})
        label5.font_name = "fonts/Poppins-SemiBold.ttf"
        label5.font_size = "13sp"

        label_email = MDLabel(text = email, pos_hint = {"center_x": .96, "center_y": .17})
        label_email.font_name = "fonts/Poppins-SemiBold.ttf"
        label_email.font_size = "13sp"

        layout.add_widget(image)
        layout.add_widget(label)
        layout.add_widget(label_roll)
        layout.add_widget(label2)
        layout.add_widget(label_name)
        layout.add_widget(label3)
        layout.add_widget(label_class)
        layout.add_widget(label4)
        layout.add_widget(label_age)
        layout.add_widget(label5)
        layout.add_widget(label_email)
        studentCard.add_widget(layout)

        screen.add_widget(studentCard)

    for i in range(len(roll_nos)):
        generate_cards(images[i], roll_nos[i], names[i], classeds[i], ages[i], emails[i])