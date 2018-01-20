#input

stringList = ['magical','unicorns']
numList = [1,2,3,4,5,6,7.7]

#output
# "The list you entered is of mixed type"
# "String: magical unicorns hello world"
# "Sum: 117.98"


mixedList = ['magical unicorns',19,'hello',98.98,'world']    

         
def listChecker (someList):
    StringCheck = False
    NumCheck = False
    Concat_String = ""
    Running_Sum = 0.0
    for val in someList:
        if type(val) == str:
            StringCheck = True
            Concat_String = Concat_String + val + " "
        elif type(val) == float:
            NumCheck = True
            Running_Sum = Running_Sum + val
        elif type(val) == int:
            NumCheck = True
            Running_Sum = Running_Sum + val


listChecker(stringList)
listChecker(numList)
listChecker(mixedList)
