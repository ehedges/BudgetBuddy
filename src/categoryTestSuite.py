from categoryModule import Category
from itemModule import Item

def categoryTests():

    print("Testing Category.")
    
    passTests = 0
    failedTests = []
    currentTest = 1

    print("Test ",currentTest,": Create valid category.")

    try:

        testCategory = Category("Food", 5.00)

        if testCategory.name == "Food" and testCategory.amount == 5.00 and len(testCategory.itemList) == 0:
            passTests = passTests + 1
            print("Created valid category: PASS TEST")
        else:
            print("Error when creating category, unable to create category:TEST FAILED")
            failedTests.insert(len(failedTests),currentTest)
    except:
        print("Error when creating category:TEST FAILED")
        failedTests.insert(len(failedTests),currentTest)
    
    currentTest += 1
    print("Test ",currentTest,": Create invalid category using negative amount.")
    try:

        testCategory = ("Food", -5.00)

        if testCategory == None:
            passTests = passTests + 1
            print("Return None with invalid category: PASS TEST")
        else:
            print("Error when creating category, created with invalid data:TEST FAILED")
            failedTests.insert(len(failedTests),currentTest)

    except:
        print("Error when creating category:TEST FAILED")
        failedTests.insert(len(failedTests),currentTest)

    currentTest += 1
    print("Test ",currentTest,": Create invalid category using None amount.")
    try:

        testCategory = ("Food", None)

        if testCategory == None:
            passTests = passTests + 1
            print("Return None with invalid category: PASS TEST")
        else:
            print("Error when creating category, created with invalid data:TEST FAILED")
            failedTests.insert(len(failedTests),currentTest)

    except:
        print("Error when creating category:TEST FAILED")
        failedTests.insert(len(failedTests),currentTest)

    currentTest += 1
    print("Test ",currentTest,": Create invalid category using empty amount.")
    try:

        testCategory = ("Food", emptyAmount)

        if testCategory == None:
            passTests = passTests + 1
            print("Return None with invalid category: PASS TEST")
        else:
            print("Error when creating category, created with invalid data:TEST FAILED")
            failedTests.insert(len(failedTests),currentTest)

    except:
        print("Error when creating category:TEST FAILED")
        failedTests.insert(len(failedTests),currentTest)


    currentTest += 1
    print("Test ",currentTest,": Create invalid category using None name.")
    try:

        testCategory = (None, 5.00)

        if testCategory == None:
            passTests = passTests + 1
            print("Return None with invalid category: PASS TEST")
        else:
            print("Error when creating category, created with invalid data:TEST FAILED")
            failedTests.insert(len(failedTests),currentTest)

    except:
        print("Error when creating category:TEST FAILED")
        failedTests.insert(len(failedTests),currentTest)

    currentTest += 1
    print("Test ",currentTest,": Create invalid category using no string.")
    try:

        testCategory = (emptyString, 5.00)

        if testCategory == None:
            passTests = passTests + 1
            print("Return None with invalid category: PASS TEST")
        else:
            print("Error when creating category, created with invalid data:TEST FAILED")
            failedTests.insert(len(failedTests),currentTest)

    except:
        print("Error when creating category:TEST FAILED")
        failedTests.insert(len(failedTests),currentTest)

    currentTest += 1
    print("Test ",currentTest,": Create valid category and add an item.")
    try:

        testCategory = Category("Food", 5.00)

        testItem = Item("Coffee",1.50)

        addBool = testCategory.addItem(testItem)

        if len(testCategory.itemList) == 1 and addBool == True:
            passTests = passTests + 1
            print("Created valid category with added item: PASS TEST")
        else:
            print("Error when adding to category:TEST FAILED")
            failedTests.insert(len(failedTests),currentTest)
    except:
        print("Error when creating category:TEST FAILED")
        failedTests.insert(len(failedTests),currentTest)
 
    currentTest += 1
    print("Test ",currentTest,": Create valid category and add 2 items.")
    try:

        testCategory = Category("Food", 5.00)

        testItem = Item("Coffee",1.50)

        testCategory.addItem(testItem)

        testItem = Item("Tea",2.50)

        testCategory.addItem(testItem)

        if len(testCategory.itemList) == 2 and addBool == True:
            passTests = passTests + 1
            print("Created valid category with 2 items: PASS TEST")
        else:
            print("Error when adding items to category:TEST FAILED")
            failedTests.insert(len(failedTests),currentTest)
    except:
        print("Error when creating category:TEST FAILED")
        failedTests.insert(len(failedTests),currentTest)

    currentTest += 1
    print("Test ",currentTest,": Create valid category and delete only item.")
    try:

        testCategory = Category("Food", 5.00)

        testItem = Item("Tea",2.50)

        addBool = testCategory.addItem(testItem)

        deleteBool = testCategory.deleteItemCompare(testItem)

        if len(testCategory.itemList) == 0 and deleteBool == True:
            passTests = passTests + 1
            print("Deleted only item: PASS TEST")
        else:
            print("Error when deleting only itme:TEST FAILED")
            failedTests.insert(len(failedTests),currentTest)
    except:
        print("Error when creating category:TEST FAILED")
        failedTests.insert(len(failedTests),currentTest)
 
    currentTest += 1
    print("Test ",currentTest,": Create valid category and delete one item from 2 items.")
    try:

        testCategory = Category("Food", 5.00)

        testItem = Item("Coffee",1.50)

        testCategory.addItem(testItem)

        testItem = Item("Tea",2.50)

        testCategory.addItem(testItem)

        deleteBool = testCategory.deleteItemCompare(Item("Tea",2.50))

        if len(testCategory.itemList) == 1 and deleteBool == True:
            passTests = passTests + 1
            print("Deleted item from list of 2: PASS TEST")
        else:
            print("Error deleting from category:TEST FAILED")
            failedTests.insert(len(failedTests),currentTest)
    except:
        print("Error when creating category:TEST FAILED")
        failedTests.insert(len(failedTests),currentTest)
 
    currentTest += 1
    print("Test ",currentTest,": Create valid category and delete one item from 3 items.")
    try:

        testCategory = Category("Food", 5.00)

        testItem = Item("Coffee",1.50)

        testCategory.addItem(testItem)

        testItem = Item("Tea",2.50)

        testCategory.addItem(testItem)

        testItem = Item("Burger",0.50)
        
        testCategory.addItem(testItem)

        deleteBool = testCategory.deleteItemCompare(Item("Tea",2.50))

        if len(testCategory.itemList) == 2 and deleteBool == True:
            passTests = passTests + 1
            print("Deleted one item from 3: PASS TEST")
        else:
            print("Error deleting from category:TEST FAILED")
            failedTests.insert(len(failedTests),currentTest)
    except:
        print("Error when creating category:TEST FAILED")
        failedTests.insert(len(failedTests),currentTest)
 
    currentTest += 1
    print("Test ",currentTest,": Create valid category and delete 2 items from 3 items.")
    try:

        testCategory = Category("Food", 5.00)

        testItem = Item("Coffee",1.50)

        testCategory.addItem(testItem)

        testItem = Item("Tea",2.50)

        testCategory.addItem(testItem)

        testCategory.addItem(Item("Burger",0.50))

        deleteBool = testCategory.deleteItemCompare(testItem)

        deleteBool = testCategory.deleteItemCompare(Item("Coffee",1.50))        

        if len(testCategory.itemList) == 1 and deleteBool == True:
            passTests = passTests + 1
            print("Deleted one item from 3: PASS TEST")
        else:
            print("Error deleting from category:TEST FAILED")
            failedTests.insert(len(failedTests),currentTest)
    except:
        print("Error when creating category:TEST FAILED")
        failedTests.insert(len(failedTests),currentTest)

    currentTest += 1
    print("Test ",currentTest,": Create valid category and add None.")
    try:

        testCategory = Category("Food", 5.00)

        testCategory.addItem(None)

        if len(testCategory.itemList) == 0:
            passTests = passTests + 1
            print("Did not add None item: PASS TEST")
        else:
            print("Error when adding to category:TEST FAILED")
            failedTests.insert(len(failedTests),currentTest)
    except:
        print("Error when creating category:TEST FAILED")
        failedTests.insert(len(failedTests),currentTest)

    currentTest += 1
    print("Test ",currentTest,": Create valid category and calculate the remainder.")
    try:

        testCategory = Category("Food", 5.00)

        testItem = Item("Coffee",1.50)

        addItemBool = testCategory.addItem(testItem)

        if testCategory.calculateRemainingAmount() == 3.50 and  addItemBool == True:
            passTests = passTests + 1
            print("Calcualted correct remainder: PASS TEST")
        else:
            print("Error when calculating remainder:TEST FAILED")
            failedTests.insert(len(failedTests),currentTest)
    except:
        print("Error when creating category:TEST FAILED")
        failedTests.insert(len(failedTests),currentTest)
 
    currentTest += 1
    print("Test ",currentTest,": Create valid category, calculate the remainder with no items.")
    try:

        testCategory = Category("Food", 5.00)

        if testCategory.calculateRemainingAmount() == 5.00:
            passTests = passTests + 1
            print("Calculated proper amount with no items: PASS TEST")
        else:
            print("Error when calculating remainder:TEST FAILED")
            failedTests.insert(len(failedTests),currentTest)
    except:
        print("Error when creating category:TEST FAILED")
        failedTests.insert(len(failedTests),currentTest)

    currentTest += 1
    print("Test ",currentTest,": Create valid category and calculate a negative remainder.")
    try:

        testCategory = Category("Food", 3.00)

        testItem = Item("Coffee",1.50)

        testCategory.addItem(testItem)

        testItem = Item("Tea",2.50)

        testCategory.addItem(testItem)

        if testCategory.calculateRemainingAmount() == -1.00:

            passTests = passTests + 1
            print("Calculated negative remainder: PASS TEST")
        else:
            print("Error when calculating remainder:TEST FAILED")
            failedTests.insert(len(failedTests),currentTest)
    except:
        print("Error when creating category:TEST FAILED")
        failedTests.insert(len(failedTests),currentTest)

    currentTest += 1
    print("Test ",currentTest,": Create valid category and calculate with no items.")
    try:

        testCategory = Category("Food", 5.00)

        if testCategory.calculateRemainingAmount() == 5.00:
            passTests = passTests + 1
            print("Calculated remainder with no items: PASS TEST")
        else:
            print("Error when calculating remainder:TEST FAILED")
            failedTests.insert(len(failedTests),currentTest)
    except:
        print("Error when creating category:TEST FAILED")
        failedTests.insert(len(failedTests),currentTest)

 
    currentTest += 1
    print("Test ",currentTest,": Create valid category and delete items from position 2 items.")
    try:

        testCategory = Category("Food", 5.00)

        testItem = Item("Coffee",1.50)

        testCategory.addItem(testItem)

        testItem = Item("Tea",2.50)

        testCategory.addItem(testItem)

        testCategory.addItem(Item("Burger",0.50))

        deleteBool = testCategory.deleteItemPos(2)

        if len(testCategory.itemList) == 2 and deleteBool == True:
            passTests = passTests + 1
            print("Deleted one item from 3: PASS TEST")
        else:
            print("Error deleting from category:TEST FAILED")
            failedTests.insert(len(failedTests),currentTest)
    except:
        print("Error when creating category:TEST FAILED")
        failedTests.insert(len(failedTests),currentTest)

    currentTest += 1
    print("Test ",currentTest,": Create valid category and deleteCompare with no items.")
    try:

        testCategory = Category("Food", 5.00)

        returnBool = testCategory.deleteItemCompare(Item("Burger",0.50))

        if returnBool == False:
            passTests = passTests + 1
            print("Calculated remainder with no items: PASS TEST")
        else:
            print("Error when calculating remainder:TEST FAILED")
            failedTests.insert(len(failedTests),currentTest)
    except:
        print("Error when creating category:TEST FAILED")
        failedTests.insert(len(failedTests),currentTest)

    currentTest += 1
    print("Test ",currentTest,": Create valid category and deletePos with no items.")
    try:

        testCategory = Category("Food", 5.00)

        returnBool = testCategory.deleteItemPos(1)

        if returnBool == False:
            passTests = passTests + 1
            print("Calculated remainder with no items: PASS TEST")
        else:
            print("Error when calculating remainder:TEST FAILED")
            failedTests.insert(len(failedTests),currentTest)
    except:
        print("Error when creating category:TEST FAILED")
        failedTests.insert(len(failedTests),currentTest)

    if currentTest == passTests:
        print("Passed all tests!")
        return failedTests
    else:
        print("Failed tests: ",)
        for i in failedTests:
            print(i, end =',')
        return failedTests

categoryTests()