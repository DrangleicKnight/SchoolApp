from kivy.uix.video import Video
from kivymd.uix.button import MDIconButton
from kivymd.uix.card import MDCard
from kivymd.uix.fitimage import FitImage
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel

boolean_value = ["False"]
maintain_card = []

def about_us_card(self):
    main_card = MDCard(md_bg_color = "black", size_hint=(.9, .6), pos_hint={"center_x": .5, "center_y": .45}, radius=[10])
    layout = MDFloatLayout()

    label = MDLabel(text="About Us", halign="center", theme_text_color = "Custom", text_color = "orange",
                    pos_hint={"center_x": .12, "center_y": .95})
    label.font_size = "19sp"
    label.font_name = "fonts/Poppins-Bold.ttf"

    icon = MDIconButton(size_hint=(.14, .12), pos_hint={"center_x": .96, "center_y": .96})
    icon.on_press = lambda : remove_about_card(self)
    image = FitImage(size_hint=(.12, .11), pos_hint={"center_x": .96, "center_y": .96}, radius=[120],
                     source="images/cross2.jpg")

    inner_card = MDCard(size_hint=(.95, .87), pos_hint={"center_x": .5, "center_y": .46}, radius=[20],
                        md_bg_color=(133 / 255, 0, 0, .9))
    layout2 = MDFloatLayout()
    label2 = MDLabel(
        text="Adnan's School of Wizardry and WitchCraft was founded in 2023 at Kohinoor Reina , by Adnan Sayyed, in the comfort of his couch. \nThe reason for the creation of this Institute is to teach students about the benefits of being based and to inculcate values in them that will help them in securing bitches",
        pos_hint={"center_x": .5, "center_y": .83}, theme_text_color="Custom", text_color="orange", size_hint=(.9, 1))
    label2.font_size = "13sp"
    label2.font_name = "fonts/Poppins-SemiBold.ttf"

    video = Video(size_hint=(.95, 1), pos_hint={"center_x": .5, "center_y": .36}, state="play", options={'eos': "loop"},
                  source="images/allana.mp4")

    layout2.add_widget(label2)
    layout2.add_widget(video)
    inner_card.add_widget(layout2)

    layout.add_widget(icon)
    layout.add_widget(image)
    layout.add_widget(label)
    layout.add_widget(inner_card)

    main_card.add_widget(layout)

    maintain_card.clear()
    maintain_card.append(main_card)

def add_about_card(self):
    screen = self.root.get_screen("homepage")

    if boolean_value[0] == "False":
        screen.add_widget(maintain_card[0])
        boolean_value[0] = "True"


def remove_about_card(self):
    screen = self.root.get_screen("homepage")

    if boolean_value[0] == "True":
        screen.remove_widget(maintain_card[0])
        boolean_value[0] = "False"
