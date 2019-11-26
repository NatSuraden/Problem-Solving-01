import time
def ABZ():
    global word
    num = 0
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in word:
        if i not in abc:
            num += 0
        else:
            if i == "A":
                num += 65
            elif i =="B":
                num += 66
            elif i == "C":
                num += 67
            elif i =="D":
                num += 68
            elif i =="E":
                num += 69       
            elif i =="F":
                num += 70
            elif i =="G":
                num += 71
            elif i =="H":
                num += 72
            elif i =="I":
                num += 73
            elif i =="J":
                num += 74
            elif i =="K":
                num +=  75
            elif i =="L":
                num += 76
            elif i =="M":
                num += 77
            elif i =="N":
                num += 78
            elif i =="O":
                num += 79
            elif i =="P":
                num += 80
            elif i =="Q":
                num += 81
            elif i =="R":
                num += 82
            elif i =="S":
                num += 83
            elif i =="T":
                num += 84
            elif i =="U":
                num += 85
            elif i =="V":
                num += 86
            elif i =="W":
                num += 87
            elif i =="X":
                num += 88
            elif i =="Y":
                num += 89
            elif i =="Z":
                num += 90
    print(num)
    
word = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
start = time.time()
ABZ()
print("time:",(time.time()-start)*1000)
