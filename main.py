from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivy.lang import Builder
from kivymd.uix.list import TwoLineListItem
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivymd.uix.menu import MDDropdownMenu
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
import requests
help_str = '''
ScreenManager:
    WelcomeScreen:
    MainScreen:
    LoginScreen:
    SignupScreen:
<WelcomeScreen>:
    name:'welcomescreen'
    MDLabel:
        text:'Login'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.9}
    MDLabel:
        text:'&'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.7}
    MDLabel:
        text:'Signup'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.5}
    MDRaisedButton:
        text:'Login'
        pos_hint : {'center_x':0.4,'center_y':0.3}
        size_hint: (0.13,0.1)
        on_press: 
            root.manager.current = 'loginscreen'
            root.manager.transition.direction = 'left'
    MDRaisedButton:
        text:'Signup'
        pos_hint : {'center_x':0.6,'center_y':0.3}
        size_hint: (0.13,0.1)
        on_press:
            root.manager.current = 'signupscreen'
            root.manager.transition.direction = 'left'
        
<LoginScreen>:
    name:'loginscreen'
    MDLabel:
        text:'Login'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.9}
    MDTextField:
        
        id:login_UserID
        pos_hint: {'center_y':0.6,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'UserID'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDTextField:
        id:login_password
        pos_hint: {'center_y':0.4,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Password'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDRaisedButton:
        text:'Login'
        size_hint: (0.13,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press:
            app.login()
            
            
        
    MDTextButton:
        text: 'Create an account'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.current = 'signupscreen'
            root.manager.transition.direction = 'up'
<SignupScreen>:
    name:'signupscreen'
    MDLabel:
        text:'Signup'
        font_style:'H2'
        halign:'center'
        pos_hint: {'center_y':0.9}
    MDTextField:
        id:signup_UserID
        pos_hint: {'center_y':0.6,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'UserID'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDTextField:
        id:signup_Name
        pos_hint: {'center_y':0.75,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Name'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
    MDTextField:
        id:signup_password
        pos_hint: {'center_y':0.4,'center_x':0.5}
        size_hint : (0.7,0.1)
        hint_text: 'Password'
        helper_text:'Required'
        helper_text_mode:  'on_error'
        icon_right: 'account'
        icon_right_color: app.theme_cls.primary_color
        required: True
        mode: "rectangle"
    MDRaisedButton:
        text:'Signup'
        size_hint: (0.13,0.07)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: app.signup()
    MDTextButton:
        text: 'Already have an account'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press:
            root.manager.current = 'loginscreen'
            root.manager.transition.direction = 'down'
    
    
<MainScreen>:
    name: 'mainscreen'
	#:import CustomOverFlowMenu __main__.CustomOverFlowMenu
	MDBoxLayout:
    	orientation: "vertical"
    	padding:20
    	MDTopAppBar:
        	title: "RChat by Rajeev..."
        	use_overflow: True
        	overflow_cls: CustomOverFlowMenu()
		MDBoxLayout:
			orientation:'vertical'
			md_bg_color:0.9,0.9,0.9,1
			padding:19
			MDScrollView:
				MDList:
					id:ram
					spacing:'60dp'
		MDBoxLayout:
			size_hint_x:1
			size_hint_y:0.30
			md_bg_color:'teal'
			padding:19
    		MDTextField:
        		id: text_field_error
				max_text_length: 35
        		hint_text: "Enter a message ..."
        		helper_text: "Max Length 35"
        		helper_text_mode: "on_error"
        		pos_hint: {'bottom':1, 'left':.1}
       	 	mode:'fill'
        		multiline:True
       	 	size_hint:1, 0.5
   	     MDIconButton:
 	       	icon:'send-circle'
        		icon_size:'55sp'
        		on_release:
        			app.chatHis()
'''

class CustomOverFlowMenu(MDDropdownMenu):
    pass
class WelcomeScreen(Screen):
    pass
class MainScreen(Screen):
    pass
