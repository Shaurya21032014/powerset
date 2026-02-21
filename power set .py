import math;

def printPowerSwt(set, SetSize):
    powersetsize = (int) (math.pow(2 , SetSize));
    outer = 0;
    inner = 0;

    for outer in range(0, powersetsize):
        for inner in range(0, SetSize):


            if((outer & (1 << inner )) > 0):
                print(set[inner],end = "")
        print("")


size = int(input("enter arry size"))

set = []
for i  in range(0,size):
    n = int(input("enter element"))
    set.append(n)

printPowerSwt(set, len(set))