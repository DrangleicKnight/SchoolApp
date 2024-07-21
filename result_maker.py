import mimetypes
import os
import smtplib
from email.message import EmailMessage

import img2pdf
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.dialog import MDDialog

student_roll = [3]
student_name = ["Adnan Sayyed"]

result_text = []

emptyFields = MDDialog(md_bg_color = (1, 1, 1, .7), size_hint=(.6, .13), pos_hint={"center_x": .5, "center_y": .5}, title = "Fill all Details",
                               buttons = [MDRoundFlatButton(text="Dismiss", md_bg_color = (133/255, 0, 0, 1),
                               on_press = lambda a: emptyFields.dismiss())])

def check_if_empty(roll, name, classed, dated, sem, pyth_int, pyth_ext, pyth_total, dev_int, dev_ext, dev_total, network_int,
                   network_ext, network_total, android_int, android_ext, android_total, os_int, os_ext, os_total, total,
                   obtained_total, percentage, result, attendance, generate_btn):
    if len(roll.text) and len(name.text) and len(classed.text) and len(dated.text) and len(sem.text) and len(pyth_int.text) and len(pyth_ext.text) and len(dev_int.text) and len(dev_ext.text) and len(network_int.text) and len(network_ext.text) and len(android_int.text) and len(android_ext.text) and len(os_int.text) and len(os_ext.text) and len(attendance.text) and len(total.text) > 0:
        student_roll.clear()
        student_name.clear()
        student_roll.append(roll.text)
        student_name.append(name.text)
        # validates info and generates result
        validation(pyth_int, pyth_ext, pyth_total, dev_int, dev_ext, dev_total, network_int, network_ext, network_total, android_int, android_ext, android_total, os_int, os_ext, os_total, total, obtained_total, percentage, result)
        generate_btn.disabled = False
    else:
        emptyFields.open()

def validation(pyth_int, pyth_ext, pyth_total, dev_int, dev_ext, dev_total, network_int, network_ext, network_total, android_int, android_ext, android_total, os_int, os_ext, os_total, total, obtained_total, percentage, result):
    pyth_total.text = str(int(pyth_int.text) + int(pyth_ext.text))
    dev_total.text = str(int(dev_int.text) + int(dev_ext.text))
    network_total.text = str(int(network_int.text) + int(network_ext.text))
    android_total.text = str(int(android_int.text) + int(android_ext.text))
    os_total.text = str(int(os_int.text) + int(os_ext.text))

    total_obtained_marks = int(pyth_total.text) + int(dev_total.text) + int(network_total.text) + int(android_total.text) + int(os_total.text)
    obtained_total.text = str(total_obtained_marks)

    percentage.text = str(int((total_obtained_marks / int(total.text)) * 100))

    if float(percentage.text) < 35:
        result.text = "Fail"
        result_text.clear()
        result_text.append(f"Your score and attendance for the semester is displayed in the marksheet! "
                           f"\n\nYou have failed the semester, make sure to meet the class co-ordinator."
                           f"\n\nWishing you luck for the next sem!")
    elif 35 < float(percentage.text) < 50:
        result.text = "Pass - Third Class"
        result_text.clear()
        result_text.append(f"Your score and attendance for the semester is displayed in the marksheet! "
                           f"\n\nYou have passed, but in Third Class."
                           f"\n\nMake sure you do better next sem!")
    elif 51 < float(percentage.text) < 60:
        result.text = "Pass - Second Class"
        result_text.clear()
        result_text.append(f"Your score and attendance for the semester is displayed in the marksheet! "
                           f"\n\nYou have passed, but in Second Class."
                           f"\n\nMake sure you do better next sem!")
    elif 61 < float(percentage.text) < 70:
        result.text = "Pass - First Class"
        result_text.clear()
        result_text.append(f"Your score and attendance for the semester is displayed in the marksheet! "
                           f"\n\nYou have passed with First Class! Congratulations!"
                           f"\nYour performance in this semester has been amazing!"
                           f"\n\nBest of luck for the next sem!")
    else:
        result.text = "Pass - First Class with Distinction"
        result_text.clear()
        result_text.append(f"Your score and attendance for the semester is displayed in the marksheet! "
                           f"\n\nYou have passed with First Class - Distinction!!! Congratulations!"
                           f"\nYour performance in this semester has been top notch"
                           f"\nYou have been an ideal student and delivered outstanding results in academics."
                           f"\n\nWe hope that you continue to perform the same in the next semester!")

