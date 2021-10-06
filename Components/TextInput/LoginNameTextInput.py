from kivy.uix.textinput import TextInput


class LoginNameTextInput(TextInput):
    def __init__(self):
        super().__init__()
        self.multiline = False