problem =(input("enter your problem ").split(" "))
if problem[1] == "+" :
    print(int(problem[0]) + int(problem[2]))
elif problem[1] == "-" :
     print(int(problem[0]) - int(problem[2]))
elif problem[1] == "*" :
     print(int(problem[0]) * int(problem[2]))
elif problem[1] == "/" :
     print(int(problem[0]) / int(problem[2]))
elif problem[1] == "**" :
    print(int(problem[0]) ** int(problem[2]))         
else :
     print("go learn MATH yourself")    