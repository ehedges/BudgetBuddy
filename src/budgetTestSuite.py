from budgetModule import Budget
from categoryTestSuite import categoryTests
from categoryModule import Category
from itemTestSuite import itemTests
from itemModule import Item

itemTestResults  = itemTests()
    
if len(itemTestResults) > 0:
    print("Failed item tests.")
else:
    print("Passed all item tests.")

categoryTestResults = categoryTests()

if len(categoryTestResults) > 0:
    print("Failed item tests.")
else:
    print("Passed all item tests.")

currentTest = 1
passTest = 0 
failedCount = 0
failedTest = []

print("Test ",currentTest,": Create valid empty budget with False Bool.")

try:

    testBudget = Budget("TestBudget",10.00,False,"10-1996")

    if testBudget.name != "TestBudget" or testBudget.amount != 10.00 or testBudget.reoccur != False or testBudget.date != "10-1996":
        print ("Error when creating budget, Wrong values: FAILED TEST")
        failedTest.insert(failedCount,currentTest)
        failedCount = failedCount+1
    else:
        print ("Created proper budget: PASSED TEST")
        passTest = passTest + 1

except:
    print ("Error when creating budget.")
    failedTest.insert(0,currentTest)

currentTest = currentTest +1
print("Test ",currentTest,": Create valid empty budget with True Bool.")
testBudget = Budget("TestBudget",10.00,True,"10-1996")
try:

    testBudget = Budget("TestBudget",10.00,True,"10-1996")

    if testBudget.name != "TestBudget" or testBudget.amount != 10.00 or testBudget.reoccur != True or testBudget.date != "10-1996":
        print ("Error when creating budget, Wrong values: FAILED TEST")
        failedTest.insert(failedCount,currentTest)
        failedCount = failedCount+1
    else:
        print ("Created proper budget: PASSED TEST")
        passTest = passTest + 1

except:
    print ("Error when creating budget.")
    failedTest.insert(failedCount,currentTest)
    failedCount = failedCount+1

currentTest = currentTest +1
print("Test ",currentTest,": Create invalid empty budget with negative amount.")
try:

    testBudget = Budget("TestBudget",-10.00,True,"10-1996")

    if testBudget.name != None:
        print ("Error when creating budget, Wrong values: FAILED TEST")
        failedTest.insert(failedCount,currentTest)
        failedCount = failedCount+1
    else:
        print ("Created proper budget: PASSED TEST")
        passTest = passTest + 1

except:
    print ("Error when creating budget.")
    failedTest.insert(failedCount,currentTest)
    failedCount = failedCount+1

currentTest = currentTest +1
print("Test ",currentTest,": Create invalid with invalid date.")
try:

    testBudget = Budget("TestBudget",10.00,True,"13-1996")

    if testBudget.name != None:
        print ("Error when creating budget, Wrong values: FAILED TEST")
        failedTest.insert(failedCount,currentTest)
        failedCount = failedCount+1
    else:
        print ("Created proper budget: PASSED TEST")
        passTest = passTest + 1

except:
    print ("Error when creating budget.")
    failedTest.insert(failedCount,currentTest)
    failedCount = failedCount+1

currentTest = currentTest +1
print("Test ",currentTest,": Create invalid with letters as date.")
try:

    testBudget = Budget("TestBudget",10.00,True,"agadgadfg")

    if testBudget.name != None:
        print ("Error when creating budget, Wrong values: FAILED TEST")
        failedTest.insert(failedCount,currentTest)
        failedCount = failedCount+1
    else:
        print ("Created proper budget: PASSED TEST")
        passTest = passTest + 1

except:
    print ("Error when creating budget.")
    failedTest.insert(failedCount,currentTest)
    failedCount = failedCount+1

currentTest = currentTest +1
print("Test ",currentTest,": Create a budget with a category without item. ")

try:

    testBudget = Budget("TestBudget",10.00,False,"10-1996")

    testCategory = Category("Food", 5.00)

    testBudget.addCategory(testCategory)

    if (testBudget.name != "TestBudget" or testBudget.amount != 10.00 or testBudget.reoccur != False or testBudget.date != "10-1996") and len(testBudget.categoryArray) != 1:
        print ("Error when creating budget, Wrong values: FAILED TEST")
        failedTest.insert(failedCount,currentTest)
        failedCount = failedCount+1
    else:
        print ("Created proper budget: PASSED TEST")
        passTest = passTest + 1

