import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.lang import Builder 

class MyApp(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x":0.5, "center_y":0.5}

        #widgets image
        self.window.add_widget(Image(source='pikes.png'))

        #widgets text
        self.texto = Label(
                    text='Qual seu nome?',
                    font_size = 18,
                    color = 'white',
                    )

        self.window.add_widget(self.texto)

        #widgets input
        self.user = TextInput(
                    multiline = False,
                    padding_y = (20, 20),
                    padding_x = (20, 20),
                    size_hint = (1, 0.5),
                    )
        self.window.add_widget(self.user)

        #widgets button
        self.button = Button(
                        text='ENVIAR',
                        size_hint = (1, 0.5),
                        bold = True,
                        background_color = "red",
                        background_normal = ""
                        )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window
    
    def callback(self, instance):
        self.texto.text = "Ola " + self.user.text + "!"
        
if __name__ == '__main__':
    MyApp().run()