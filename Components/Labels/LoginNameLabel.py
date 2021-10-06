from kivy.uix.label import Label

class LoginNameLabel(Label):
    def __init__(self):
        super().__init__()
        self.text = 'Enter Your Name'