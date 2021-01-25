from budgetModule import Budget
from categoryModule import Category
from itemModule import Item
import wx
import wx.grid as gridlib

class LoginPage(wx.Dialog):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        sizer = wx.GridBagSizer(10, 10)

        self.loginButton = wx.Button(self, wx.ID_ANY, 'Login')
        self.skipButton = wx.Button(self, wx.ID_ANY, 'Skip')

        self.usernameStatic = wx.StaticText(self, wx.ID_ANY, "Username: ") 
        self.passwordStatic = wx.StaticText(self, wx.ID_ANY, "Password: ") 
        self.userNameInput = wx.TextCtrl(self) 
        
        self.passwordInput = wx.TextCtrl(self,style = wx.TE_PASSWORD) 
        self.welcomeStatic = wx.StaticText(self, wx.ID_ANY, "Welcome to Budget Buddy! Please login: ") 

        self.skipButton.Bind(wx.EVT_BUTTON,self.SkipPressed)
        self.loginButton.Bind(wx.EVT_BUTTON,self.Login)

        sizer.Add(self.welcomeStatic,pos=(1, 0),span=(1, 3),flag = wx.ALL, border = 5)
        sizer.Add(self.usernameStatic,pos=(2, 0),span=(1, 1),flag = wx.ALL, border = 5)
        sizer.Add(self.userNameInput,pos=(2, 1),span=(1, 2),flag = wx.ALL, border = 5)
        sizer.Add(self.passwordStatic,pos=(3, 0),span=(1, 1),flag = wx.ALL, border = 5)
        sizer.Add(self.passwordInput,pos=(3, 1),span=(1, 2),flag = wx.ALL, border = 5)
        sizer.Add(self.loginButton,pos=(5, 1),span=(1, 1),flag = wx.ALL, border = 5)
        sizer.Add(self.skipButton ,pos=(5, 3),span=(1, 1),flag = wx.ALL, border = 5)

        self.SetSizerAndFit(sizer)

    def SkipPressed(self,event):
        self.Destroy()

    def Login(self,event):

        password = self.passwordInput.GetValue()
        userName = self.userNameInput.GetValue()
        
        print(password)
        print(userName)
        self.Destroy()
