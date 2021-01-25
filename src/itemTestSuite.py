from itemModule import Item

def itemTests():
    # Testing intialization
    NUMTESTS = 20
    passTests = 0
    currentTest = 1
    failedCount = 0
    failedTests = []
    #1

    print("Test" ,currentTest,": Create valid item.")
    try:
        testItem = Item('Coffee',1.00)
        if testItem.name == "Coffee" and testItem.cost == 1.00:
            print("Created Valid Item:TEST PASSED")
            passTests = passTests + 1
        else:
            raise TypeError
    except TypeError:
        print("Error when creating item:TEST FAILED")
        failedTests.insert(failedCount,currentTest)
        failedCount = failedCount + 1
    except:
        print("Error when conducting test:TEST FAILED")
        failedTests.insert(failedCount,currentTest)
        failedCount = failedCount + 1

    currentTest = currentTest + 1
    print("Test" ,currentTest,":Create invalid item using None string.")
    try:
        testItem = Item(None,1.00)
        if testItem is None:
            print("Made None value when given incorrect data:TEST PASSED")
            passTests = passTests + 1
        else:
            raise TypeError
    except TypeError:
        print("Error when creating item, created item instead of detecing error:TEST FAILED")
        failedTests.insert(failedCount,currentTest)
        failedCount = failedCount + 1
    except:
        print("Error when conducting test:TEST FAILED")
        failedTests.insert(failedCount,currentTest)
        failedCount = failedCount + 1


    testItem = Item("Coffee",-1.00)
    if testItem is None:
        print("Hello")

#3
    currentTest = currentTest + 1
    print("Test" ,currentTest,":Create invalid item using negative cost.")
    try:
        testItem = Item("Coffee",-1.00)
        if testItem is None:
            print("Made None value when given incorrect data:TEST PASSED")
            passTests = passTests + 1
        else:
            raise TypeError
    except TypeError:
        print("Error when creating item, created item instead of detecing error:TEST FAILED")
        failedTests.insert(failedCount,currentTest)
        failedCount = failedCount + 1
    except:
        print("Error when conducting test:TEST FAILED")
        failedTests.insert(failedCount,currentTest)
        failedCount = failedCount + 1

#3
    currentTest = currentTest + 1
    print("Test" ,currentTest,":Create invalid item using None cost.")
    try:
        testItem = Item("Coffee",None)
        if testItem is None:
            print("Made None value when given incorrect data:TEST PASSED")
            passTests = passTests + 1
        else:
            raise TypeError
    except TypeError:
        print("Error when creating item, created item instead of detecing error:TEST FAILED")
        failedTests.insert(failedCount,currentTest)
        failedCount = failedCount + 1
    except:
        print("Error when conducting test:TEST FAILED")
        failedTests.insert(failedCount,currentTest)
        failedCount = failedCount + 1

    currentTest = currentTest + 1
    print("Test" ,currentTest,":Create invalid item using String as cost")
    try:
        
        testItem = Item("Coffee","Cost")
        if testItem is None:
            print("Made None value when given incorrect data:TEST PASSED")
            passTests = passTests + 1
        else:
            raise TypeError
    except TypeError:
        print("Error when creating item, created item instead of detecing error:TEST FAILED")
        failedTests.insert(failedCount,currentTest)
        failedCount = failedCount + 1
    except:
        print("Error when conducting test:TEST FAILED")
        failedTests.insert(failedCount,currentTest)
        failedCount = failedCount + 1


    currentTest = currentTest + 1
    print("Test" ,currentTest,": Compare two items with the same cost .")
    try:
        
        testItem = Item("Coffee",1.00)
        testItemTwo = Item("Coffee",1.00)

        if testItem.compareItemCost(testItemTwo) == True:
            print("Correctly compared the same costs:TEST PASSED")
            passTests = passTests + 1
        else:
            raise TypeError
    except TypeError:
        print("Error when creating item, created item instead of detecing error:TEST FAILED")
        failedTests.insert(failedCount,currentTest)
        failedCount = failedCount + 1
    except:
        print("Error when conducting test:TEST FAILED")
        failedTests.insert(failedCount,currentTest)
        failedCount = failedCount + 1

    currentTest = currentTest + 1
    print("Test" ,currentTest,": Compare two items with different costs .")
    try:
        
        testItem = Item("Coffee",1.00)
        testItemTwo = Item("Coffee",2.00)   
        returnBool = testItem.compareItemCost(testItemTwo)
        if returnBool == False:
            print("Correctly compared two different costs:TEST PASSED")
            passTests = passTests + 1
        else:
            raise TypeError
    except TypeError:
        print("Error when comparing item, wrong return:TEST FAILED")
        failedTests.insert(failedCount,currentTest)
        failedCount = failedCount + 1
    except:
        print("Error when conducting test:TEST FAILED")
        failedTests.insert(failedCount,currentTest)
        failedCount = failedCount + 1


    currentTest = currentTest + 1
    print("Test" ,currentTest,": Compare invalid item using negative cost.")
    try:
        
        testItem = Item("Coffee",1.00)
        testItemTwo = Item("Coffee",1.00)
        testItemTwo.cost = -1.00
        returnBool = testItem.compareItemCost(testItemTwo) 
        if returnBool is None:
            print("Correctly negative compared costs:TEST PASSED")
            passTests = passTests + 1
        else:
            raise TypeError
    except TypeError:
        print("Error when comparing item, wrong return:TEST FAILED")
        failedTests.insert(failedCount,currentTest)
        failedCount = failedCount + 1
    except:
        print("Error when conducting test:TEST FAILED")
        failedTests.insert(failedCount,currentTest)
        failedCount = failedCount + 1

    currentTest = currentTest + 1
    print("Test" ,currentTest,": Compare invalid item using None cost.")
    try:
        
        testItem = Item("Coffee",1.00)
        testItemTwo = Item("Coffee",1.00)
        testItemTwo.cost = None
        
        if testItem.compareItemCost(testItemTwo) is None:
            print("Correctly None compared costs:TEST PASSED")
            passTests = passTests + 1
        else:
            raise TypeError
    except TypeError:
        print("Error when comparing item, wrong return:TEST FAILED")
        failedTests.insert(failedCount,currentTest)
        failedCount = failedCount + 1
    except:
        print("Error when conducting test:TEST FAILED")
        failedTests.insert(failedCount,currentTest)
        failedCount = failedCount + 1
