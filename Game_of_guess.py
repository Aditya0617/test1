import random as rd

st=rd.randint(0,10)
ch=3
print("Guess the number b/w 0-10")

while ch>=0:
    ch-=1
    x=int(input("Enter a ur guess:"))

    if ch>0:
        if x==st:
            print("Your guess is correct :)")
            break
        
        else:
            print("Wrong guess!!","\nchoices left:-",ch,"\n**---------***---------***---------**")    


    elif ch==0:
        print("Sorry! Out of choices\nBetter Luck Next Time :)")
        print("The number was:",st)
        break

    
    




