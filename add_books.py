import os

from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivymd.toast import toast
from kivymd.uix.button import MDRaisedButton, MDRoundFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.menu import MDDropdownMenu
from pdf2image import convert_from_path, pdfinfo_from_path
from pymongo import MongoClient

client = MongoClient("localhost", 27017)
myDB = client.get_database("MCA")
myCollection = myDB.get_collection("Books")

location = []
book_title = []

invalid_type = MDDialog(size_hint=(.5, .1), pos_hint={"center_x": .5, "center_y": .5},
                            title="Invalid File type", text="File should be png, jpg or gif",
                            buttons=[MDRoundFlatButton(text="Dismiss", md_bg_color=(133 / 255, 0, 0, 1),
                                                       on_press=lambda a: invalid_type.dismiss())])

def genres(self):
    screen = self.root.get_screen("add_books").ids.genre

    def text1():
        screen.text = "Academics"
        dropdown.dismiss()

    def text2():
        screen.text = "Comics"
        dropdown.dismiss()

    def text3():
        screen.text = "Thriller"
        dropdown.dismiss()

    def text4():
        screen.text = "Mystery"
        dropdown.dismiss()

    items1 = [
        {
            "viewclass": "OneLineListItem",
            "text": "Academics",
            "on_press": lambda: text1()
        },
        {
            "viewclass": "OneLineListItem",
            "text": "Comics",
            "on_press": lambda: text2()
        },
        {
            "viewclass": "OneLineListItem",
            "text": "Thriller",
            "on_press": lambda: text3()
        },
        {
            "viewclass": "OneLineListItem",
            "text": "Mystery",
            "on_press": lambda: text4()
        }
    ]
    dropdown = MDDropdownMenu(items=items1,
                              width_mult=2,
                              max_height=200,
                              pos_hint={"center_x": .5, "center_y": .5})
    dropdown.caller = self.root.get_screen("add_books").ids.genre_button
    dropdown.open()

def image_select(self):
    popup = Popup(size_hint=(.8, .6), title="Choose Image")
    fileChooser = FileChooserListView()
    fileChooser.add_widget(MDRaisedButton(text="Select",
                                          pos_hint={"center_x": .5, "center_y": .2},
                                          size_hint=(.4, .2),
                                          md_bg_color=(176 / 255, 71 / 255, 89 / 255, .7),
                                          on_press=lambda a: file_chooser(self, fileChooser.selection)))
    popup.add_widget(fileChooser)
    popup.open()


def file_chooser(self, selection):
    location.clear()
    selected = "".join(selection)

    if selected.endswith(".png") or selected.endswith(".jpg") or selected.endswith(".jpeg"):
        location.append(selected)
        screen = self.root.get_screen("add_books").ids.book_image
        screen.source = "".join(location)
    else:
        invalid_type.open()

def book_select(self):
    popup = Popup(size_hint=(.8, .6), title="Choose Book")
    fileChooser = FileChooserListView()
    fileChooser.add_widget(MDRaisedButton(text="Select",
                                          pos_hint={"center_x": .5, "center_y": .2},
                                          size_hint=(.4, .2),
                                          md_bg_color=(176 / 255, 71 / 255, 89 / 255, .7),
                                          on_press=lambda a: make_book(self, fileChooser.selection, popup)))
    popup.add_widget(fileChooser)
    popup.open()

def make_book(self, selection, popup):
    selected = "".join(selection)
    book_name = self.root.get_screen("add_books").ids.book_title
    add_button = self.root.get_screen("add_books").ids.add_it

    succesful_dialog = MDDialog(size_hint=(.5, .15), pos_hint={"center_x": .5, "center_y": .5},
                        title="Book Created Succesfully",
                        buttons=[MDRoundFlatButton(text="Dismiss", md_bg_color = (133/255, 0, 0, 1),
                                                   on_press=lambda a: succesful_dialog.dismiss())])
    empty_field = MDDialog(size_hint=(.5, .15), pos_hint={"center_x": .5, "center_y": .5},
                                title="Enter title First",
                                buttons=[MDRoundFlatButton(text="Dismiss", md_bg_color=(133 / 255, 0, 0, 1),
                                                           on_press=lambda a: empty_field.dismiss())])

    if len(book_name.text) > 1:
        if selected.endswith(".pdf"):
            if book_name.text not in os.listdir("images/students/books"):
                os.mkdir(f"images/students/books/{book_name.text}")
                info = pdfinfo_from_path(selected)
                maxPages = info["Pages"]
                for page in range(1, maxPages + 1, 10):
                    convert_from_path(selected, dpi=80, first_page=page, last_page=min(page + 10 - 1, maxPages), fmt='jpeg',
                                      output_folder=f"images/students/books/{book_name.text}/", output_file=f"Page{str(page)}.jpg")
                popup.dismiss()
                succesful_dialog.open()
                add_button.disabled = False
            else:
                print("Already there")
        else:
            invalid_type.open()
    else:
        empty_field.open()

def add_book(self, genre, title, description):
    invalid_dialog = MDDialog(size_hint=(.5, .15), pos_hint={"center_x": .5, "center_y": .5},
                                title="Fill all details",
                                buttons=[MDRoundFlatButton(text="Dismiss", md_bg_color=(133 / 255, 0, 0, 1),
                                                           on_press=lambda a: invalid_dialog.dismiss())])
    if len(genre.text) and len(title.text) and len(description.text) and len(location) > 0:
        myCollection.insert_one({"Genre": genre.text,
                                 "Title": title.text,
                                 "Description": description.text,
                                 "Image": location[0]})
        toast("Book Added")

        screen = self.root.get_screen("add_books").ids
        screen.genre.text = ""
        screen.book_title.text = ""
        screen.details.text = ""
        location.clear()
    else:
        invalid_dialog.open()


# below is the first method for creating books.
# The app appears to be more laggy after this functions but has less line of code and easier to understand.

    # images = convert_from_path(selected, fmt='jpeg', dpi=80)
    # for i in range(len(images)):
    #       images[i].save(f"images/students/books/{book_name.text}/Page" + str(i) + '.jpg', 'JPEG')


# and this is the second method, takes a little more time but app seems to be more stable after completion:

    # info = pdfinfo_from_path(selected)
    # maxPages = info["Pages"]
    # for page in range(1, maxPages + 1, 10):
    #     convert_from_path(selected, dpi=80, first_page=page, last_page=min(page + 10 - 1, maxPages), fmt='jpeg',
    #                       output_folder=f"images/students/books/{book_name.text}/", output_file=f"Page{str(page)}.jpg")