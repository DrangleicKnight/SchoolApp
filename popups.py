from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.pickers import MDDatePicker

def date_picker(self):
    datePicker = MDDatePicker(pos_hint = {"center_x" : .5, "center_y" : .6})
    datePicker.open()
    datePicker.on_ok_button_pressed = lambda: date_maker(self, datePicker)

def date_maker(self, datePicker):
    selected_date = f"{datePicker.sel_day}/{datePicker.sel_month}/{datePicker.sel_year}"
    date = self.root.get_screen("add_student").ids.date_of_birth
    date.text = selected_date

def dropup(self):
    screen = self.root.get_screen("add_student").ids.gender

    def text1():
        screen.text = "Male"
        dropdown.dismiss()

    def text2():
        screen.text = "Female"
        dropdown.dismiss()

    items1 = [
        {
            "viewclass": "OneLineListItem",
            "text": "Male",
            "on_press": lambda: text1()
        },
        {
            "viewclass": "OneLineListItem",
            "text": "Female",
            "on_press": lambda: text2()
        }
    ]
    dropdown = MDDropdownMenu(items=items1,
                              width_mult=2,
                              max_height=120,
                              pos_hint={"center_x": .5, "center_y": .5})
    dropdown.caller = self.root.get_screen("add_student").ids.genderbtn
    dropdown.open()


def course(self):
    screen = self.root.get_screen("add_student").ids.classed

    def text1():
        screen.text = "FYMCA"
        dropdown.dismiss()

    def text2():
        screen.text = "SYMCA"
        dropdown.dismiss()

    items1 = [
        {
            "viewclass": "OneLineListItem",
            "text": "FYMCA",
            "on_press": lambda: text1()
        },
        {
            "viewclass": "OneLineListItem",
            "text": "SYMCA",
            "on_press": lambda: text2()
        }
    ]
    dropdown = MDDropdownMenu(items=items1,
                              width_mult=2,
                              max_height=120,
                              pos_hint={"center_x": .5, "center_y": .5})
    dropdown.caller = self.root.get_screen("add_student").ids.classbtn
    dropdown.open()
