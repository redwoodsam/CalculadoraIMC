import locale
import os

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

locale.setlocale(locale.LC_ALL, 'pt-BR')

from kivy import Config
Config.set('graphics', 'multisamples', '0')
Config.set('graphics', 'resizable', '0')
Config.set('input', 'mouse', 'mouse, disable_multitouch')
from kivy.core.window import Window
Window.size = (250, 450)

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

def calculoimc(altura, peso):
    imc = str(float(peso)/float(altura)**2)
    return imc

class Janela(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def changefocus(self):
        self.ids.peso.focus = True

    def clickbtn(self):

        try:
            self.altura = locale.atof(self.ids.altura.text)
            self.peso = locale.atof(self.ids.peso.text)

            self.resultadoimc = float(calculoimc(self.altura, self.peso))

            if self.resultadoimc < 18.5:
                self.ids.output.text = "IMC: {:.2f} \n \nVocê está abaixo do peso ideal." .format(self.resultadoimc)
                
            if self.resultadoimc >= 18.5 and self.resultadoimc <= 24.9:
                self.ids.output.text = "IMC: {:.2f} \n \nParabéns! \nVocê está em boa forma." .format(self.resultadoimc)
                
            if self.resultadoimc >= 25 and self.resultadoimc <= 29.9:
                self.ids.output.text = "IMC: {:.2f} \n \nVocê está acima do peso." .format(self.resultadoimc)
                
            if self.resultadoimc >= 30 and self.resultadoimc <= 39.9:
                self.ids.output.text = "IMC: {:.2f} \n \nVocê está Obeso. Recomendamos procurar um especialista." .format(self.resultadoimc)
                
            if self.resultadoimc >= 40:
                self.ids.output.text = "IMC: {:.2f} \n \nVocê está com Obesidade grave!! recomendamos procurar um especialista.".format(self.resultadoimc)           
            
        except ValueError:
            self.ids.output.text = "Digite valores válidos, por favor."
        
        self.ids.altura.text = ""
        self.ids.peso.text = ""   
    

class CalculadoraApp(App):
    def build(self):
        return Janela()

if __name__ == "__main__":
    CalculadoraApp().run()