from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivymd.uix.button import MDRoundFlatButton, MDFlatButton
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivymd.uix.fitimage import FitImage
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.textfield import MDTextField

card_boolean = ["False"]

question_maker_card = []
butoon2 = []

card = []

exam_card = []

layouted = []

questions_grid = [GridLayout()]

subject_name = []
marks = []

question_answer = []
the_question = ["question"]
answer = ["answer"]
obtained_marks = []

def question_maker(self):
    card = MDCard(size_hint=(1, None), height="450dp", elevation=5, radius=[20, 20, 0, 0])
    layout = MDFloatLayout()

    label1 = MDLabel(text="Add a question", pos_hint={"center_x": .18, "center_y": .9}, halign="center")
    label1.font_size = "17sp"
    label1.font_name = "fonts/Poppins-SemiBold.ttf"

    question = MDTextField(mode="rectangle", pos_hint={"center_x": .47, "center_y": .75},
                           theme_text_color = "Custom", text_color = "black", text_color_normal = "black", text_color_focus = "black")
    question.size_hint = (.8, .2)

    label2 = MDLabel(text="Options", pos_hint={"center_x": .12, "center_y": .59}, halign="center")
    label2.font_size = "17sp"
    label2.font_name = "fonts/Poppins-SemiBold.ttf"

    check1 = MDCheckbox(group=question.text, size_hint=(.05, .05), pos_hint={"center_x": .08, "center_y": .49})
    check1.on_press = lambda : answer_setter(option1, answer_field)
    option1 = MDTextField(mode="round", size_hint=(.4, .09), pos_hint={"center_x": .32, "center_y": .49},
                          theme_text_color = "Custom", text_color = "black", text_color_normal = "black", text_color_focus = "black")
    option1.font_size = "12sp"

    check2 = MDCheckbox(group=question.text, size_hint=(.05, .05), pos_hint={"center_x": .08, "center_y": .39})
    check2.on_press = lambda: answer_setter(option2, answer_field)
    option2 = MDTextField(mode="round", size_hint=(.4, .09), pos_hint={"center_x": .32, "center_y": .39},
                          theme_text_color = "Custom", text_color = "black", text_color_normal = "black", text_color_focus = "black")
    option2.font_size = "12sp"

    check3 = MDCheckbox(group=question.text, size_hint=(.05, .05), pos_hint={"center_x": .08, "center_y": .29})
    check3.on_press = lambda: answer_setter(option3, answer_field)
    option3 = MDTextField(mode="round", size_hint=(.4, .09), pos_hint={"center_x": .32, "center_y": .29},
                          theme_text_color = "Custom", text_color = "black", text_color_normal = "black", text_color_focus = "black")
    option3.font_size = "12sp"

    check4 = MDCheckbox(group=question.text, size_hint=(.05, .05), pos_hint={"center_x": .08, "center_y": .19})
    check4.on_press = lambda: answer_setter(option4, answer_field)
    option4 = MDTextField(mode="round", size_hint=(.4, .09), pos_hint={"center_x": .32, "center_y": .19},
                          theme_text_color = "Custom", text_color_normal = "black", text_color_focus = "black")
    option4.font_size = "12sp"

    label4 = MDLabel(text="Marks:", pos_hint={"center_x": .62, "center_y": .4}, halign="center")
    label4.font_size = "14sp"
    label4.font_name = "fonts/Poppins-SemiBold.ttf"
    marks_field = TextInput(size_hint=(.09, .07), pos_hint={"center_x": .62, "center_y": .33})

    label3 = MDLabel(text="Answer:", pos_hint={"center_x": .63, "center_y": .26}, halign="center")
    label3.font_size = "14sp"
    label3.font_name = "fonts/Poppins-SemiBold.ttf"
    answer_field = TextInput(size_hint=(.34, .07), disabled = True, pos_hint={"center_x": .74, "center_y": .19})

    button1 = MDRoundFlatButton(text="Add Question", size_hint=(.4, .09), md_bg_color = (133/255, 0, 0, 1),
                                pos_hint={"center_x": .25, "center_y": .07})
    button1.on_press = lambda: make_question(self, question, option1, option2, option3, option4, answer_field, marks_field)

    button2 = MDRoundFlatButton(text="Prepare Paper", size_hint=(.4, .09), md_bg_color = (133/255, 0, 0, 1),
                                pos_hint={"center_x": .73, "center_y": .07})
    button2.on_press = lambda: make_paper(self)
    button2.disabled = True

    butoon2.append(button2)

    layout.add_widget(label1)
    layout.add_widget(question)
    layout.add_widget(label2)
    layout.add_widget(check1)
    layout.add_widget(option1)
    layout.add_widget(check2)
    layout.add_widget(option2)
    layout.add_widget(check3)
    layout.add_widget(option3)
    layout.add_widget(check4)
    layout.add_widget(option4)
    layout.add_widget(label3)
    layout.add_widget(answer_field)
    layout.add_widget(label4)
    layout.add_widget(marks_field)
    layout.add_widget(button1)
    layout.add_widget(button2)

    card.add_widget(layout)
    question_maker_card.append(card)

