
from budgetModule import Budget
from categoryModule import Category
from itemModule import Item
from homeScreen import HomePage
from loginScreen import LoginPage
import os
import wx
import wx.grid as gridlib

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY,"Budget Buddy")

        loginPanel = LoginPage(self)
        loginPanel.ShowModal()

        self.SetSize((1200,1200))
        homePanel = HomePage(self)
        homePanel.Show()
        
app = wx.App()
frame = MyFrame()
frame.Show()
app.MainLoop()