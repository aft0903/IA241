#Aileen Towner
#Lab 9 

#3.1

class my_stat: #define class

    def sigma (self, m,n): 
        
        result= 0
        
        for i in range (n, m+1): 
            result = result+i
        return result 


    def pi (self, m,n): 
        result = 1
      
        for i in range (n, m+1): 
            result = result*i
        return result 
    
        
    def factorial (self, m): 
         
        if m == 0: 
            return 1
        else:
            return m * self.factorial(m-1)
        
    def permutation (self, m, n): 
        return self.factorial(m)/self.factorial(m-n)
        
#3.2

my_cal = my_stat()

print(my_cal.sigma(5,3))

print(my_cal.pi(5,3))

print(my_cal.factorial(5))

print (my_cal.permutation(5,2))