def generate_result(self, roll, name, classed, sem, pyth_int, pyth_ext, pyth_total, dev_int, dev_ext, dev_total, network_int, network_ext, network_total, android_int, android_ext, android_total, os_int, os_ext, os_total, total, obtained_total, percentage, result, dated, attendance):
    result_screen = self.root.get_screen("result").ids

    result_screen.roll.text = f"Roll Number: {roll.text}"
    result_screen.name.text = f"Name: {name.text}"
    result_screen.classed.text = f"Class: {classed.text}"
    result_screen.sem.text = sem.text

    result_screen.pyth_int.text = pyth_int.text
    result_screen.dev_int.text = dev_int.text
    result_screen.network_int.text = network_int.text
    result_screen.android_int.text = android_int.text
    result_screen.os_int.text = os_int.text

    result_screen.pyth_ext.text = pyth_ext.text
    result_screen.dev_ext.text = dev_ext.text
    result_screen.network_ext.text = network_ext.text
    result_screen.android_ext.text = android_ext.text
    result_screen.os_ext.text = os_ext.text

    result_screen.pyth_total.text = pyth_total.text
    result_screen.dev_total.text = dev_total.text
    result_screen.network_total.text = network_total.text
    result_screen.android_total.text = android_total.text
    result_screen.os_total.text = os_total.text

    result_screen.grand_total.text = f"Grand total out of {total.text}"
    result_screen.total_obtained.text = obtained_total.text

    result_screen.percentage.text = f"Percentage : {percentage.text}%"
    result_screen.result_date.text = f"Result Date : {dated.text}"
    result_screen.result.text = f"Result : {result.text}"

    result_screen.attendance.text = f"Attendance for the Semester : {attendance.text}%"

    self.root.current = "result"

    roll.text = ""
    name.text = ""
    pyth_int.text = ""
    pyth_ext.text = ""
    pyth_total.text = ""
    dev_int.text = ""
    dev_ext.text = ""
    dev_total.text = ""
    network_int.text = ""
    network_ext.text = ""
    network_total.text = ""
    android_int.text = ""
    android_ext.text = ""
    android_total.text = ""
    os_int.text = ""
    os_ext.text = ""
    os_total.text = ""
    attendance.text = ""
    total.text = ""
    obtained_total.text = ""
    percentage.text = ""
    result.text = ""

def check_if_empty_again(self, result_sheet, email_address):
    if len(email_address.text) > 0:
        download_result(result_sheet)
        send_result(self, email_address)
    else:
        emptyFields.open()

def download_result(result):
    result.export_to_png(f"images/students/student_result/{student_roll[0]}_{student_name[0]}.png")

    with open(f"images/students/student_result/{student_roll[0]}_{student_name[0]}.pdf", "ab") as file:
        file.write(img2pdf.convert(f"images/students/student_result/{student_roll[0]}_{student_name[0]}.png"))

    for files in os.listdir(f"images/students/student_result/"):
        if files.endswith(".png"):
            os.remove(f"images/students/student_result/{files}")

def send_result(self, email):
    message = EmailMessage()
    sender = "adnanschoolofwitchcraft@gmail.com"
    recipient = email.text

    message['From'] = sender
    message['To'] = recipient

    message['Subject'] = f"Here's your result, {student_name[0]}"

    message.set_content(result_text[0])
    mime_type, _ = mimetypes.guess_type(f"images/students/student_result/{student_roll[0]}_{student_name[0]}.pdf")
    mime_type, mime_subtype = mime_type.split('/')
    with open(f"images/students/student_result/{student_roll[0]}_{student_name[0]}.pdf", "rb") as file:
        message.add_attachment(file.read(),
                               maintype=mime_type,
                               subtype=mime_subtype,
                               filename=f'{student_roll[0]}_{student_name[0]}.pdf"')
    print(message)
    mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
    mail_server.set_debuglevel(1)
    mail_server.login(sender, "lfpxxodpgugulbha")
    mail_server.send_message(message)
    mail_server.quit()

    student_roll.clear()
    student_name.clear()
    email.text = ""

    self.root.current = "result_maker"





