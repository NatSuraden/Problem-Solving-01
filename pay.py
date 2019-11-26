def Calc(Principal,Interest,Years,Time):
    Amount = Principal*(1+(Interest/Time))**(Years*Time)
    display(Amount,Principal,Interest,Years,Time)
def Read(Principal,Interest,Years,Time):
    Interest = Interest/100
    Calc(Principal,Interest,Years,Time)
def display(Amount,Principal,Interest,Years,Time):
    print("Principal",Principal,"Interest",Interest,"Years",Years,"Time",Time,"Amount",Amount)
def main():
    Principal = int(input("Enter Principal :"))
    Interest = int(input("Enter Interes :"))
    Time = int(input("Enter Time :"))
    Years = int(input("Enter Years :"))
    Read(Principal,Interest,Years,Time)
main()