def answer_setter(option, answer_field):
    answer = option.text
    answer_field.text = answer

def validate_answer(question, answer, marks):
    answer_pair = {question.text : answer.text}

    if answer_pair in question_answer:
        obtained_marks.append(int(marks.text))
        question_answer.remove({question.text : answer.text})

def add_card(self):
    screen = self.root.get_screen("exam")
    if card_boolean[0] == "False":
        screen.add_widget(question_maker_card[0])
        card_boolean[0] = "True"

def remove_card(self):
    screen = self.root.get_screen("exam")
    if card_boolean[0] == "True":
        screen.remove_widget(question_maker_card[0])
        card_boolean[0] = "False"

def make_question(self, questions, options1, options2, options3, options4, answer_field, marks_field):
    griddy = self.root.get_screen("exam").ids.grid
    quest_grid = questions_grid[0]

    get_sub_name = self.root.get_screen("exam").ids.sub_name
    get_marks = self.root.get_screen("exam").ids.marks

    invalid_details = MDDialog(size_hint=(.5, .15), pos_hint={"center_x": .5, "center_y": .5},
                               text="Fill all details",
                               buttons=[MDFlatButton(text="Dismiss", on_press=lambda a: invalid_details.dismiss())])

    if len(get_sub_name.text) and len(get_marks.text) and len(questions.text) and len(options1.text) and len(options3.text)\
            and len(options4.text) and len(answer_field.text) and len(marks_field.text) > 0:
        #set question and answer
        question_answer.append({questions.text: answer_field.text})

        subject_name.append(get_sub_name.text)
        marks.append(get_marks.text)

        questify = butoon2[0]

        def prepare_question(grid):
            card = MDCard(md_bg_color = (0, 0, 0, .1), size_hint=(.7, None), height="250dp", radius=[20])
            layout = MDFloatLayout()

            question = MDLabel(text=questions.text,
                               size_hint=(.9, 1), pos_hint={"center_x": .5, "center_y": .87})
            question.font_name = "fonts/Poppins-SemiBold.ttf"
            question.font_size = "16sp"

            check1 = MDCheckbox(group=question.text, size_hint=(.1, .1), pos_hint={"center_x": .08, "center_y": .65})
            option1 = MDLabel(text=options1.text, size_hint=(.5, 1), pos_hint={"center_x": .4, "center_y": .65})
            option1.font_name = "fonts/Poppins-Regular.ttf"
            option1.font_size = "14sp"
            check1.on_press = lambda : validate_answer(question, option1, label_marks)

            check2 = MDCheckbox(group=question.text, size_hint=(.1, .1), pos_hint={"center_x": .08, "center_y": .5})
            option2 = MDLabel(text=options2.text, size_hint=(.5, 1), pos_hint={"center_x": .4, "center_y": .5})
            option2.font_name = "fonts/Poppins-Regular.ttf"
            option2.font_size = "14sp"
            check2.on_press = lambda: validate_answer(question, option2, label_marks)

            check3 = MDCheckbox(group=question.text, size_hint=(.1, .1), pos_hint={"center_x": .08, "center_y": .35})
            option3 = MDLabel(text=options3.text, size_hint=(.5, 1), pos_hint={"center_x": .4, "center_y": .35})
            option3.font_name = "fonts/Poppins-Regular.ttf"
            option3.font_size = "14sp"
            check3.on_press = lambda: validate_answer(question, option3, label_marks)

            check4 = MDCheckbox(group=question.text, size_hint=(.1, .1), pos_hint={"center_x": .08, "center_y": .2})
            option4 = MDLabel(text=options4.text, size_hint=(.5, 1), pos_hint={"center_x": .4, "center_y": .2})
            option4.font_name = "fonts/Poppins-Regular.ttf"
            option4.font_size = "14sp"
            check4.on_press = lambda: validate_answer(question, option4, label_marks)

            label1 = MDLabel(text = "Marks :", pos_hint = {"center_x": 1.28, "center_y": .15})
            label1.font_size = "13sp"
            label1.font_name = "fonts/Poppins-SemiBold.ttf"

            label_marks = MDLabel(text = marks_field.text, pos_hint = {"center_x": 1.39, "center_y": .15})
            label_marks.font_size = "13sp"
            label_marks.font_name = "fonts/Poppins-SemiBold.ttf"

            layout.add_widget(question)
            layout.add_widget(check1)
            layout.add_widget(check2)
            layout.add_widget(check3)
            layout.add_widget(check4)
            layout.add_widget(option1)
            layout.add_widget(option2)
            layout.add_widget(option3)
            layout.add_widget(option4)
            layout.add_widget(label1)
            layout.add_widget(label_marks)

            card.add_widget(layout)
            grid.add_widget(card)

        prepare_question(griddy)
        prepare_question(quest_grid)

        questify.disabled = False

        questions.text = ""
        options1.text = ""
        options2.text = ""
        options3.text = ""
        options4.text = ""
        answer_field.text = ""
    else:
        invalid_details.open()