except:
    print ("Error when creating budget.")
    failedTest.insert(failedCount,currentTest)
    failedCount = failedCount+1

currentTest = currentTest +1
print("Test ",currentTest,": Create a budget with a category with an item added before. ")

try:

    testBudget = Budget("TestBudget",10.00,False,"10-1996")

    testCategory = Category("Food", 5.00)
    testItem = Item("Coffee",1.50)
    testCategory.addItem(testItem)
    testBudget.addCategory(testCategory)

    if (testBudget.name != "TestBudget" or testBudget.amount != 10.00 or testBudget.reoccur != False or testBudget.date != "10-1996") and len(testBudget.categoryArray) != 1:
        print ("Error when creating budget, Wrong values: FAILED TEST")
        failedTest.insert(failedCount,currentTest)
        failedCount = failedCount+1
    else:
        print ("Created proper budget: PASSED TEST")
        passTest = passTest + 1

except:
    print ("Error when creating budget.")
    failedTest.insert(failedCount,currentTest)
    failedCount = failedCount+1

currentTest = currentTest +1
print("Test ",currentTest,": Create a budget with a category with an item added after. ")

try:

    testBudget = Budget("TestBudget",10.00,False,"10-1996")

    testCategory = Category("Food", 5.00)
    testBudget.addCategory(testCategory)
    testItem = Item("Coffee",1.50)
    testCategory.addItem(testItem)

    if (testBudget.name != "TestBudget" or testBudget.amount != 10.00 or testBudget.reoccur != False or testBudget.date != "10-1996") and len(testBudget.categoryArray) != 1:
        print ("Error when creating budget, Wrong values: FAILED TEST")
        failedTest.insert(failedCount,currentTest)
        failedCount = failedCount+1
    else:
        print ("Created proper budget: PASSED TEST")
        passTest = passTest + 1

except:
    print ("Error when creating budget.")
    failedTest.insert(failedCount,currentTest)
    failedCount = failedCount+1

currentTest = currentTest +1
print("Test ",currentTest,": Update budget name.")

try:

    testBudget = Budget("TestBudget",10.00,False,"10-1996")

    testBudget.updateBudgetName("BudgetTest")

    if testBudget.name != "BudgetTest" or testBudget.amount != 10.00 or testBudget.reoccur != False or testBudget.date != "10-1996":
        print ("Error when creating budget, Wrong values: FAILED TEST")
        failedTest.insert(failedCount,currentTest)
        failedCount = failedCount+1
    else:
        print ("Created proper budget: PASSED TEST")
        passTest = passTest + 1

except:
    print ("Error when creating budget.")
    failedTest.insert(failedCount,currentTest)
    failedCount = failedCount+1

currentTest = currentTest +1
print("Test ",currentTest,": Update budget amount.")

try:

    testBudget = Budget("TestBudget",10.00,False,"10-1996")

    returnVal = testBudget.updateAmount(15.50)

    if (testBudget.name != "TestBudget" or testBudget.amount != 15.50 or testBudget.reoccur != False or testBudget.date != "10-1996") and returnVal == True:
        print ("Error when creating budget, Wrong values: FAILED TEST")
        failedTest.insert(failedCount,currentTest)
        failedCount = failedCount+1
    else:
        print ("Created proper budget: PASSED TEST")
        passTest = passTest + 1

except:
    print ("Error when creating budget.")
    failedTest.insert(failedCount,currentTest)
    failedCount = failedCount+1

currentTest = currentTest +1
print("Test ",currentTest,": Update budget with negative amount.")

try:

    testBudget = Budget("TestBudget",10.00,False,"10-1996")

    returnVal = testBudget.updateAmount(-15.50)

    if (testBudget.name != "TestBudget" or testBudget.amount != 10.00 or testBudget.reoccur != False or testBudget.date != "10-1996") or returnVal == True:
        print ("Error when creating budget, Wrong values: FAILED TEST")
        failedTest.insert(failedCount,currentTest)
        failedCount = failedCount+1
    else:
        print ("Created proper budget: PASSED TEST")
        passTest = passTest + 1
except:
    print ("Error when creating budget.")
    failedTest.insert(failedCount,currentTest)
    failedCount = failedCount+1

currentTest = currentTest +1
print("Test ",currentTest,": Update budget occur.")

try:

    testBudget = Budget("TestBudget",10.00,False,"10-1996")

    testBudget.updateOccur(True)

    if testBudget.name != "TestBudget" or testBudget.amount != 10.00 or testBudget.reoccur != True or testBudget.date != "10-1996":
        print ("Error when creating budget, Wrong values: FAILED TEST")
        failedTest.insert(failedCount,currentTest)
        failedCount = failedCount+1
    else:
        print ("Created proper budget: PASSED TEST")
        passTest = passTest + 1

