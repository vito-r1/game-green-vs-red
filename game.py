#!/usr/bin/python3
import io
import numpy as np


#Reading the data from the file
filename = 'testfile.txt'
def getdata(filename):
    file = open(filename, 'r')
    lines = [i.rstrip() for i in file.readlines()]
    file.close()
    return lines

lines = getdata(filename)
alllines = lines[1:-1]

#Getting the data from the first row
firstline = [lines[0].split(', ')]
testx = int(firstline[0][0])
testy = int(firstline[0][1])

#Checking if the rule of the game regarding x, y is ok
if testx <= testy < 1000:
    print("OK")
else:
    exit(print("Wrong x or y"))

#From the last row the data is extracted
lastline = [lines[-1].split(', ')]
x1 = int(lastline[0][0]) - 1 #due the array index is starting from 0
y1 = int(lastline[0][1]) - 1
generationnnn = int(lastline[0][-1])

#print(alllines)

#Every other data become a 2d array
newarray = np.array([list(a) for a in alllines]).astype(int)
#print(newarray)

firstx = 0
firsty = 0
lastx = testx - 1
lasty = testy - 1

class Checks:   
        
    #Simple checks that will return an array with the surrounding cells
    def matrixxy(self, x, y, xminus1, xplus1, xplus2, yminus1, yplus1, yplus2, valueofxy, arrayname):
        if index == (firstx, firsty):
            leftcornerup = arrayname[:2, :2]
            datamatrixxy = leftcornerup
            return datamatrixxy
        elif index == (firstx, lasty):
            rightcornerup = arrayname[:2, -2:]
            datamatrixxy = rightcornerup
            return datamatrixxy
        elif index == (lastx, firsty):
            leftcornerdown = arrayname[-2:, :2]
            datamatrixxy = leftcornerdown
            return datamatrixxy
        elif index == (lastx, lasty):
            rightcornerdown = arrayname[-2:, -2:]
            datamatrixxy = rightcornerdown
            return datamatrixxy
        elif x == (firstx):
            firstrow = arrayname[:xplus2, yminus1:yplus2]
            datamatrixxy = firstrow
            return datamatrixxy
        elif y == (firsty):
            firstcolumn = arrayname[xminus1:xplus2, :yplus2]
            datamatrixxy = firstcolumn
            return datamatrixxy
        elif y == (lasty):
            lastcolumn = arrayname[xminus1:xplus2, yminus1:]
            datamatrixxy = lastcolumn
            return datamatrixxy
        elif x == (lastx):
            lastrow = arrayname[xminus1:, yminus1:yplus2]
            datamatrixxy = lastrow
            return datamatrixxy    
        else:
            matrix9 = arrayname[xminus1:xplus2, yminus1:yplus2]
            datamatrixxy = matrix9
            return datamatrixxy 
    
    #Counting the null and ones from the returned array by matrixxy()
    def countthemall(self, dcount, valueofxy):
        zeros = np.count_nonzero(dcount == 0)
        ones = np.count_nonzero(dcount == 1)
        if valueofxy == 0:
            zeros -= 1
            return zeros, ones
        else:
            ones -= 1
            return zeros, ones
        
    #Applaying the rules of the game regarding the value of x, y and counted 0s or 1s    
    def rulesofthegame(self, valueofxyd, cnt0, cnt1):
        #print("Print value of xy is:", valueofxy, "; Count0, cnt1: ",cnt0 , cnt1)
        if valueofxyd == 1:
            if cnt1 == (0 or 1 or 4 or 5 or 7 or 8):
                dataofxy = int(0)
                return int(dataofxy)
            else:
                dataofxy = 1
                return int(dataofxy)        
        else:
            if cnt1 == (0 or 1 or 2 or 4 or 5 or 7 or 8):
                dataofxy = 1
                return int(dataofxy)
            else:
                dataofxy = int(0)
                return int(dataofxy)        
            
            
    #First testing if there is a change of the value if not it keeps it as it is else change it
    def changeofthevalue(self, changedvalue, arrayname, x, y):
            arrayname[x, y] = changedvalue
            return True
    
    #The internal checks - one by one
    def switch(self):
        mtrxxy = self.matrixxy(x, y, xminus1, xplus1, xplus2, yminus1, yplus1, yplus2, valueofxy, arrcur.arr)
        cnt0, cnt1 = self.countthemall(mtrxxy, valueofxy)
        rlsgame = self.rulesofthegame(valueofxy, cnt0, cnt1)
        print(rlsgame)
        chngvle = self.changeofthevalue(rlsgame, arrnext.arr, x, y)
        #print("--------")
        #print(valueofxy, mtrxxy, cnt0, cnt1, rlsgame, chngvle, x, y)    
        
        
class Internalth:
    
    def __init__(self):
        self.arr = []
    
    def copyofarray(self, arrayname):
        self.arr = []
        self.arr = np.copy(arrayname).astype(int)
    
    def countofgenn(self, currvalue):
        if currvalue == 1 :
            self.arr = np.append(self.arr, currvalue).astype(int)
            print(self.arr)

checks = Checks()
noiterations = 0
valueofgenxy = newarray[x1, y1]
generationncurrent = generationnnn

arrcur = Internalth()    #Making one array that will be current
arrnext = Internalth()   #Making one array that will be next generation
arrpr = Internalth()
geniter = Internalth()   #Making one array that will count the value of x1, y1 till genN


while generationncurrent > noiterations:
    
    if generationncurrent < generationnnn:
        arrcur.copyofarray(arrpr.arr)       
    else:
        arrcur.copyofarray(newarray)
        arrnext.copyofarray(newarray)
        
    for index, valueofxy in np.ndenumerate(arrcur.arr):
        x, y = index
        int(valueofxy)
        xminus1 = x - 1   #Values that are used for the numpy array views
        xplus1 = x + 1
        xplus2 = x + 2
        yminus1 = y - 1
        yplus1 = y + 1 
        yplus2 = y + 2   
        checks.switch()  #All of the internal checks  
        if (x, y) == (x1, y1):
            geniter.countofgenn(valueofxy)
            
    arrpr.copyofarray(arrnext.arr)  
    generationncurrent -= 1
    #print(generationncurrent)
print(arrcur.arr, len(geniter.arr), " - x1, y1 as green during the ", generationnnn, "iterations")