def exam_paper():
    grid = GridLayout(cols=1)

    card = MDCard(md_bg_color=(133 / 255, 0, 0, .9), size_hint=(1, None), height="150dp",
                  radius=[0, 0, 15, 15], pos_hint={"center_x": .5, "center_y": .8})
    layout = MDFloatLayout()

    image = FitImage(size_hint=(.15, .5), radius=[50], pos_hint={"center_x": .1, "center_y": .5},
                     source="images/log.png")

    label1 = MDLabel(text="Adnan's Institute of WitchCraft", halign="center",
                     pos_hint={"center_x": .55, "center_y": .75})
    label1.font_size = "18sp"
    label1.font_name = "fonts/Poppins-Bold.ttf"

    label2 = MDLabel(text="SYMCA : 2021-2023", halign="center",
                     pos_hint={"center_x": .5, "center_y": .55})
    label2.font_size = "15sp"
    label2.font_name = "fonts/Poppins-Bold.ttf"

    layout.add_widget(image)
    layout.add_widget(label1)
    layout.add_widget(label2)

    layouted.append(layout)
    card.clear_widgets()
    card.add_widget(layouted[0])

    scroll = ScrollView(do_scroll_x=False, do_scroll_y=True)
    questions_grid[0] = GridLayout(cols=1, size_hint=(1, None), spacing=[0, 25], padding=[20, 10])
    layout2 = MDFloatLayout(size_hint=(1, None), height="200dp", pos_hint={"center_x": .5, "center_y": .6})

    label_roll = MDLabel(text="Roll No:", halign="center", pos_hint={"center_x": .12, "center_y": .8})
    label_roll.font_size = "18sp"
    label_roll.font_name = "fonts/Poppins-SemiBold.ttf"

    text_roll = MDTextField(mode="round", size_hint=(.2, .2), pos_hint={"center_x": .36, "center_y": .8},
                            text_color_normal = "black", text_color_focus = "black")
    text_roll.font_size = "15sp"

    label_name = MDLabel(text="Name:", halign="center", pos_hint={"center_x": .115, "center_y": .5})
    label_name.font_size = "18sp"
    label_name.font_name = "fonts/Poppins-SemiBold.ttf"

    text_name = MDTextField(mode="round", size_hint=(.4, .2), pos_hint={"center_x": .45, "center_y": .5},
                            text_color_normal = "black", text_color_focus = "black")
    text_name.font_size = "15sp"

    label_email = MDLabel(text="E-mail:", halign="center", pos_hint={"center_x": .123, "center_y": .2})
    label_email.font_size = "18sp"
    label_email.font_name = "fonts/Poppins-SemiBold.ttf"

    text_email = MDTextField(mode="round", size_hint=(.4, .2), pos_hint={"center_x": .45, "center_y": .2},
                            text_color_normal = "black", text_color_focus = "black")
    text_email.font_size = "15sp"

    layout2.add_widget(label_roll)
    layout2.add_widget(text_roll)
    layout2.add_widget(label_name)
    layout2.add_widget(text_name)
    layout2.add_widget(label_email)
    layout2.add_widget(text_email)

    questions_grid[0].add_widget(layout2)
    scroll.add_widget(questions_grid[0])

    grid.add_widget(card)
    grid.add_widget(scroll)

    exam_card.append(grid)