except:
    print ("Error when creating budget.")
    failedTest.insert(failedCount,currentTest)
    failedCount = failedCount+1

currentTest = currentTest +1
print("Test ",currentTest,": Update budget occur with None.")

try:

    testBudget = Budget("TestBudget",10.00,False,"10-1996")

    returnBool = testBudget.updateOccur(None)

    if testBudget.reoccur != False or returnBool != False:
        print ("Error when creating budget, Wrong values: FAILED TEST")
        failedTest.insert(failedCount,currentTest)
        failedCount = failedCount+1
    else:
        print ("Created proper budget: PASSED TEST")
        passTest = passTest + 1

except:
    print ("Error when creating budget.")
    failedTest.insert(failedCount,currentTest)
    failedCount = failedCount+1

currentTest = currentTest +1
print("Test ",currentTest,": Update budget occur with string.")

try:

    testBudget = Budget("TestBudget",10.00,False,"10-1996")

    returnVal = testBudget.updateOccur("Value")

    if testBudget.reoccur != False or returnBool != False:
        print ("Error when creating budget, Wrong values: FAILED TEST")
        failedTest.insert(failedCount,currentTest)
        failedCount = failedCount+1
    else:
        print ("Created proper budget: PASSED TEST")
        passTest = passTest + 1

except:
    print ("Error when creating budget.")
    failedTest.insert(failedCount,currentTest)
    failedCount = failedCount+1

currentTest = currentTest +1
print("Test ",currentTest,": Calculate spending on empty budget.")

try:

    testBudget = Budget("TestBudget",10.00,False,"10-1996")
        
    testSpending = testBudget.totalSpending()

    if testSpending != 0:
        print ("Error when creating budget, Wrong values: FAILED TEST")
        failedTest.insert(failedCount,currentTest)
        failedCount = failedCount+1
    else:
        print ("Created proper budget: PASSED TEST")
        passTest = passTest + 1

except:
    print ("Error when creating budget.")
    failedTest.insert(failedCount,currentTest)
    failedCount = failedCount+1


currentTest = currentTest +1
print("Test ",currentTest,": Calculate spending on budget with empty category.")

try:

    testBudget = Budget("TestBudget",10.00,False,"10-1996")
        
    testCategory = Category("Food", 5.00)

    testBudget.addCategory(testCategory)

    testSpending = testBudget.totalSpending()

    if testSpending != 0:
        print ("Error when creating budget, Wrong values: FAILED TEST")
        failedTest.insert(failedCount,currentTest)
        failedCount = failedCount+1
    else:
        print ("Created proper budget: PASSED TEST")
        passTest = passTest + 1

except:
    print ("Error when creating budget.")
    failedTest.insert(failedCount,currentTest)
    failedCount = failedCount+1

currentTest = currentTest +1
print("Test ",currentTest,": Calculate spending on budget with category with one object.")

try:

    testBudget = Budget("TestBudget",10.00,False,"10-1996")
        
    testCategory = Category("Food", 5.00)
    testItem = Item("Coffee",1.50)
    testCategory.addItem(testItem)
    testBudget.addCategory(testCategory)

    testSpending = testBudget.totalSpending()

    if testSpending != 1.50:
        print ("Error when creating budget, Wrong values: FAILED TEST")
        failedTest.insert(failedCount,currentTest)
        failedCount = failedCount+1
    else:
        print ("Created proper budget: PASSED TEST")
        passTest = passTest + 1

except:
    print ("Error when creating budget.")
    failedTest.insert(failedCount,currentTest)
    failedCount = failedCount+1

currentTest = currentTest +1
print("Test ",currentTest,": Calculate spending on budget with category with two objects.")

try:

    testBudget = Budget("TestBudget",10.00,False,"10-1996")
        
    testCategory = Category("Food", 5.00)
    testItem = Item("Coffee",1.50)
    testCategory.addItem(testItem)
    testItem = Item("Coffee",2.50)
    testCategory.addItem(testItem)
    testBudget.addCategory(testCategory)

    testSpending = testBudget.totalSpending()

    if testSpending != 4.00:
        print ("Error when creating budget, Wrong values: FAILED TEST")
        failedTest.insert(failedCount,currentTest)
        failedCount = failedCount+1
    else:
        print ("Created proper budget: PASSED TEST")
        passTest = passTest + 1

