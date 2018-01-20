# input
wordList = ['hello','world','my','name','is','Anna']
char = 'o'
char2 = 's'
# output
newList = []

def find_char(wordList,char):

    for str in wordList:
        # print wordList
        if char in str:
            print "The following strings contain the letter O: " , str
            newList.append(str)
            print "This is the new list of strings containg the letter O: " , newList
           
        if char2 in str:
            print "The following strings contain the letter S: " , str
            newList.append(str)
            print "This is the new list with sss's tooo: " , newList

find_char(wordList,char)