def make_paper(self):
    listed = self.root.get_screen("classroom").ids.listed

    label_subject = MDLabel(text = f"Subject : {subject_name[0]}", halign="center",
                            pos_hint={"center_x": .5, "center_y": .35})
    label_subject.font_size = "16sp"
    label_subject.font_name = "fonts/Poppins-Bold.ttf"

    label_marks = MDLabel(text = f"Marks : {marks[0]}", halign="center",
                          pos_hint={"center_x": .5, "center_y": .15})
    label_marks.font_size = "14sp"
    label_marks.font_name = "fonts/Poppins-Bold.ttf"

    layouted[0].add_widget(label_subject)
    layouted[0].add_widget(label_marks)

    button = MDRoundFlatButton(text="Submit", size_hint=(.2, None), height="80dp", md_bg_color=(0, 0, 0, 1),
                               theme_text_color="Custom", text_color=(1, 1, 1, 1),
                               pos_hint={"center_x": .5, "center_y": .1})

    button.on_press = lambda : [submit_exam(self, exam_opener, icon)]

    grid = questions_grid[0]
    grid.height = sum(child.height for child in grid.children) * 1.1

    exam_paperino = exam_card[-1]
    exam_paperino.add_widget(button)

    exam_opener = OneLineIconListItem(text=f"{subject_name[0]} Test")
    exam_opener.on_press = lambda: exam_dialog(self, exam_paperino)
    icon = IconLeftWidget(icon="clipboard")
    exam_opener.add_widget(icon)
    listed.add_widget(exam_opener)

    self.root.current = "teachers_dashboard"

def exam_dialog(self, paper):
    screen = self.root.get_screen("classroom")

    carda = MDCard(md_bg_color = (1, 1, 1, 1), size_hint=(.9, .9), pos_hint={"center_x": .5, "center_y": .5})

    carda.clear_widgets()
    carda.add_widget(paper)
    screen.add_widget(carda)

    card.append(carda)

def submit_exam(self, exam_opener, icon):
    screen = self.root.get_screen("classroom")

    if ((sum(obtained_marks) / int(marks[0])) * 100) > 40:
        text = "You have passed the test"
    else:
        text = "You have failed the test"

    score = MDDialog(size_hint=(.6, .15), pos_hint={"center_x": .5, "center_y": .5}, title = "Your Score",
                               text=f"Roll Number : {self.global_roll}\nName : {self.global_name}"
                                    f"\nScore : {sum(obtained_marks)} / {marks[0]} \n\n{text}",
                               buttons=[MDRoundFlatButton(text="Dismiss", md_bg_color = (133/255, 0, 0, 1),
                               on_press=lambda a: score.dismiss())])

    current_paper = card[0]

    screen.remove_widget(current_paper)
    icon.icon = "check-decagram"
    exam_opener.disabled = True
    score.open()
    screen.export_to_png(f"images/students/test_result/{self.global_roll}_{self.global_name}.png")

    card.clear()
    obtained_marks.clear()
    question_answer.clear()
    the_question.clear()
    answer.clear()

    subject_name.clear()
    marks.clear()

    exam_card.clear()
    layouted.clear()
    questions_grid[0].clear_widgets()

    exam_paper()
