pnum=24
i=3
print("You have 3 chance to enter correct number: ")

while(i>0):
    num=int(input('Enter a no.: '))
    if(num==pnum):
        print("You win")
        break
    else:
        print('Enter wrong number')
i=i+1
