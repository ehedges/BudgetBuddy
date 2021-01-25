from categoryModule import Category
import wx
import re
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure
import numpy as np

class Budget:

    def __init__(self,name,amount,occurBool,dateInput):

        self.name = None
        self.amount = None
        self.date = None
        self.reoccur = None
        self.categoryArray = []
        try:
            
            if type(name) is not str or amount < 0.00 or type(occurBool) is not bool or type(dateInput) is not str:
                
                return None

            try:

                validDate = self.checkDate(dateInput)

                if validDate != True:
                    return None

            except: 
                return None

            if len(name) < 1:
                return None

            self.name = name
            self.amount = amount
            self.date = dateInput
            self.reoccur = occurBool
            self.categoryArray = []

            self.currentPanel = None
            self.currentGraph = None

        except:
            self = None

    def addCategory(self,insertCategory):

        try:

            if type(insertCategory) is not Category:
                return False

            self.categoryArray.append(insertCategory)

            return True

        except:
            None

    def writeBudget(self,fileName):

        fileString = "BUDGET:BEGIN\r\nNAME:" + self.name +"\r\nAMOUNT:" + str(format(self.amount, '.2f')) +"\r\n"

        if self.reoccur == False:

            fileString = fileString + "REOCCOURING:FALSE\r\n"

        else:

            fileString = fileString + "REOCCOURING:TRUE\r\n"

        fileString = fileString + "DATE:" 

        invalidBool = False

        try:

            if len(self.date) != 7:
                invalidBool = True

        except:

            invalidBool = False
        
        if invalidBool == True:

            fileString = fileString + datetime.today().strftime('%Y-%m') + "\r\n"

        else:

            fileString = fileString + self.date + "\r\n"

        for i in self.categoryArray:
            fileString = fileString + i.writeCategory()

        fileString = fileString + "BUDGET:END\r\n"

        f = open(fileName, "w")

        f.write(fileString)

    def updateBudgetName(self, newName):

        try:

            if type(newName) is not str:
                return False

            if len(newName) < 1:
                return False

            self.name = newName
            return True

        except:
            return None

    def updateAmount(self, newAmount):

        try:

            if  newAmount < 0:
                return False

            self.amount = newAmount

            return True

        except:
            return None

    def updateOccur(self,updateBool):

        try:

            if type(updateBool) is not bool:
                return False

            self.reoccur = updateBool

            return True

        except:
            return None

    def checkAmount(self):

        totalAmount = 0

        if self.amount == None:
            return None

        for i in self.categoryArray:

            totalAmount += i.getAmount()

        if totalAmount == self.amount:

            return True

        else:
            return False

    def totalRemaining(self):

        if self.amount == None:
            return None

        spending = self.totalSpending()

        if spending == None:
            return None

        return (self.amount-spending)

    def totalSpending(self):

        try:

            spendTotal = 0.00

            #Loop through each category, calculating expenses

            for i in self.categoryArray:

                spendAmount = i.calculateExpenses()

                if spendAmount == None:
                    return None

                spendTotal = spendTotal + spendAmount

            return (spendTotal)
        
        except:

            return None

    def findCategory(self,toFind):
        
        for i in self.categoryArray:

            if i.compareCategory(toFind) == True:
                return i

        return None

    
    def validateBudget(self):

        try:

            if type(self.name) is not str or self.amount < 0.00 or type(self.occurBool) is not bool or type(self.dateInput) is not str:
                
                return False

            try:

                datetime.datetime.strptime(dateInput,"%Y-%m")

            except:

                try:

                    datetime.datetime.strptime(dateInput,"%m-%Y")

                except:
                    return False

            for i in self.categoryArray:
                
                if i.validateCategory() != True:
                    return False

            return True

        except:

            return None

    def toJSON(self):
        print("WIP")

    def checkYearOrDay(self,string):

        if len(string) == 2:
                
            if int(string) > 12 or int(string) < 1:
                return False

        elif len(string) == 4:

            if int(string) < 1950 or int(string) > 2100:
                return False

        else:

            return False

        
        return True
    
    def checkDate(self,dateInput):

        if len(dateInput) != 7:
            return False

        dateSplit = dateInput.split("-")
        prefix = dateSplit[0]
        ending = dateSplit[1]

        if self.checkYearOrDay(prefix) != True or self.checkYearOrDay(ending) != True:

            return False

        return True


    # Everything below is UI stuff. It is a mess.

    def displayBudget(self,panel,sizer):

        #categoryDisplayPanel is so that the position of summary and the Category panels are in the correct position.
        #You can't place multiplepanels in the same location in a sizer. So we place a panel in that location.
        #Then add another panel which is the actual category with items.
        #We swap between these panels to show the multiple category panels. 
        #Panel Array holds all the category panels to swap between.
        self.categoryDisplayPanel = wx.Panel(panel)
        #ListUIPanel has the list of all the categories. It's the thing to the left. 
        self.listUIPanel = wx.Panel(panel)
        
        listUISizer = wx.GridBagSizer(5, 5)

        self.currentPanel = self.displaySummary(self.categoryDisplayPanel)
        self.currentPanel.Show()

        self.panelArray = []
        self.panelArray.append(self.currentPanel)
        #The list on the left that holds the different name and costs of the categories. 
        self.categoryListUI = self.createCategoryUIList(self.listUIPanel,listUISizer,self.categoryDisplayPanel)

        #Creates arrays with the types of graphs.

        titleString = self.name+": "+self.date
        titleStatic = wx.StaticText(self.listUIPanel, wx.ID_ANY, titleString)
        listUISizer.Add(titleStatic,pos=(0, 0),span=(1, 1),flag = wx.ALIGN_CENTER, border = 5)
        self.listUIPanel.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClickSwitch, self.categoryListUI)

        self.listUIPanel.SetSizerAndFit(listUISizer)

        sizer.Add(self.categoryDisplayPanel,pos=(1, 1),span=(4, 4),flag = wx.EXPAND|wx.ALL|wx.ALIGN_LEFT, border = 5)
        sizer.Add(self.listUIPanel,pos=(1, 0),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT|wx.ALIGN_BOTTOM, border = 5)

        panel.SetSizerAndFit(sizer)

    #This allows you to switch between the different panels to display the categories.
    def OnClickSwitch(self,event):

        if self.currentPanel != None:
            self.currentPanel.Hide()
        self.currentPanel = self.panelArray[event.GetIndex()]

        if event.GetIndex() == 0:
            self.updateSummaryPanel()

        if self.currentPanel is None:

            wx.MessageBox('Could not display Category.', 'Error', wx.OK | wx.ICON_ERROR)

        else:
            self.currentPanel.Show()

    #This generates the panel that displays the summary
    def displaySummary(self,parent):

        panel =  wx.Panel(parent)

        sizer = wx.GridBagSizer(5, 5)
        remainString = "Remaining: $ "+str(format(self.totalRemaining(),'.2f'))
        spendingString = "Expenses: $ "+str(format(self.totalSpending(),'.2f'))
        self.spendingStatic = wx.StaticText(panel, wx.ID_ANY, spendingString)
        nameString = "Summary"
        titleStatic = wx.StaticText(panel, wx.ID_ANY, nameString)
        self.remainStatic = wx.StaticText(panel, wx.ID_ANY, remainString)
        self.amountStatic = wx.StaticText(panel, wx.ID_ANY, "Amount: $ " + str(format(self.amount,'.2f')))

        amountButton = wx.Button(panel, wx.ID_ANY, 'Change Amount')
        amountButton.Bind(wx.EVT_BUTTON,self.updateAmountDialog)
        addCategoryButton = wx.Button(panel, wx.ID_ANY, 'Add Category')
        deleteCategoryButton = wx.Button(panel, wx.ID_ANY, 'Delete Category')
        sizer.Add(titleStatic,pos=(0, 2),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)
        sizer.Add(self.amountStatic,pos=(1, 0),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)
        sizer.Add(self.spendingStatic,pos=(1, 2),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)
        sizer.Add(self.remainStatic,pos=(1, 5),span=(1, 3),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)
        sizer.Add(amountButton,pos=(2, 5),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)
        sizer.Add(addCategoryButton,pos=(3, 5),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)
        sizer.Add(deleteCategoryButton,pos=(4, 5),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)

        addCategoryButton.Bind(wx.EVT_BUTTON,self.onClickAddCategory)
        deleteCategoryButton.Bind(wx.EVT_BUTTON,self.onClickDeleteCategory)

        self.summaryCategoryUIList = wx.ListCtrl(panel, wx.ID_ANY,style = wx.LC_REPORT) 
        self.summaryCategoryUIList.InsertColumn(0, 'Name',width = 75)
        self.summaryCategoryUIList.InsertColumn(1, 'Amount',width = 75)
        self.summaryCategoryUIList.InsertColumn(2, 'Expense',width = 75)
        self.summaryCategoryUIList.InsertColumn(3, 'Remaining',width = 75)

        sizer.Add(self.summaryCategoryUIList,pos=(2, 0),span=(4, 4),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)

        index = 0

        for i in self.categoryArray:

            i.insertListCtrl(self.summaryCategoryUIList,index)

            index += 1

        panel.SetSizerAndFit(sizer)
        
        panel.Show()

        return panel

    #Creates the list that has the summary and the categories. This is what you click to switch the panels.
    def createCategoryUIList(self,listUIPanel,listUISizer,categoryDisplayPanel):

        index = 0
        self.tempUIList = wx.ListCtrl(listUIPanel, wx.ID_ANY,style = wx.LC_REPORT) 

        listUISizer.Add(self.tempUIList,pos=(1, 0),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT|wx.ALIGN_BOTTOM, border = 5)

        self.tempUIList.InsertColumn(0, 'Name',width = 75)
        self.tempUIList.InsertColumn(1, 'Amount',width = 100)        
        self.tempUIList.InsertColumn(2, 'Spending',width = 100)  
        self.tempUIList.InsertColumn(3, 'Remaining',width = 100)
        self.insertListCtrlSummary(self.tempUIList,index)

        index += 1

        for i in self.categoryArray:

            i.insertListCtrl(self.tempUIList,index)
            
            tempPanel = i.displayCategory(self.categoryDisplayPanel)
            tempPanel.Hide()
            self.panelArray.append(tempPanel)
            index += 1

    #This adds the summary to the list thing on the left.
    def insertListCtrlSummary(self,uiList,index):
        uiList.InsertItem(index, "Summary")
        uiList.SetItem(index, 1, "$ "+str(format(self.amount, '.2f')))
        uiList.SetItem(index, 2, "$ "+str(format(self.totalSpending(), '.2f')))
        uiList.SetItem(index, 3, "$ "+str(format(self.totalRemaining(), '.2f') ))

    #Updates the summary when the information in a category changes.
    def updateSummaryPanel(self):

        self.summaryCategoryUIList.DeleteAllItems()

        index = 0

        self.updateExpensesUI()
        self.updateRemainingUI()

        for i in self.categoryArray:

            i.insertListCtrl(self.summaryCategoryUIList,index)
            
            index += 1

    #Creates dialog box that allows the user to change an amount.

    def updateAmountDialog(self,event):
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

    #Event handler for the dialog box button mentioned before. 
    def onDialogChangeClick(self,event):

        getString = self.amountInput.GetValue()
        self.amount = float(getString)
        self.amountStatic.SetLabel("Amount: $ "+ str(format(self.amount,'.2f')))
        self.updateExpensesUI()
        self.updateRemainingUI()
        self.amountDialog.Destroy()

    def updateExpensesUI(self):
        spendingString = "Expenses: $ "+str(format(self.totalSpending(),'.2f'))
        self.spendingStatic.SetLabel(spendingString)

    def updateRemainingUI(self):
        remainString = "Remaining: $ "+str(format(self.totalRemaining(),'.2f'))
        self.remainStatic.SetLabel(remainString)


    def onClickAddCategory(self,event):
        self.categoryDialog = wx.Dialog(None,title = 'Add Category')
        dialogPanel = wx.Panel(self.categoryDialog)
        sizer = wx.GridBagSizer(10, 10)
        categoryNameStatic = wx.StaticText(dialogPanel, wx.ID_ANY, "Name: ") 
        self.categoryNameInput = wx.TextCtrl(dialogPanel) 

        categoryAmountStatic = wx.StaticText(dialogPanel, wx.ID_ANY, "Amount: ") 
        self.categoryAmountInput = wx.TextCtrl(dialogPanel)
        addButton = wx.Button(dialogPanel, wx.ID_ANY, 'Add Category')

        addButton.Bind(wx.EVT_BUTTON,self.onDialogAddClick)

        sizer.Add(categoryNameStatic,pos=(1, 1),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)
        sizer.Add(self.categoryNameInput,pos=(1, 2),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)

        sizer.Add(categoryAmountStatic,pos=(2, 1),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)
        sizer.Add(self.categoryAmountInput,pos=(2, 2),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)
        
        sizer.Add(addButton,pos=(1, 3),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)

        dialogPanel.SetSizerAndFit(sizer)

        self.categoryDialog.ShowModal()

    def onDialogAddClick(self,event):
        name = self.categoryNameInput.GetValue()
        amount = float(self.categoryAmountInput.GetValue())
        tempCategory = Category(name,amount)
        self.categoryArray.append(tempCategory)
        tempCategory.insertListCtrl(self.tempUIList,len(self.categoryArray))
        tempCategory.insertListCtrl(self.summaryCategoryUIList,(len(self.categoryArray)-1))
        tempPanel = tempCategory.displayCategory(self.categoryDisplayPanel)
        tempPanel.Hide()
        self.panelArray.append(tempPanel)
        self.categoryDialog.Destroy()

    def onClickDeleteCategory(self,event):
        #This is to delete if person selects the category to delete
        selectDeleteBool = False
        deleteListId = []
        length = len(self.categoryArray)
        for i in range(length):
            tempListCtrlCategory = self.summaryCategoryUIList.GetItem(i)
            #4 and 6 are some hardcoded values in the model. I tried using keywords but it didn't work.
            if tempListCtrlCategory.GetState() == 4 or tempListCtrlCategory.GetState() == 6:
                selectDeleteBool = True
                deleteListId.insert(0,tempListCtrlCategory.GetId())
        #True means something is selected, to delete                
        if selectDeleteBool == True:

            for i in deleteListId:
                self.summaryCategoryUIList.DeleteItem(i)
                self.tempUIList.DeleteItem(i+1)
                self.categoryArray.pop(i)

            wx.MessageBox('Successfully deleted category.', 'Success', wx.OK | wx.ICON_NONE)
            self.updateExpensesUI()
            self.updateRemainingUI()
            return

        self.categoryDialog = wx.Dialog(None,title = 'Delete Category')
        dialogPanel = wx.Panel(self.categoryDialog)
        sizer = wx.GridBagSizer(10, 10)
        categoryNameStatic = wx.StaticText(dialogPanel, wx.ID_ANY, "Name: ") 
        self.categoryNameInput = wx.TextCtrl(dialogPanel) 

        categoryAmountStatic = wx.StaticText(dialogPanel, wx.ID_ANY, "Amount: ") 
        self.categoryAmountInput = wx.TextCtrl(dialogPanel)
        addButton = wx.Button(dialogPanel, wx.ID_ANY, 'Delete Category')

        addButton.Bind(wx.EVT_BUTTON,self.onDialogDeleteClick)

        sizer.Add(categoryNameStatic,pos=(1, 1),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)
        sizer.Add(self.categoryNameInput,pos=(1, 2),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)

        sizer.Add(categoryAmountStatic,pos=(2, 1),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)
        sizer.Add(self.categoryAmountInput,pos=(2, 2),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)
        
        sizer.Add(addButton,pos=(1, 3),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)

        dialogPanel.SetSizerAndFit(sizer)

        self.categoryDialog.ShowModal()
       
    def onDialogDeleteClick(self,event):
        name = self.categoryNameInput.GetValue()
        cost = self.categoryAmountInput.GetValue()
        tempCategory = Category(name,float(cost))

        try:
            index = 0
            deleteBool = False
            for i in self.categoryArray:
                if i.compareCategory(tempCategory,False) == True:
                    self.categoryArray.pop(index)
                    deleteBool = True
                    self.summaryCategoryUIList.DeleteItem(index)
                    break
                index += 1

            if deleteBool == False:

                wx.MessageBox('Could not find category to delete.', 'Error', wx.OK | wx.ICON_ERROR)

            else:

                wx.MessageBox('Successfully deleted category.', 'Success', wx.OK | wx.ICON_NONE)

        except:
            wx.MessageBox('Error while trying to delete.', 'Error', wx.OK | wx.ICON_ERROR)

        self.categoryDialog.Destroy()  
    #Poorly named, this switches graph to categories.    
    def swapFromGraphToCategory(self):
        print("WIP")
        #ensures nothing is left over if you switch back. If you generate graphs and don't delete the program will chug
        if self.currentGraph != None:
            for i in self.graphArrayBar:
                i.Destroy()

            for i in self.graphArrayPie:
                i.Destroy()

            self.currentGraph = None
            self.swapGraphTypeButton.Destroy()
            print("Deleted")
            
        self.listUIPanel.Unbind(wx.EVT_LIST_ITEM_ACTIVATED)
        self.listUIPanel.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClickSwitch, self.categoryListUI)

        self.currentPanel.Show()

    def swapFromCategoryToGraph(self):
        print("WIP")
        self.listUIPanel.Unbind(wx.EVT_LIST_ITEM_ACTIVATED)
        self.listUIPanel.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClickSwitchGraphs, self.categoryListUI)

        self.createGraphs()

        self.currentPanel.Hide()
        #Graphtype true means pie, graphtype false = bar
        #Should alawys have a 0. 0 is the summary graph.
        if self.graphType == True:
             self.currentGraph = self.graphArrayPie[0]
        else:
            self.currentGraph = self.graphArrayBar[0]

        self.currentGraph.Show()


    def createGraphs(self):

        self.graphArrayBar = []
        self.graphArrayPie = []

        self.swapGraphTypeButton = wx.Button(self.categoryDisplayPanel, wx.ID_ANY, 'Display Bar Graphs')
        self.swapGraphTypeButton.Bind(wx.EVT_BUTTON,self.swapGraphTypes)

        if self.currentGraph != None:
            self.currentGraph.Destroy()

        self.currentGraph = None
        #Graphtype true means pie, graphtype false = bar
        self.graphType = True

        #Send in the panel here

        self.graphArrayBar.append(self.displaySummaryGraph(self.categoryDisplayPanel,"bar"))
        self.graphArrayPie.append(self.displaySummaryGraph(self.categoryDisplayPanel,"pie"))

        for i in self.categoryArray:
            self.graphArrayBar.append(i.displayGraph(self.categoryDisplayPanel,"bar"))
            self.graphArrayPie.append(i.displayGraph(self.categoryDisplayPanel,"pie"))

    def OnClickTypeGraphs(self,event):
        print("WIP")
        #This means display pie

        self.currentGraph.Hide()

        currentIndex = event.GetIndex()

        if self.graphType == True:
             self.currentGraph = self.graphArrayPie[currentIndex]
        else:
            self.currentGraph = self.graphArrayBar[currentIndex]

        self.currentGraph.Show()

    def OnClickSwitchGraphs(self,event):

        self.currentGraph.Hide()

        currentIndex = event.GetIndex()

        if self.graphType == True:
            self.currentGraph = self.graphArrayPie[currentIndex]
        else:
            self.currentGraph = self.graphArrayBar[currentIndex]

        self.currentGraph.Show()

    def createSummaryGraph(self,figure,graphType):
        
        ax = figure.add_axes([0,0,1,1])
        ax.set_title(self.name + " Summary")
        itemNameArray = []
        itemCostArray = []
        for i in self.categoryArray:

            i.insertCategoryName(itemNameArray)
            i.insertCategoryCost(itemCostArray)

        if graphType == "bar":
            ax.bar(itemNameArray,itemCostArray)
        if graphType == "pie":
            ax.axis('equal')
            ax.pie(itemCostArray, labels = itemNameArray,autopct='%1.2f%%')

        return ax

    def displaySummaryGraph(self,panel,graphType):
        #Adds the canvas to the panel here.
        figure = plt.figure()
        axis = self.createSummaryGraph(figure,graphType)
        canvas = FigureCanvas(panel, wx.ID_ANY, figure)
        canvas.Hide()
        return canvas

    #Graphtype true means pie, graphtype false = bar

    def swapGraphTypes(self,event):

        if self.graphType == True:

            index = 0

            for i in self.graphArrayPie:

                if i == self.currentGraph:

                    break

                index+=1

            self.swapGraphTypeButton.SetLabel('Display Pie Graphs')

            self.currentGraph.Hide()

            self.currentGraph = self.graphArrayBar[index]
            self.currentGraph.Show()

            self.graphType = False

        else:
            
            index = 0

            for i in self.graphArrayBar:

                if i == self.currentGraph:

                    break
                
                index+=1

            self.swapGraphTypeButton.SetLabel('Display Bar Graphs')

            self.currentGraph.Hide()

            self.currentGraph = self.graphArrayPie[index]
            self.currentGraph.Show()

            self.graphType = True