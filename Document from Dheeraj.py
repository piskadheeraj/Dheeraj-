balance =10000
print("Welcome to the atm!!")
print("Your balance is ",balance)
while balance >0 :
    amount = int(input("enter the amount to withdrawl :\t"))
    if amount ==0 :
        print("Thank you for using the atm !!")
        break
    elif amount > balance :
        print("In suficient balance !!. Try smaller amount")
    else :
        balance -= amount
        print( "withdrawl is successfull !! :$",balance)
if balance == 0:
        print("There is no balance is left .thank you")
