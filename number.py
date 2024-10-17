number= int(input("Enter number between 100-999: "))
firstdigit = (number // 100)
seconddigit = (number // 10)%10
thirddigit = (number %10)
even_counter=0
odd_counter=0
print(thirddigit,  seconddigit, firstdigit)
if(thirddigit %2==0 ):even_counter+=1
else: odd_counter+=1
if(seconddigit %2==0):even_counter+=1
else: odd_counter+=1
if (firstdigit %2==0):even_counter+=1
else: odd_counter+=1
print("Number of even ",even_counter)
print("Number of odd",odd_counter)



