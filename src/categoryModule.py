from itemModule import Item
import sys
import wx
from matplotlib import pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure
import numpy as np

class Category:

    def __init__(self,name,amount):

        try:

            if amount < 0.00 or type(name) is not str:

                return None

            self.name = name
            self.amount = amount
            self.itemList = []

        except:

            return None
    
    def addItem(self,itemObj):

        try:

            if type(itemObj) is not Item:

                return False

            self.itemList.append(itemObj)

            return True

        except:

            return None

    def deleteItemCompare(self,itemObj):

        try:

            for i in self.itemList:

                if i.compareItem(itemObj) == True:
                    self.itemList.remove(i)
                    return True

            return False

        except:

            return None

    def deleteItemPos(self,position):

        try:

            if(len(self.itemList)==0):
                return False

            self.itemList.pop(position)
            return True            
        except:
            return None

    def calculateRemainingAmount(self):

        expense = self.calculateExpenses()

        if expense == None:
            return None

        return (self.amount-expense)

    def calculateExpenses(self):

        expense = 0.00

        try:

            for i in self.itemList:
                expense = expense + i.getCost()

        except:

            return None
    
        return expense
    
    def writeCategory(self):

        writeString = "CATEGORY:BEGIN\r\nNAME:"+self.name+"\r\nAMOUNT:"+str(format(self.amount, '.2f'))+"\r\n"

        for i in self.itemList:
            writeString = writeString+i.writeItemString()
        writeString = writeString+"CATEGORY:END\r\n"

        return writeString

    def toJSON(self):
        
        itemJSON = {"name":self.name,"amount":self.amount}

    def updateName(self,name):
        
        try: 

            if type(name) is not str:

                return False

            self.name = name

            return True

        except:
            
            return None

    def getAmount(self):

        return self.amount

    #Need to test
    def validateCategory(self):
        try:

            if type(self.name) is not str:
                raise TypeError
            if len(self.name) < 1:
                raise TypeError
            if type(self.amount) is not float:
                raise TypeError
            if self.amount < 0:
                raise TypeError
            
            for i in self.itemList:

                if i.validateItem() != True:
                    raise TypeError

        except TypeError:
            return False

        except:
            return None

        return True

    def insertCategoryName(self,array):
        print("WIP")
        array.append(self.name)

    def insertCategoryCost(self,array):
        print("WIP")
        array.append(self.amount)

    #Below is all UI stuff, above is functionality. 
    def displayCategory(self,panelMaster):

        self.panel = wx.Panel(panelMaster)
        sizer = wx.GridBagSizer(5, 5)

        self.selectList = []

        self.addButton = wx.Button(self.panel, wx.ID_ANY, 'Add Item')
        self.deleteButton = wx.Button(self.panel, wx.ID_ANY, 'Delete Item')
        self.amountButton = wx.Button(self.panel, wx.ID_ANY, 'Change Amount')

        self.titleStatic = wx.StaticText(self.panel, wx.ID_ANY, self.name)
        self.spendingString = "Spending: $ "+ str(format(self.calculateExpenses(), '.2f'))
        self.remainString = "Remaining: $ "+ str(format(self.calculateRemainingAmount(), '.2f'))
        self.amountString = "Amount: $ "+ str(format(self.amount, '.2f'))
        self.remainStatic = wx.StaticText(self.panel, wx.ID_ANY, self.remainString)
        self.spendingStatic = wx.StaticText(self.panel, wx.ID_ANY, self.spendingString)
        self.amountStatic = wx.StaticText(self.panel, wx.ID_ANY, self.amountString) 

        self.itemListUI = wx.ListCtrl(self.panel, wx.ID_ANY,style = wx.LC_REPORT)
        self.itemListUI.InsertColumn(0, 'Name',width = 75)
        self.itemListUI.InsertColumn(1, 'Cost',width = 100) 
        index = 0

        for i in self.itemList:
            i.displayItem(self.itemListUI,index)
            index+=1

        sizer.Add(self.titleStatic,pos=(0, 2),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)
        sizer.Add(self.amountStatic,pos=(1, 0),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)
        sizer.Add(self.spendingStatic,pos=(1, 1),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)
        sizer.Add(self.remainStatic,pos=(1, 3),span=(1, 3),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)
        sizer.Add(self.itemListUI,pos=(2, 0),span=(4, 2),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)
        sizer.Add(self.amountButton,pos=(2, 3),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)
        sizer.Add(self.addButton,pos=(3, 3),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)
        sizer.Add(self.deleteButton,pos=(4, 3),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)

        self.addButton.Bind(wx.EVT_BUTTON,self.onAddClick)
        self.deleteButton.Bind(wx.EVT_BUTTON,self.onDeleteClick)
        self.amountButton.Bind(wx.EVT_BUTTON,self.onAmountClick)
        self.panel.SetSizerAndFit(sizer)

        return self.panel

    def compareCategory(self,tempCategory,itemCompareBool):
        try:

            if self.name != tempCategory.name:
                return False
            
            if self.amount != tempCategory.amount:
                return False

            if itemCompareBool == True:

                for i in self.itemList:

                    foundBool = False

                    for j in tempCategory.itemList:

                        if i.compareItem(j) == True:
                            foundBool == True
                            break

                    if foundBool == False:
                        return False

            return True

        except:
            return None

    def insertListCtrl(self,uiList,index):
        uiList.InsertItem(index, self.name) 
        uiList.SetItem(index, 1, "$ "+str(format(self.amount, '.2f'))) 
        uiList.SetItem(index, 2, "$ "+str(format(self.calculateExpenses(), '.2f')))
        uiList.SetItem(index, 3, "$ "+str(format(self.calculateRemainingAmount(), '.2f')))

    def onAddClick(self,event):

        self.itemDialog = wx.Dialog(self.panel,title = 'Add Item')
        dialogPanel = wx.Panel(self.itemDialog)
        sizer = wx.GridBagSizer(10, 10)
        itemNameStatic = wx.StaticText(dialogPanel, wx.ID_ANY, "Name: ") 
        self.itemNameInput = wx.TextCtrl(dialogPanel) 

        itemCostStatic = wx.StaticText(dialogPanel, wx.ID_ANY, "Cost: ") 
        self.itemCostInput = wx.TextCtrl(dialogPanel)
        addButton = wx.Button(dialogPanel, wx.ID_ANY, 'Add Item')

        addButton.Bind(wx.EVT_BUTTON,self.onDialogAddClick)

        sizer.Add(itemNameStatic,pos=(1, 1),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)
        sizer.Add(self.itemNameInput,pos=(1, 2),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)

        sizer.Add(itemCostStatic,pos=(2, 1),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)
        sizer.Add(self.itemCostInput,pos=(2, 2),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)
        
        sizer.Add(addButton,pos=(1, 3),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)

        dialogPanel.SetSizerAndFit(sizer)

        self.itemDialog.ShowModal()

    def onDialogAddClick(self,event):
        name = self.itemNameInput.GetValue()
        cost = self.itemCostInput.GetValue()
        tempItem = Item(name,float(cost))
        index = len(self.itemList)
        tempItem.displayItem(self.itemListUI,index)
        self.itemList.append(tempItem)
        self.updateRemainingUI()
        self.updateSpendingUI()
        self.itemDialog.Destroy()

    def onDeleteClick(self,event):

        #This is to delete if person selects the item to delete
        selectDeleteBool = False
        deleteListId = []
        length = len(self.itemList)
        print("Start:")
        for i in range(length):
            tempListCtrlItem = self.itemListUI.GetItem(i)
            print(i,":",tempListCtrlItem.GetState())
            #4 and 6 are some hardcoded values in the model. I tried using keywords but it didn't work.
            if tempListCtrlItem.GetState() == 4 or tempListCtrlItem.GetState() == 6:
                selectDeleteBool = True
                deleteListId.insert(0,tempListCtrlItem.GetId())
        #True means something is selected, to delete
        if selectDeleteBool == True:

            for i in deleteListId:
                print(i)
                self.itemListUI.DeleteItem(i)
                self.itemList.pop(i)
            wx.MessageBox('Successfully deleted item(s).', 'Success', wx.OK | wx.ICON_NONE)
            self.updateRemainingUI()
            self.updateSpendingUI()
            return
        #Otherwise prompt for box to delete.
        self.itemDialog = wx.Dialog(self.panel,title = 'Delete Item')
        dialogPanel = wx.Panel(self.itemDialog)
        sizer = wx.GridBagSizer(10, 10)
        itemNameStatic = wx.StaticText(dialogPanel, wx.ID_ANY, "Name: ") 
        self.itemNameInput = wx.TextCtrl(dialogPanel) 

        itemCostStatic = wx.StaticText(dialogPanel, wx.ID_ANY, "Cost: ") 
        self.itemCostInput = wx.TextCtrl(dialogPanel)
        addButton = wx.Button(dialogPanel, wx.ID_ANY, 'Delete Item')

        addButton.Bind(wx.EVT_BUTTON,self.onDialogDeleteClick)

        sizer.Add(itemNameStatic,pos=(1, 1),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)
        sizer.Add(self.itemNameInput,pos=(1, 2),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)

        sizer.Add(itemCostStatic,pos=(2, 1),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)
        sizer.Add(self.itemCostInput,pos=(2, 2),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)
        
        sizer.Add(addButton,pos=(1, 3),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)

        dialogPanel.SetSizerAndFit(sizer)

        self.itemDialog.ShowModal()
  
    def onDialogDeleteClick(self,event):
        name = self.itemNameInput.GetValue()
        cost = self.itemCostInput.GetValue()
        tempItem = Item(name,float(cost))

        try:
            index = 0
            deleteBool = False
            for i in self.itemList:
                if i.compareItem(tempItem) == True:
                    self.itemList.pop(index)
                    deleteBool = True
                    self.itemListUI.DeleteItem(index)
                    break
                index += 1

            if deleteBool == False:

                wx.MessageBox('Could not find item to delete.', 'Error', wx.OK | wx.ICON_ERROR)

            else:

                wx.MessageBox('Successfully deleted item.', 'Success', wx.OK | wx.ICON_NONE)

        except:
            wx.MessageBox('Error while trying to delete.', 'Error', wx.OK | wx.ICON_ERROR)

        self.itemDialog.Destroy()  

    def updateRemainingUI(self):
        self.remainString = "Remaining: $ "+ str(format(self.calculateRemainingAmount(), '.2f'))
        self.remainStatic.SetLabel(self.remainString)
        self.panel.Update()

    def updateSpendingUI(self):
        self.spendingString = "Spending: $ "+ str(format(self.calculateExpenses(), '.2f'))
        self.spendingStatic.SetLabel(self.spendingString)
        self.panel.Update()

    def updateAmountUI(self,event):
        #getString = self.amountDisplay.GetValue()
        #self.amount = format(float(getString),'.2f')
        self.updateRemainingUI()
        self.updateSpendingUI()

    def onAmountClick(self,event):
        self.amountDialog = wx.Dialog(None,title = 'Change Amount')
        dialogPanel = wx.Panel(self.amountDialog)
        sizer = wx.GridBagSizer(10, 10)
        amountStatic = wx.StaticText(dialogPanel, wx.ID_ANY, "Amount: $") 
        self.amountInput = wx.TextCtrl(dialogPanel) 

        changeButton = wx.Button(dialogPanel, wx.ID_ANY, 'Change')

        changeButton.Bind(wx.EVT_BUTTON,self.onDialogChangeClick)

        sizer.Add(amountStatic,pos=(1, 1),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)
        sizer.Add(self.amountInput,pos=(1, 2),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)
        
        sizer.Add(changeButton,pos=(1, 3),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)

        dialogPanel.SetSizerAndFit(sizer)

        self.amountDialog.ShowModal()
        
    def onDialogChangeClick(self,event):

        getString = self.amountInput.GetValue()
        self.amount = float(getString)
        self.amountStatic.SetLabel("Amount: $ "+ str(format(self.amount,'.2f')))
        self.updateSpendingUI()
        self.updateRemainingUI()
        self.amountDialog.Destroy()

    def createGraph(self,figure,graphType):
        
        ax = figure.add_axes([0,0,1,1])
        ax.set_title(self.name)
        itemNameArray = []
        itemCostArray = []
        for i in self.itemList:

            for k in itemNameArray:
                #Checks for dups, like 2 or 3 coffees in the list.
                if i.compareItemName(k) == True:

                    itemCostArray[itemNameArray.index(k)] += i.getCost()
                    continue

            i.insertListName(itemNameArray)
            i.insertListCost(itemCostArray)

        if graphType == "bar":
            ax.bar(itemNameArray,itemCostArray)
        if graphType == "pie":
            ax.axis('equal')
            ax.pie(itemCostArray, labels = itemNameArray,autopct='%1.2f%%')

        return ax

    def displayGraph(self,panel,graphType):
        figure = plt.figure()
        axis = self.createGraph(figure,graphType)
        canvas = FigureCanvas(panel, wx.ID_ANY, figure)

        #bar graph is too big. Shrinking it here.
        if graphType == "bar":
            canvas.SetSize(500,500)

        canvas.Hide()
        return canvas

#Test for item not in the lists for the deletes.