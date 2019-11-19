import time
def ABZ():
    global word
    num = 0
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in word:
        if i not in abc:
            num += 0
        else:
            num += ord(i)
    print(num)
    
word = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
start = time.time()
ABZ()
print("time:",(time.time()-start)*1000)