from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image

from Components.Buttons.LoginButton import LoginButton
from Components.Images.LoginImage import LoginImage
from Components.Labels.LoginNameLabel import LoginNameLabel
from Components.TextInput.LoginNameTextInput import LoginNameTextInput


class ChatApp(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1

        #Declaring components
        self.nameLabel = LoginNameLabel()
        self.nameInput = LoginNameTextInput()
        self.loginButton = LoginButton()
        self.loginImage = LoginImage()
        # Button onClick Bindings
        self.loginButton.bind(on_press=self.LoginCallback)
        #Adding components to the widget
        self.window.add_widget(self.loginImage)
        self.window.add_widget(self.nameLabel)
        self.window.add_widget(self.nameInput)
        self.window.add_widget(self.loginButton)

        return self.window

    def LoginCallback(self,instance):
        self.nameLabel.text = self.nameInput.text

chatApp = ChatApp()

chatApp.run()