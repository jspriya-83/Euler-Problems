num=raw_input("enter the power of two you want to calculate:")

power=int(num)

longnum=2**power

#finding the sum of digits of num

strnum=str(longnum)

print(strnum)

sum=0
length=len(strnum)
print("No of digits:", length)

for i in range(length):
    #print(strnum[i])
    sum=sum+int(strnum[i])

print("sum:",sum)