except:
    print ("Error when creating budget.")
    failedTest.insert(failedCount,currentTest)
    failedCount = failedCount+1

currentTest = currentTest +1
print("Test ",currentTest,": Calculate spending on budget with two category, one of which has an object.")

try:

    testBudget = Budget("TestBudget",10.00,False,"10-1996")
        
    testCategory = Category("Food", 5.00)
    testCategoryTwo = Category("Food", 5.00)
    testItem = Item("Coffee",1.50)
    testCategory.addItem(testItem)
    testBudget.addCategory(testCategory)
    testBudget.addCategory(testCategoryTwo)

    testSpending = testBudget.totalSpending()

    if testSpending != 1.50:
        print ("Error when creating budget, Wrong values: FAILED TEST")
        failedTest.insert(failedCount,currentTest)
        failedCount = failedCount+1
    else:
        print ("Created proper budget: PASSED TEST")
        passTest = passTest + 1

except:
    print ("Error when creating budget.")
    failedTest.insert(failedCount,currentTest)
    failedCount = failedCount+1


currentTest = currentTest + 1
print("Test ",currentTest,": Calculate spending on budget with two categories, each has multiple items.")

try:

    testBudget = Budget("TestBudget",10.00,False,"10-1996")
        
    testCategory = Category("Food", 5.00)
    testCategoryTwo = Category("Food", 5.00)
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
    testItem = Item("Coffee",2.50)
    testCategoryTwo.addItem(testItem)
    testItem = Item("Coffee",1.50)
    testCategoryTwo.addItem(testItem)
    testItem = Item("Coffee",2.50)
    testCategoryTwo.addItem(testItem)

    testBudget.addCategory(testCategory)
    testBudget.addCategory(testCategoryTwo)
    
    testSpending = testBudget.totalSpending()

    if testSpending != 16.00:
        print ("Error when creating budget, Wrong values: FAILED TEST")
        failedTest.insert(failedCount,currentTest)
        failedCount = failedCount+1
    else:
        print ("Created proper budget: PASSED TEST")
        passTest = passTest + 1
 
except:
    print ("Error when creating budget.")
    failedTest.insert(failedCount,currentTest)
    failedCount = failedCount+1

currentTest = currentTest + 1
print("Test ",currentTest,": Calculate remainder of budget with two categories, each has multiple items.")
try:

    testBudget = Budget("TestBudget",10.00,False,"10-1996")
        
    testCategory = Category("Food", 5.00)
    testCategoryTwo = Category("Food", 5.00)
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
    testItem = Item("Coffee",2.50)
    testCategoryTwo.addItem(testItem)
    testItem = Item("Coffee",1.50)
    testCategoryTwo.addItem(testItem)
    testItem = Item("Coffee",2.50)
    testCategoryTwo.addItem(testItem)

    testBudget.addCategory(testCategory)
    testBudget.addCategory(testCategoryTwo)
    testSpending = testBudget.totalRemaining()

    if testBudget.name != "TestBudget" or testBudget.amount != 10.00 or testBudget.reoccur != False or testBudget.date != "10-1996":
        print ("Error when creating budget, Wrong values: FAILED TEST")
        failedTest.insert(failedCount,currentTest)
        failedCount = failedCount+1

    elif testSpending != -6.00:
        print ("Error when creating budget, Wrong values: FAILED TEST")
        failedTest.insert(failedCount,currentTest)
        failedCount = failedCount+1
    else:
        print ("Created proper budget: PASSED TEST")
        passTest = passTest + 1
except:
    print ("Error when creating budget.")
    failedTest.insert(failedCount,currentTest)
    failedCount = failedCount+1

if currentTest == passTest:
    print("Passed all tests!")

else:
    print("Failed tests: ",)
    for i in failedTest:
        print(i, end =',')

print("\n\nResults Summary:")
print("\nItem:")
if len(itemTestResults) > 0:
    print("Failed tests: ",)
    for i in itemTestResults:
        print(i, end =',')

else:
    print("Passed all item tests.")
print("\n\nCategory:")
if len(categoryTestResults) > 0:
    print("Failed tests: ",)
    for i in categoryTestResults:
        print(i, end =',')

else:
    print("Passed all item tests.")

print("\n\nBudget:")
if currentTest == passTest:
    print("Passed all tests!")

else:
    print("Failed tests: ",)
    for i in failedTest:
        print(i, end =',')
    print("\n")