#Check this here.
    currentTest = currentTest + 1
    print("Test" ,currentTest,": Compare Item with the same name.")
    try:
        
        testItem = Item("Coffee",1.00)
        testItemTwo = Item("Coffee",1.00)
        
        if testItem.compareItemName(testItemTwo) == True:
            print("Correctly compared names:TEST PASSED")
            passTests = passTests + 1
        else:
            raise TypeError
    except TypeError:
        print("Error when comparing item, wrong return:TEST FAILED")
        failedTests.insert(failedCount,currentTest)
        failedCount = failedCount + 1
    except:
        print("Error when conducting test:TEST FAILED")
        failedTests.insert(failedCount,currentTest)
        failedCount = failedCount + 1
#check this here
    currentTest = currentTest + 1
    print("Test" ,currentTest,": Compare item with different names.")
    try:
        
        testItem = Item("Coffee",1.00)
        testItemTwo = Item("Tea",1.00)
        
        if testItem.compareItemName(testItemTwo) == False:
            print("Correctly compared two different names:TEST PASSED")
            passTests = passTests + 1
        else:
            raise TypeError
    except TypeError:
        print("Error when comparing item, wrong return:TEST FAILED")
        failedTests.insert(failedCount,currentTest)
        failedCount = failedCount + 1
    except:
        print("Error when conducting test:TEST FAILED")
        failedTests.insert(failedCount,currentTest)
        failedCount = failedCount + 1
