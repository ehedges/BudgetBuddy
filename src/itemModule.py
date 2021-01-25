import json
#Creates item
#In: Name of Item and Cost
#Out: Item Object
class Item:

    def __init__(self, nameItem, costItem):

        self.name = None
        self.cost = None

        try: 
            #Checks if the cost is a number larger than 0, and that the type of name is string
            if costItem < 0.00 or type(nameItem) is not str:
                self = None
            else:

                if len(nameItem) < 1:
                    self = None
                else:
                    self.name = nameItem
                    self.cost = round(costItem,2)

                    if self.name == None or self.cost == None:
                        self = None
        except:
            self = None

#Turns the item into a string that can be read in.
#In: Item
#Out: A string representing the item
    def writeItemString(self):
        return("ITEM:("+self.name+","+str(format(self.cost, '.2f'))+")\r\n")

    def updateItemName(self,name):

        try: 

            if type(name) is not str:

                return False

            self.name = name

            return True

        except:

            return None

#Changes the item Cost
#In: Item, Float
#Out: An item with updated cost. 
    def updateItemCost(self,cost):

        try: 

            if type(cost) is not float:

                return False

            self.cost = cost
            return True

        except:

            return None

#Compares itembased upon name and cost. Returns true if equal, false if not
#In: Item and item to checl
#Out: Boolean

    def compareItem(self,checkItem):

        compBoolCost = self.compareItemCost(checkItem) 
        compBoolName = self.compareItemName(checkItem) 
        if compBoolCost == True and compBoolName == True:
            return True

        elif compBoolCost == None or compBoolName == None:
            return None   

        else:
            return False

#Compares itembased upon name and cost. Returns true if equal, false if not
#In: Item and item to checl
#Out: Boolean

    def compareItemCost(self,checkItem):
        try:

            checkCost = 0.00

            if type(self.cost) is not float:
                return None

            if type(checkItem) is float:
                checkCost = checkItem
            elif type(checkItem.cost) is float:
                checkCost = checkItem.cost
            else:
                return None

            if self.cost < 0 or checkCost < 0:
                return None

            return  self.cost == checkCost
        except:

            return None

    def compareItemName(self,checkItem):
        try:


            if type(self.name) is not str or type(checkItem.name) is not str:
                return None

            return  self.name == checkItem.name
        except:
            return None

    def getCost(self):
        return self.cost

    def getName(self):
        return self.name

    def insertListCost(self,array):
        array.append(self.cost)
        return array

    def insertListName(self,array):
        array.append(self.name)
        return array

    def displayItem(self,itemListUI,index):
        itemListUI.InsertItem(index, self.name)
        itemListUI.SetItem(index, 1, "$ "+str(format(self.cost, '.2f'))) 

    def toJSON(self):

        itemJSON = {"name":self.name,"cost":self.cost}

        return json.dumps(itemJSON)

    def validateItem(self):

        try:

            if type(self.name) is not str:
                raise TypeError
            if len(self.name) < 1:
                raise TypeError
            if type(self.cost) is not float:
                raise TypeError
            if self.cost < 0:
                raise TypeError

        except TypeError:
            return False
        except:
            return None

        return True


