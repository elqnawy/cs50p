sentence =input("enter your sentence in camel case ")
def conv(word) :
    result=""
    for l in word :        
        if l.isupper():
            l = "_"+ str(l.lower())
            result =result + l
        else:
            result =result + l
    return result  
      
       
print(conv(sentence))