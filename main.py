import os

import pyautogui
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivymd.app import MDApp
from pymongo import MongoClient

from classroom import generate_students
from exam import question_maker, exam_paper
from generate_xl import load_data
from homepage import about_us_card
from library import load_books
from time_table import datatable

os.environ["KIVY_NO_CONSOLELOG"] = "1"
Window.size = (500, 780)

Window.top = int(pyautogui.size().height - Window.height * 1.38)
Window.left = int(pyautogui.size().width - Window.width * 1.45)


class MainApp(MDApp):
    client = MongoClient("localhost", 27017)
    myDatabase = client.get_database("MCA")
    studentsCollection = myDatabase.get_collection("Students")

    global_roll = StringProperty(None)
    global_name = StringProperty(None)
    global_email = StringProperty(None)

    def build(self):
        self.theme_cls.primary_palette = "Amber"

        global screen_manager
        screen_manager = ScreenManager(transition=NoTransition())

        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("teachers_dashboard.kv"))
        # screen_manager.add_widget(Builder.load_file("attendance.kv"))
        screen_manager.add_widget(Builder.load_file("exam.kv"))
        screen_manager.add_widget(Builder.load_file("add_teacher.kv"))
        screen_manager.add_widget(Builder.load_file("result.kv"))
        screen_manager.add_widget(Builder.load_file("result_maker.kv"))
        screen_manager.add_widget(Builder.load_file("update_student.kv"))
        screen_manager.add_widget(Builder.load_file("add_student.kv"))
        screen_manager.add_widget(Builder.load_file("homepage.kv"))
        screen_manager.add_widget(Builder.load_file("admission_form.kv"))
        screen_manager.add_widget(Builder.load_file("classroom.kv"))
        screen_manager.add_widget(Builder.load_file("teacher_icard.kv"))
        screen_manager.add_widget(Builder.load_file("time_table.kv"))
        screen_manager.add_widget(Builder.load_file("students_hub.kv"))
        screen_manager.add_widget(Builder.load_file("library.kv"))
        screen_manager.add_widget(Builder.load_file("add_books.kv"))
        screen_manager.add_widget(Builder.load_file("book.kv"))
        screen_manager.add_widget(Builder.load_file("icard.kv"))

        return screen_manager

    def on_start(self):
        load_data(self)
        generate_students(self)
        datatable(self)
        question_maker(self)
        exam_paper()
        load_books(self)
        about_us_card(self)
        Clock.schedule_interval(self.change_screen, 4)


    def change_screen(self, *args):
        screen = screen_manager.get_screen("homepage").ids
        screen.caroused.load_next()
        screen.caroused2.load_next()

if __name__ == "__main__":
    MainApp().run()
