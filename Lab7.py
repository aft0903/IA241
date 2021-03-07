#Aileen Towner
#Lab 7 

#3.1
i=0
while i<=5:
    if i !=3:
        print (i)
    i=i+1
#3.2
i=1
factorial = 1
while i<=5:
      factorial=factorial*i
      i=i+1

print(factorial)


#3.3
i=0
sum=0
while i<=5:
    sum = sum+i
    i=i+1
    
print(i)

#3.4
i=3
result = 1

while i <= 8:
    result =result*i
    i=i+1
    
print (result)

#3.5
i=4
result = 1
while i<=8:
    result=result*i
    i = i +1
    
print(result)

#3.6
num_list = [12,32,43,35]
while num_list:
    num_list.remove(num_list[0])
print (num_list)
