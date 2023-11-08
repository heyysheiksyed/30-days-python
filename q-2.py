words=[]
for i in range(0,5):
    a=input("") 
    words.append(a)    
for i in range(0,5):
    if(i!=4):
        print(words[i],end=" ") 
    else:
        print(words[i]+".")