class LoginScreen(Screen):
    pass
class SignupScreen(Screen):
    pass
sm = ScreenManager()
sm.add_widget(WelcomeScreen(name = 'loginscreen'))
sm.add_widget(MainScreen(name = 'mainscreen'))
sm.add_widget(LoginScreen(name = 'loginscreen'))
sm.add_widget(SignupScreen(name = 'signupscreen'))


class LoginApp(MDApp):
    def build(self):
        self.strng = Builder.load_string(help_str)
        self.url  = "https://rchat-again-default-rtdb.firebaseio.com/.json"
        return self.strng

    def signup(self):
        signupUserID = self.strng.get_screen('signupscreen').ids.signup_UserID.text
        signupPassword = self.strng.get_screen('signupscreen').ids.signup_password.text
        signupName = self.strng.get_screen('signupscreen').ids.signup_Name.text
        if signupUserID.split() == [] or signupPassword.split() == [] or signupName.split() == []:
            cancel_btn_Name_dialogue = MDFlatButton(text = 'Retry',on_release = self.close_Name_dialog)
            self.dialog = MDDialog(title = 'Invalid Input',text = 'Please Enter a valid Input',size_hint = (0.7,0.2),buttons = [cancel_btn_Name_dialogue])
            self.dialog.open()
        if len(signupName.split())>1:
            cancel_btn_Name_dialogue = MDFlatButton(text = 'Retry',on_release = self.close_Name_dialog)
            self.dialog = MDDialog(title = 'Invalid Name',text = 'Please enter Name without space',size_hint = (0.7,0.2),buttons = [cancel_btn_Name_dialogue])
            self.dialog.open()
        else:
            print(signupUserID,signupPassword)
            signup_info = str({f'\"{signupUserID}\":{{"Password":\"{signupPassword}\","Name":\"{signupName}\"}}'})
            signup_info = signup_info.replace(".","-")
            signup_info = signup_info.replace("\'","")
            to_database = json.loads(signup_info)
            print((to_database))
            requests.patch(url = self.url,json = to_database)
            self.strng.get_screen('loginscreen').manager.current = 'loginscreen'
    auth = 'R5w2371nl1Z7J45KIkf4MWeD0QURcljdgujcxoHz'

    def login(self):
        self.loginUserID = self.strng.get_screen('loginscreen').ids.login_UserID.text
        loginPassword = self.strng.get_screen('loginscreen').ids.login_password.text

        self.login_check = False
        supported_loginUserID = self.loginUserID.replace('.','-')
        supported_loginPassword = loginPassword.replace('.','-')
        request  = requests.get(self.url+'?auth='+self.auth)
        data = request.json()
        UserIDs= set()
        for key,self.value in data.items():
            UserIDs.add(key)
        if supported_loginUserID in UserIDs and supported_loginPassword == data[supported_loginUserID]['Password']:
            self.Name = data[supported_loginUserID]['Name']
            self.login_check=True
            self.strng.get_screen('mainscreen').manager.current = 'mainscreen'
        else:
            print("user no longer exists")
        if self.strng.get_screen('mainscreen').manager.current == 'mainscreen':
        	Window.softinput_mode = 'pan'
    def close_Name_dialog(self,obj):
        self.dialog.dismiss()

    def chatHis (self):
    	if self.strng.get_screen('mainscreen').ids.text_field_error !="":
    		self.value=self.strng.get_screen('mainscreen').ids.text_field_error.text
    		po=MDBoxLayout(md_bg_color=(0,0,0,1), orientation='vertical',size_hint_y=0.03,size_hint_x=.005,pos_hint={'x':0.5,'y':.5},id='x',padding=16)
    		po.add_widget(MDLabel(text=f'[{self.loginUserID}]:: {self.value}', font_style='H6',pos_hint={'y':1}))

    		self.strng.get_screen('mainscreen').ids.ram.add_widget(po)
    		self.strng.get_screen('mainscreen').ids.text_field_error.text=''
    		
LoginApp().run()
