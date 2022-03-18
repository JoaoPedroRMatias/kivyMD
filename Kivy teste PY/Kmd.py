from cgitb import text
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField #Caso queira fazer de forma comumd, para ser melhor elaborado usar o metodo builder
from kivy.lang import Builder
from helpers import username_helper

class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_hue = "500"
        screen = Screen()

        #-=-=-=-=-=-=-=-=- WIDGET EM LABEL E ICONE -=-=-=-=-=-=-=-=-
        #label = MDLabel(text='Ola mundo!', halign='center', theme_text_color="Custom", text_color=(255/255,92/255,92/255),  font_style="Subtitle2")
        #screen.add_widget(label)
        #icon_label = MDIcon(icon='application', halign='center')
        #screen.add_widget(icon_label)
        
        #-=-=-=-=-=-=-=-=- WIDGET EM BUTTON -=-=-=-=-=-=-=-=-
        #btn_flat = MDRectangleFlatButton(text='ENVIAR',
                                #pos_hint={'center_x':0.5, 'center_y':0.5})
        #screen.add_widget(btn_flat)

        #-=-=-=-=-=-=-=-=- WIDGET EM INPUT -=-=-=-=-=-=-=-=-
        #username = MDTextField(text='Username:', 
                            #pos_hint={'center_x':0.5, 'center_y':0.5},
                            #size_hint_x= None, width=300) (METODO SIMPLES)

        button = MDRectangleFlatButton(text='LOGIN', pos_hint={'center_x':0.5, 'center_y':0.4})

        username = Builder.load_string(username_helper)
        screen.add_widget(button)
        screen.add_widget(username)
        return screen

MyApp().run()