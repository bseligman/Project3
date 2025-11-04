#Programming Project 03 written by Benjamin Seligman, pledged

'''
OnewayAirfare Program
Imagine you run a small airline that offers flights between N different cities, and actually you offer a
direct flight from every city to every other city. The price policy of the marketing department is to
choose a price uniformly at random from the set of prices {19, 29, 39, 49, 59, 69} for each (one-way) flight
leg. That is, it is as if you determined the price for a leg by rolling a 6-sided die that shows the above
price values. An example flight map for N = 5 is visualized by the complete digraph in Figure 1.
Write a program that takes three integers N, s, and t as input from the command line (as command
line arguments), where N represents the number of cities served, s represents the index of the start city
of the customer, and t represents the index of the target city of the customer. Assume that the cities
are numbered from 0 to N − 1. You should verify the following constraints for your input values:
 The number of cities should be between 3 and 100, that is 3 ≤ N ≤ 100.
 The index of the start city s must be valid, that is 0 ≤ s ≤ N − 1. (Since we start the numbering
of the cities at 0, there will not be a city numbered N.)
 The index of the target city t must be valid, that is 0 ≤ t ≤ N − 1.
If one of the above constraints is violated, you program should terminate immediately indicating the
details of the incorrect input.
If all inputs are valid, then randomly generate a price matrix for every (one-way) flight leg you offer.
For example, for N = 5, the random price matrix might look like this (this matrix is visualized in
Figure 1)
'''

### IMPORTS
import random
import sys


### ADD SPECIFIC ERRORS!
'''
Zybook section 8.10 explains how to use command-line arguments. The three input values will
be stored as strings in args[1], args[2], and args[3].
 Use a list of lists to represent the price matrix. See zyBook section 8.5 for details how to create
a multi-dimensional data structure; in this case we need a two-dimensional structure'''

### VARS
PriceChooseFrom = [19, 29, 39, 49, 59, 69]
## N, Cities Served
# If not between 3 -> 100, terminates
citiesServed = int(sys.argv[1])
startingCity = int(sys.argv[2])
endingCity = int(sys.argv[3])

if(citiesServed < 3) or (citiesServed > 100):
    sys.exit(0)
## S, Index of starting City of Customer
# If not between 0 and N -1, terminates
if(startingCity < 1) or (startingCity > citiesServed):
    sys.exit(0)
# T, Target index of City, of Customer
# If not between 0 and N-1, terminates
if(endingCity < 1) or (endingCity > citiesServed):
    sys.exit(0)

### FUNCTIONS
#Generate Matrix from inputs
def matrixGen(N,S,T):
    TheMatrix = []
    for i in range(0,N):
        NewMatrix = []
        for b in range(0,N):
            NewMatrix.append(PriceChooseFrom[random.randint(0,5)])
        TheMatrix.append(NewMatrix)
    return(TheMatrix)
#Matrix print Function
def matrixPrint(matrix):
    MatrixLen = len(matrix)
    for i in range(0,MatrixLen):
        if(i==0):
            print("   a" + str(i), end=" ")
        else:
            print("a" + str(i), end=" ")
    print("\n", end="")
    for i in range(len(matrix)):
        for b in range(len(matrix)):
            print(matrix[b][i],end=",")
        print("\n")

        '''
        line = str(matrix.index(items))
        print("d" + line, end=" ")
        for itemstwo in items:
            print(str(itemstwo), end=" ")
        print("\n", end="")
        '''
#Find Lowest of Values in a list of lists
def findLowestLisOfLis(themainlist):
    least = themainlist[0]
    for i in range(len(themainlist)-1):
        if(themainlist[i]!=0):
            if(themainlist[i+1] < themainlist[i]):
                least=themainlist[i+1]
    return(least)
#Matrix Add Up Function
def matrixFindRowValue(matrix,a,d):
    #print(matrix)
    stored_paths = []
    prices_and_rows = []
    avalue = 0
    for items in matrix:
        row=[]
        #find starting point
        if matrix.index(items) == a:
            for itemsofthelist in items:
                #for locations being stored for carryovers
                stored_paths.append(items.index(itemsofthelist))
                #for values themselves, yes I could've used dictionary but I just prfer 2 lists
                row.append(itemsofthelist)
                print(print("row:",row))
                #TESTING GROUNDS
                #If last listed flight is not the destination city, shift over another flight to that city
                if(itemsofthelist == items[-0]):
                    if(itemsofthelist != d):
                        print((matrix[matrix.index(items)+1][-1]))
                        row.append(matrix[matrix.index(items)+1][-1])
        prices_and_rows.append(sum(row))
        lowestprice = findLowestLisOfLis(prices_and_rows)
    print("test:",prices_and_rows)
    return(lowestprice)
def matrixFindDiagnolRowValue(matrix,a,d):
    prices_and_rows = []
    avalue = 0


### MAIN
mymatrix = matrixGen(citiesServed, startingCity, endingCity)
matrixPrint(mymatrix)
print(matrixFindRowValue(mymatrix,2,2))