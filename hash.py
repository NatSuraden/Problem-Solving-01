import random
namelist = ["","","","","","","","","",""]
doit = "Y"
def get_in_the_list(keys,val,num):
    global namelist
    Data = {keys:val}
    if namelist[num] == "":
        namelist[num]=Data
    else:
        count = -1
        for i in namelist:
            count+= 1
            if i == "":
                namelist[count] = Data
                break     
    return namelist
def nathash():
    global namelist
    n = random.randint(0,9)
    #while namelist[n] != "":
        #n = random.randint(0,9)
    return n
while doit == "Y":
    keys = input("Enter your name :")
    val = input("number ID :")
    num = nathash()
    print(get_in_the_list(keys,val,num))
    doit = input("want more(Y = Yes,N = No)")






    

