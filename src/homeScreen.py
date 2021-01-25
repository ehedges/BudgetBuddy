from budgetModule import Budget
from categoryModule import Category
from itemModule import Item
from datetime import datetime
import wx

class HomePage(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.sizer = wx.GridBagSizer(100, 100)

        menuBar = self.createMenuBar(parent)

        self.path = None
        self.currentPath = None
        self.currentBudget = self.loadSettings()

        tb = wx.ToolBar( self, -1 ) 
        self.ToolBar = tb 
        
        self.budgetBox = self.currentBudget.displayBudget(self,self.sizer)
        self.SetSizerAndFit(self.sizer)

    def createMenuBar(self,parent):
        menuBar = wx.MenuBar()

        fileMenu = wx.Menu()
        menuBar.Append(fileMenu, '&File')
        #File menu selections here
        self.populateFileMenu(fileMenu,parent)

        #View
        viewMenu = wx.Menu()
        menuBar.Append(viewMenu, '&View')

        self.populateViewMenu(viewMenu,parent)

        parent.SetMenuBar(menuBar)

        return menuBar

    def populateFileMenu(self,fileMenu,parent):
        #Quit Option
        fileQuit = wx.MenuItem(fileMenu,wx.ID_EXIT, text = "Quit",kind = wx.ITEM_NORMAL) 
        fileMenu.Append(fileQuit)

        parent.Bind(wx.EVT_MENU, self.OnQuit, fileQuit)

        #Logout Option
        fileLogin = fileMenu.Append(wx.ID_ANY, 'Login', 'Log into application')

        #Logout Option
        fileLogout = fileMenu.Append(wx.ID_ANY, 'Logout', 'Logout of application')

        parent.Bind(wx.EVT_MENU, self.logOut, fileLogout)

        #New Option
        fileNewBudget = fileMenu.Append(wx.ID_ANY, 'New Budget', 'Create New Budget')

        parent.Bind(wx.EVT_MENU, self.dialogCreateBudget, fileNewBudget)

        #SaveOption
        fileSave = fileMenu.Append(wx.ID_ANY, 'Save', 'Save Budget')

        parent.Bind(wx.EVT_MENU, self.OnSave, fileSave)

        #SaveOption
        fileSaveAs = fileMenu.Append(wx.ID_ANY, 'Save As', 'Save Budget as')

        parent.Bind(wx.EVT_MENU, self.OnSaveAs, fileSaveAs)

        #Load Option
        fileLoad = fileMenu.Append(wx.ID_ANY, 'Load', 'Load Budget')

        parent.Bind(wx.EVT_MENU, self.loadBudgetFile, fileLoad)

        #Load Option
        fileCancel = fileMenu.Append(wx.ID_ANY, 'Cancel', 'Cancel')

    def OnQuit(self,event):
        exit()

    def logOut(self,event):

        print("WIP")

    def dialogCreateBudget(self,event):
        
        self.createDialog = wx.Dialog(None,title = 'Create New Budget')
        dialogPanel = wx.Panel(self.createDialog)
        sizer = wx.GridBagSizer(10, 10)
        amountStatic = wx.StaticText(dialogPanel, wx.ID_ANY, "Amount: $") 
        self.amountInput = wx.TextCtrl(dialogPanel) 

        nameStatic = wx.StaticText(dialogPanel, wx.ID_ANY, "Name: ")
        self.nameInput = wx.TextCtrl(dialogPanel)  

        self.todayDateCheckBox = wx.CheckBox(dialogPanel, label = 'Use this month\'s date instead')

        dateStatic = wx.StaticText(dialogPanel, wx.ID_ANY, "Enter a date (MM-YYYY): ")
        self.dateInput = wx.TextCtrl(dialogPanel)  

        self.occurCheckBox = wx.CheckBox(dialogPanel, label = 'Reoccur every month.')
         
        createButton = wx.Button(dialogPanel, wx.ID_ANY, 'Create Budget')

        createButton.Bind(wx.EVT_BUTTON,self.oncreateBudgetDialogClick)
        
        sizer.Add(nameStatic,pos=(1, 1),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)
        sizer.Add(self.nameInput ,pos=(1, 2),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)

        sizer.Add(amountStatic,pos=(2, 1),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)
        sizer.Add(self.amountInput,pos=(2, 2),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)
        
        sizer.Add(self.todayDateCheckBox,pos=(4, 1),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)

        sizer.Add(dateStatic,pos=(3, 1),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)
        sizer.Add(self.dateInput,pos=(3, 2),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)

        sizer.Add(self.occurCheckBox,pos=(5, 1),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)

        sizer.Add(createButton,pos=(6, 2),span=(1, 1),flag = wx.EXPAND|wx.ALIGN_LEFT, border = 5)

        dialogPanel.SetSizerAndFit(sizer)

        self.createDialog.ShowModal()

    def OnSave(self,event):
        print("WIP")
        if self.currentPath is None:
            self.OnSaveAs(event)

        if self.currentPath is not None:

            self.currentBudget.writeBudget(self.currentPath)

        else:
            wx.LogError("Cannot save current data in file "+self.currentPath+".")

    def OnSaveAs(self, event):

        with wx.FileDialog(self, "Save BUDJ file", wildcard="BUDJ files (*.budj)|*.budj",
                           style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return     # the user changed their mind

        # save the current contents in the file
            self.currentPath = fileDialog.GetPath()

            try:
                self.currentBudget.writeBudget(self.currentPath)
            except IOError:
                wx.LogError("Cannot save current data in file "+self.currentPath+".")
        
    def startNewBudget(self):

        self.currentBudget = Budget("TestBudget",15.00,False,"1996-10")


    def loadSettings(self):

        testBudget = Budget("TestBudget",15.00,False,"1996-10")
        testCategory = Category("Food", 5.00)
        testCategoryTwo = Category("Stuff", 10.00)
        testItem = Item("Coffee",1.50)
        testCategory.addItem(testItem)
        testItem = Item("Coffee",2.50)
        testCategory.addItem(testItem)
        testItem = Item("Coffee",1.50)
        testCategory.addItem(testItem)
        testItem = Item("Coffee",2.50)
        testCategory.addItem(testItem)

        testItem = Item("Coffee",1.50)
        testCategoryTwo.addItem(testItem)
        testItem = Item("Coffee",2.00)
        testCategoryTwo.addItem(testItem)
        testItem = Item("Coffee",1.50)
        testCategoryTwo.addItem(testItem)
        testItem = Item("Coffee",2.50)
        testCategoryTwo.addItem(testItem)

        testBudget.addCategory(testCategory)
        testBudget.addCategory(testCategoryTwo)

        return testBudget

    def loadBudgetFile(self,event):

        with wx.FileDialog(self, "Save BUDJ file", wildcard="BUDJ files (*.budj)|*.budj",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return     # the user changed their mind

        # save the current contents in the file
            self.currentPath = fileDialog.GetPath()

            try:

                categoryBool = False
                budgetBool = False

                occur = False
                #Stores the lines to be converted into a category
                categoryLineArray = []
                #HOlds completed categories
                categoryArray = []

                date = ""
                name = ""
                budgetAmount = 0.00

                file = open(self.currentPath,"r")
                #Parsing Starts here
                for line in file:
                    
                    line  = line.rstrip("\r\n")
                    lineArray = line.split(":")
                    if len(lineArray) != 2:

                        if len(lineArray) != 1:
                            raise IOError

                        elif lineArray[0] != '':
                            raise IOError
                        else:
                            continue

                    prefix = lineArray[0]
                    ending = lineArray[1]

                    # If we find a category, make a list of it's contents.
                    if categoryBool == True and budgetBool == True:

                            if prefix == "CATEGORY":
                        
                                categoryBool = self.checkBool(categoryBool,ending)
                                
                                if categoryBool is None:
                                    raise IOError

                                if categoryBool == False:

                                    categoryArray.append(self.loadBudgetParseCategory(categoryLineArray))
                                    categoryLineArray = []
                                    
                            else:
                                categoryLineArray.append(line)   
                    #If somehow we start a category before the budget starts, the file is incorrect so we throw an error.
                    elif categoryBool == True and budgetBool == False:

                        raise IOError
                    #If we are not in a category, then we are in the budget, and should have relevant stuff
                    elif budgetBool == True:
                        #Check if budget starts or ends
                        if prefix == "BUDGET":

                            budgetBool = self.checkBool(budgetBool,ending)

                            if budgetBool is not False:
                                raise IOError
                        #Starts the category
                        elif prefix == "CATEGORY":

                            categoryBool = self.checkBool(categoryBool,ending)

                            if categoryBool is None:
                                raise IOError
                        #Gets the name of the budget
                        elif prefix == "NAME":

                            name = ending
                        #Parses the amount
                        elif prefix == "AMOUNT":

                            budgetAmount = float(ending)
                        #Checks if the budget will occur monthly
                        elif prefix == "REOCCURING":

                            if prefix == "TRUE":

                                occur = True

                            elif prefix == "FALSE":

                                occur = False

                            else:

                                raise IOError
                        
                        elif prefix == "DATE":

                            date = ending

                    else:
                
                        if prefix == "BUDGET":

                            budgetBool = self.checkBool(budgetBool,ending)

                            if budgetBool is not True:
                                raise IOError

                        else:

                            raise IOError

                file.close()

                tempBudget = Budget(name,budgetAmount,occur,date)

                for i in categoryArray:

                    if i == None:
                        raise IOError

                    tempBudget.addCategory(i)

                self.currentBudget = tempBudget
        
                self.updateScreen()
                

            except IOError:
                wx.LogError("Cannot load current data in file "+self.currentPath+".")

    def loadBudgetParseCategory(self,categoryArray):
        name = ""
        amount = ""
        itemArray = []
        #Maybe turn thisinto a function somehow, it is the same as above. 
        for line in categoryArray:

            line  = line.rstrip("\r\n")
            lineArray = line.split(":")

            if len(lineArray) != 2:

                if len(lineArray) != 1:
                    return None

                elif lineArray[0] != '':
                    return None
                else:
                    continue

            prefix = lineArray[0]
            ending = lineArray[1]

            if prefix == "NAME":
                name = ending

            elif prefix == "AMOUNT":
                amount = float(ending)

            elif prefix == "ITEM":

                if ending[0] != "(" or ending[len(ending)-1] != ")":
                    return None

                itemSplit = ending.split(",")

                itemName = itemSplit[0].replace("(","")
                itemAmount = itemSplit[1].replace(")","")            
                itemArray.append(Item(itemName,float(itemAmount)))
            else:
                return None

        tempCategory = Category(name,amount)

        for i in itemArray:

            if i == None:

                return None

            tempCategory.addItem(i)

        return tempCategory

    def oncreateBudgetDialogClick(self,event):
        name = self.nameInput.GetValue()
        amount = float(self.amountInput.GetValue())
        occurBool = self.occurCheckBox.GetValue()

        date = self.dateInput.GetValue() 

        if self.todayDateCheckBox.GetValue() == True:
         
            date = datetime.now().strftime('%Y-%m')
            print(date)

        self.currentBudget = Budget(name,amount,occurBool,date)
        self.updateScreen()
        self.createDialog.Destroy()

    def checkBool(self,check,ending):

        if ending == "END":

            if check == False:
                return None

            check = False

        if ending == "BEGIN":

            if check == True:
                return None

            check = True

        return check

    def findBudgetPath(self):

        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir=self.currentDirectory, 
            defaultFile="",
            wildcard=wildcard,
            style=wx.FD_OPEN | wx.FD_CHANGE_DIR
            )
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            print ("You chose the following file(s):")
            for path in paths:
                self.path = path
        dlg.Destroy()

    def populateViewMenu(self,viewMenu,parent):

        viewDisplayGraph = viewMenu.Append(wx.ID_ANY, 'View Graph', "View Graph")
        parent.Bind(wx.EVT_MENU, self.OnDisplayGraph, viewDisplayGraph)

        viewCategories = viewMenu.Append(wx.ID_ANY, 'View Budget', "View Budget")
        parent.Bind(wx.EVT_MENU, self.OnDisplayCategories, viewCategories)

        viewEditGraph = viewMenu.Append(wx.ID_ANY, 'Graph Settings', "Edit Graph Settings")
        parent.Bind(wx.EVT_MENU, self.OnEditGraph, viewEditGraph)

    def OnDisplayGraph(self,event):
        self.currentBudget.swapFromCategoryToGraph()

    def OnDisplayCategories(self,event):
        print("WIP")
        self.currentBudget.swapFromGraphToCategory()

    def OnEditGraph(self,event):
        print("WIP")

    def updateScreen(self):
        self.sizer.Clear(True)
        self.sizer = wx.GridBagSizer(100, 100)
        self.currentBudget.displayBudget(self,self.sizer)

        self.SetSizerAndFit(self.sizer)
