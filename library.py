import os

from kivymd.uix.button import MDTextButton
from kivymd.uix.card import MDCard
from kivymd.uix.fitimage import FitImage
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from pymongo import MongoClient

client = MongoClient("localhost", 27017)
myDB = client.get_database("MCA")
myCollection = myDB.get_collection("Books")

def load_books(self):
    academics_image = []
    academics_book = []
    academics_desc = []

    comics_image = []
    comics_book = []
    comics_desc = []

    thriller_image = []
    thriller_book = []
    thriller_desc = []

    mystery_image = []
    mystery_book = []
    mystery_desc = []

    screen_academics = self.root.get_screen("library").ids.academics_grid
    screen_comics = self.root.get_screen("library").ids.comics_grid
    screen_thriller = self.root.get_screen("library").ids.thriller_grid
    screen_mystery = self.root.get_screen("library").ids.mystery_grid

    for books in myCollection.find():
        if books.get("Genre") == "Academics":
            academics_image.append(books.get("Image"))
            academics_book.append(books.get("Title"))
            academics_desc.append(books.get("Description"))
        elif books.get("Genre") == "Comics":
            comics_image.append(books.get("Image"))
            comics_book.append(books.get("Title"))
            comics_desc.append(books.get("Description"))
        elif books.get("Genre") == "Thriller":
            thriller_image.append(books.get("Image"))
            thriller_book.append(books.get("Title"))
            thriller_desc.append(books.get("Description"))
        elif books.get("Genre") == "Mystery":
            mystery_image.append(books.get("Image"))
            mystery_book.append(books.get("Title"))
            mystery_desc.append(books.get("Description"))

    def generate_academics(image, title, desc):
        book_card = MDCard(size_hint=(1, None), height="120dp", md_bg_color=(1, 1, 1, .8))
        layout = MDFloatLayout()
        book_image = FitImage(size_hint=(.22, .9), pos_hint={"center_x": .13, "center_y": .5}, radius=[15],
                              source=image)

        title_book = MDTextButton(text=title, halign = "left", pos_hint={"center_x": .47, "center_y": .7})
        title_book.font_size = "15sp"
        title_book.font_name = "fonts/Poppins-Bold.ttf"
        title_book.on_press = lambda : make_book(self, title_book.text)

        desc_book = MDLabel(text=desc, size_hint=(.7, 1), pos_hint={"center_x": .64, "center_y": .45})
        desc_book.font_size = "12sp"
        desc_book.font_name = "fonts/Poppins-SemiBold.ttf"

        layout.add_widget(book_image)
        layout.add_widget(title_book)
        layout.add_widget(desc_book)

        book_card.add_widget(layout)
        screen_academics.add_widget(book_card)

    def generate_comics(image, title, desc):
        book_card = MDCard(size_hint=(1, None), height="120dp", md_bg_color=(1, 1, 1, .8))
        layout = MDFloatLayout()
        book_image = FitImage(size_hint=(.22, .9), pos_hint={"center_x": .13, "center_y": .5}, radius=[15],
                              source=image)

        title_book = MDTextButton(text=title, halign = "left", pos_hint={"center_x": .47, "center_y": .7})
        title_book.font_size = "15sp"
        title_book.font_name = "fonts/Poppins-Bold.ttf"
        title_book.on_press = lambda: make_book(self, title_book.text)

        desc_book = MDLabel(text=desc, size_hint=(.7, 1), pos_hint={"center_x": .64, "center_y": .45})
        desc_book.font_size = "12sp"
        desc_book.font_name = "fonts/Poppins-SemiBold.ttf"

        layout.add_widget(book_image)
        layout.add_widget(title_book)
        layout.add_widget(desc_book)

        book_card.add_widget(layout)
        screen_comics.add_widget(book_card)

    def generate_thriller(image, title, desc):
        book_card = MDCard(size_hint=(1, None), height="120dp", md_bg_color=(1, 1, 1, .8))
        layout = MDFloatLayout()
        book_image = FitImage(size_hint=(.22, .9), pos_hint={"center_x": .13, "center_y": .5}, radius=[15],
                              source=image)

        title_book = MDTextButton(text=title, halign = "left", pos_hint={"center_x": .47, "center_y": .7})
        title_book.font_size = "15sp"
        title_book.font_name = "fonts/Poppins-Bold.ttf"
        title_book.on_press = lambda: make_book(self, title_book.text)

        desc_book = MDLabel(text=desc, size_hint=(.7, 1), pos_hint={"center_x": .64, "center_y": .45})
        desc_book.font_size = "12sp"
        desc_book.font_name = "fonts/Poppins-SemiBold.ttf"

        layout.add_widget(book_image)
        layout.add_widget(title_book)
        layout.add_widget(desc_book)

        book_card.add_widget(layout)
        screen_thriller.add_widget(book_card)

    def generate_mystery(image, title, desc):
        book_card = MDCard(size_hint=(1, None), height="120dp", md_bg_color=(1, 1, 1, .8))
        layout = MDFloatLayout()
        book_image = FitImage(size_hint=(.22, .9), pos_hint={"center_x": .13, "center_y": .5}, radius=[15],
                              source=image)

        title_book = MDTextButton(text=title, halign = "left", pos_hint={"center_x": .47, "center_y": .7})
        title_book.font_size = "15sp"
        title_book.font_name = "fonts/Poppins-Bold.ttf"
        title_book.on_press = lambda: make_book(self, title_book.text)

        desc_book = MDLabel(text=desc, size_hint=(.7, 1), pos_hint={"center_x": .64, "center_y": .45})
        desc_book.font_size = "12sp"
        desc_book.font_name = "fonts/Poppins-SemiBold.ttf"

        layout.add_widget(book_image)
        layout.add_widget(title_book)
        layout.add_widget(desc_book)

        book_card.add_widget(layout)
        screen_mystery.add_widget(book_card)

    screen_academics.clear_widgets()
    screen_comics.clear_widgets()
    screen_thriller.clear_widgets()
    screen_mystery.clear_widgets()

    for i in range(len(academics_book)):
        generate_academics(academics_image[i], academics_book[i], academics_desc[i])
    for i in range(len(comics_book)):
        generate_comics(comics_image[i], comics_book[i], comics_desc[i])
    for i in range(len(thriller_book)):
        generate_thriller(thriller_image[i], thriller_book[i], thriller_desc[i])
    for i in range(len(mystery_book)):
        generate_mystery(mystery_image[i], mystery_book[i], mystery_desc[i])

def make_book(self, path):
    screen = self.root.get_screen("book").ids.book_content
    screen.clear_widgets()

    title = self.root.get_screen("book").ids.titled
    title.text = path

    def make_pages(source):
        layout = MDFloatLayout()
        image = FitImage(source=source)

        layout.add_widget(image)
        screen.add_widget(layout)

    for images in os.listdir(f"images/students/books/{path}"):
        make_pages(f"images/students/books/{path}/{images}")

    self.root.current = "book"