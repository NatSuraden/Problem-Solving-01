#def Factorial():
    #global N
    #num = 1
    #for i in range(1,N+1):
        #num = num * i
    #print(num)
def Factorial2(N):
    global aNFactorial
    if N > 1:
        aNFactorial = N * Factorial2(N-1)
        return aNFactorial    
    else:
        aNFactorial = 1
        return aNFactorial    
N = int(input("Enter :"))
Factorial2(N)
print(aNFactorial)


