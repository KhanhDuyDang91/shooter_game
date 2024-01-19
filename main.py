from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView

from fomular import *

fomular = ""

class FunctionScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        label_1 = Label(text = "Choose your fomular to calculate:")

        self.btn_1 = Button(text='Ax^2 + Bx - C')
        self.btn_1.on_press = self.first_fomular

        self.btn_2 = Button(text='x^2 + 2Ax + A^2 = 0')
        self.btn_2.on_press = self.second_fomular

        self.btn_3 = Button(text='x^2 - 2Ax + A^2 = 0')
        self.btn_3.on_press = self.third_fomular

        self.btn_4 = Button(text='(Ax + B)^2 * (Ax - B)^2 = 0')
        self.btn_4.on_press = self.fourth_fomular

        self.btn_5 = Button(text='(Ax + B)^3 = 0')
        self.btn_5.on_press = self.fifth_fomular

        self.btn_6 = Button(text='(Ax - B)^3 = 0')
        self.btn_6.on_press = self.sixth_fomular

        self.btn_7 = Button(text='Ax^3 - B^3 = 0')
        self.btn_7.on_press = self.seventh_fomular



        layout_1 = BoxLayout(orientation='vertical', padding = 8, spacing =8)

        layout_1.add_widget(label_1)
        layout_1.add_widget(self.btn_1)
        layout_1.add_widget(self.btn_2)
        layout_1.add_widget(self.btn_3)
        layout_1.add_widget(self.btn_4)
        layout_1.add_widget(self.btn_5)
        layout_1.add_widget(self.btn_6)
        layout_1.add_widget(self.btn_7)


        self.add_widget(layout_1)

    def first_fomular(self):
        global fomular 
        fomular = "first"
        self.manager.current = "inputscreen"

    
    def second_fomular(self):
        global fomular 
        fomular = "second"
        self.manager.current = "inputscreen"

    def third_fomular(self):
        global fomular 
        fomular = "third"
        self.manager.current = "inputscreen"

    def fourth_fomular(self):
        global fomular 
        fomular = "fourth"
        self.manager.current = "inputscreen"

    def fifth_fomular(self):
        global fomular 
        fomular = "fifth"
        self.manager.current = "inputscreen"

    def sixth_fomular(self):
        global fomular 
        fomular = "sixth"
        self.manager.current = "inputscreen"

    def seventh_fomular(self):
        global fomular 
        fomular = "seventh"
        self.manager.current = "inputscreen"





class InputScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.calulate_btn = Button(text="Calculate")
        self.calulate_btn.on_press = self.calculate
        if fomular == "first":
            self.a_inp = TextInput(text ="Enter the number for A:", multiline=False)
            self.b_inp = TextInput(text ="Enter the number for B:", multiline=False)
            self.c_inp = TextInput(text ="Enter the number for C:", multiline=False)

        elif fomular == "second" or fomular == "third":
            self.a_inp = TextInput(text ="Enter the number for A:", multiline=False)
        
        else:
            self.a_inp = TextInput(text ="Enter the number for A:", multiline=False)
            self.b_inp = TextInput(text ="Enter the number for B:", multiline=False)
        

        layout_1 = BoxLayout(orientation="vertical", padding = 8 , spacing = 8)
        layout_1.add_widget(self.a_inp)

        try:
            layout_1.add_widget(self.b_inp)
        except:
            pass

        try:
            layout_1.add_widget(self.c_inp)
        except: 
            pass

        layout_1.add_widget(self.calulate_btn)
        self.add_widget(layout_1)

    def calculate(self):
        global a, b, c
        a = float(int(self.a_inp.text))

        try:
            b = float(int(self.b_inp.text))
        except:
            b = 0.0

        try:
            c = float(int(self.c_inp.text))
        except:
            c = 0.0

        self.manager.current = "calculate"


class CalculateScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        label_ans = Label(text = "The result for the question is:")
        ans = ""
        if fomular == "first":
            ans = solution1(a,b,c) 
        if fomular == "second":
            ans = solution2(a) 
        if fomular == "third":
            ans = solution3(a) 
        if fomular == "fourth":
            ans = solution4(a,b) 
        if fomular == "fifth":
            ans = solution5(a,b) 
        if fomular == "sixth":
            ans = solution6(a,b) 
        if fomular == "seventh":
            ans = solution7(a,b) 


        label_result = Label(text = ans)

        self.again_btn = Button(text = "Another calculation")
        self.again_btn.on_press = self.choose_fomula

        outer = BoxLayout(orientation="vertical", padding= 8, spacing = 8)
        outer.add_widget(label_ans)
        outer.add_widget(label_result)

        self.add_widget(outer)
    
    def choose_fomula(self):
        self.manager.current = "function"


class Application(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FunctionScreen(name = "function"))
        sm.add_widget(InputScreen(name = "inputscreen"))
        sm.add_widget(CalculateScreen(name = "calculate"))
        return sm
    
app = Application()
app.run()