#Aileen Towner
#IA 241
#Lab 8 

#3.1

def count_words (input_str):
    
    return len(input_str.split())
    
# TEST: print(count_words('a string'))

#3.2
demo_str = 'hello world'
print(count_words(demo_str))

#3.3

def min_num (num_list): #function
    
    min_item = num_list[0] #define variables 
    
    for num in num_list:  #for every number in the list 
        if type(num) is not str: 
            if min_item >= num:# if the variable is less than the number as it goes thru the list             min_item = nu
                min_item = num
    return (min_item)
    
#3.4
demo_list = [1,2,3,4,5,6]
print(min_num(demo_list))


#3.5 
mix_list = [1,2,3,4,'a',5,6]
print(min_num(mix_list))
