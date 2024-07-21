from kivymd.uix.pickers import MDDatePicker

do_vid = True

def dateTime(self):
    datepicker = MDDatePicker(pos_hint = {"center_x" : .5, "center_y" : .5})
    datepicker.open()
    datepicker.on_ok_button_pressed = lambda : dated(self, datepicker)

def dated(self, dPicker):
    months = ["January", "February", "March", "April", "May",
              "June", "July", "August", "September", "October", "November", "December"]

    global day
    global month

    if dPicker.sel_day < 10:
        day = f"{0}{dPicker.sel_day}"
    else:
        day = dPicker.sel_day

    if dPicker.sel_month < 10:
        month = f"{0}{dPicker.sel_month}"
    else:
        month = dPicker.sel_month

    today = f"{day}-{month}-{dPicker.sel_year}"
    sheet = f"{months[dPicker.sel_month - 1]} - {dPicker.year}"

    date_screen = self.root.get_screen("attendance").ids.toDate
    sheet_screen = self.root.get_screen("attendance").ids.sheetName

    date_screen.text = today
    sheet_screen.text = sheet

    button = self.root.get_screen("attendance").ids.btn

    date_screen = self.root.get_screen("attendance").ids.toDate
    if len(date_screen.text) > 0:
        button.disabled = False


