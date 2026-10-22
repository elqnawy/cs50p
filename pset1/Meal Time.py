t =input("What time is it ")

if ":" not in t:
    t = t + ":00"
else :
    t =t    

t =t.split(":")

Hours =int(t[0])
Mins =int(t[1]) / 60
timy = Hours + Mins
def main():

    convert(timy)

def convert(t):
    if 7 <= t <= 8 :
        print("its breakfast time")
    elif 12 <= t <= 13 :
        print("its lunch time")   
    elif 18 <= t <= 19 :
        print("its dinner time") 
    else :
         return    


if __name__ == "__main__":
    main()