#check this one here
    currentTest = currentTest + 1
    print("Test" ,currentTest,": Compare invalid item using None string.")
    try:
        
        testItem = Item("Coffee",1.00)
        testItemTwo = Item("Tea",1.00)
        
        testItemTwo.name = None
        returnBool = testItem.compareItemName(testItemTwo)
        if returnBool is None:
            print("Correctly None compared costs:TEST PASSED")
            passTests = passTests + 1
        else:
            raise TypeError
    except TypeError:
        print("Error when comparing item, wrong return:TEST FAILED")
        failedTests.insert(failedCount,currentTest)
        failedCount = failedCount + 1
    except:
        print("Error when conducting test:TEST FAILED")
        failedTests.insert(failedCount,currentTest)
        failedCount = failedCount + 1

    currentTest = currentTest + 1
    print("Test" ,currentTest,": Compare Item that are the same.")
    try:
        
        testItem = Item("Coffee",1.00)
        testItemTwo = Item("Coffee",1.00)
        returnBool = testItem.compareItem(testItemTwo)
        if returnBool == True:
            print("Correctly compared names:TEST PASSED")
            passTests = passTests + 1
        else:
            raise TypeError
    except TypeError:
        print("Error when comparing item, wrong return:TEST FAILED")
        failedTests.insert(failedCount,currentTest)
        failedCount = failedCount + 1
    except:
        print("Error when conducting test:TEST FAILED")
        failedTests.insert(failedCount,currentTest)
        failedCount = failedCount + 1

    currentTest = currentTest + 1
    print("Test" ,currentTest,": Compare Item that are the different.")
    try:
        
        testItem = Item("Coffee",1.00)
        testItemTwo = Item("Coffee",1.50)
        returnBool = testItem.compareItem(testItemTwo)
        if returnBool == False:
            print("Correctly compared names:TEST PASSED")
            passTests = passTests + 1
        else:
            raise TypeError
    except TypeError:
        print("Error when comparing item, wrong return:TEST FAILED")
        failedTests.insert(failedCount,currentTest)
        failedCount = failedCount + 1
    except:
        print("Error when conducting test:TEST FAILED")
        failedTests.insert(failedCount,currentTest)
        failedCount = failedCount + 1

    currentTest = currentTest + 1
    print("Test" ,currentTest,": Update name.")
    try:
        
        testItem = Item('Coffee',1.00)
        boolReturn = testItem.updateItemName('Tea')
        if testItem.name == 'Tea' and  boolReturn == True:
            print("Correctly updated name:TEST PASSED")
            passTests = passTests + 1
        else:
            raise TypeError
    except TypeError:
        print("Error when updating item name:TEST FAILED")
        failedTests.insert(failedCount,currentTest)
        failedCount = failedCount + 1
    except:
        print("Error when conducting test:TEST FAILED")
        failedTests.insert(failedCount,currentTest)
        failedCount = failedCount + 1

    currentTest = currentTest + 1
    print("Test" ,currentTest,": Update cost.")
    try:
        
        testItem = Item("Coffee",1.00)
        testItem.updateItemCost(2.50)
        
        if testItem.cost == 2.50:
            print("Correctly updated cost:TEST PASSED")
            passTests = passTests + 1
        else:
            raise TypeError
    except TypeError:
        print("Error when updating cost:TEST FAILED")
        failedTests.insert(failedCount,currentTest)
        failedCount = failedCount + 1
    except:
        print("Error when conducting test:TEST FAILED")
        failedTests.insert(failedCount,currentTest)
        failedCount = failedCount + 1

    currentTest = currentTest + 1
    print("Test" ,currentTest,": Write Item.")
    try:
        
        testItem = Item("Coffee",1.00)

        writeString = testItem.writeItemString()
        if writeString == "ITEM:(Coffee,1.00)\r\n":
            print("Correctly compared names:TEST PASSED")
            passTests = passTests + 1
        else:
            raise TypeError
    except TypeError:
        print("Error when writing item, wrong string:TEST FAILED")
        failedTests.insert(failedCount,currentTest)
        failedCount = failedCount + 1
    except:
        print("Error when conducting test:TEST FAILED")
        failedTests.insert(failedCount,currentTest)
        failedCount = failedCount + 1
    currentTest = currentTest + 1

    print("Test" ,currentTest,": Get Item cost.")
    try:
        
        testItem = Item("Coffee",1.00)
        
        if testItem.getCost() == True:
            print("Correctly returned cost:TEST PASSED")
            passTests = passTests + 1
        else:
            raise TypeError
    except TypeError:
        print("Error when getting cost, wrong return:TEST FAILED")
        failedTests.insert(failedCount,currentTest)
        failedCount = failedCount + 1
    except:
        print("Error when conducting test:TEST FAILED")
        failedTests.insert(failedCount,currentTest)
        failedCount = failedCount + 1

    if NUMTESTS == passTests:
        print("PASSED ALL TESTS!")
        return failedTests
    else:
        print("Failed tests: ",)

        for i in failedTests:
            print(i, end =',')
        return failedTests

    return

itemTests()