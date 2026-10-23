

account =0

while account < 50:
        print(f"Amount Due {50 - account}")
        amount =int(input("put your coin "))
        if amount == 25:
            account += 25
        elif amount == 10:
            account += 10   
        elif amount == 5:
            account += 5
        else :
            print("not accepted coin") 
          

print(f"Change Owed {account - 50}")         
account = 0
print("Here is your coke!")        
 