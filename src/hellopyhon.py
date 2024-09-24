num_1=1
num_2=1

sum = 0
i = 1
while i < 10:

    sum=sum+num_1+num_2
    num_1=num_2
    num_2=sum
    i=i+1
    print(sum)


# print(sum)