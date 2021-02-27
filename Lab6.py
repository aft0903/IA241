#Lab6 
#Aileen Towner

#3.1
for i in range(6):
    if(i!=3):
        print(i)
#3.2
multiply = 0
for i in range (1,6):
    multiply= multiply *i
print (multiply)

#3.3
add =0
for i in range (1,6):
    add= add+ i
print(add)

#3.4
result = 0

for i in range (3,9):
    result= result *i
print (result)

#3.5
result = 1
for i in range (4,9):
    result = result *i
print (result) 

#3.6
result =0 
for word in "this is my 6th string".split():
    print(word)
    result = result + 1
print(result)

#3.7
my_tweet = { 
    "favorite_count":1138, 
    "lang": "en",
    "coordinates": (-75,40),
    "entities": {"hashtags":["Preds", "Pens", "SingIntoSpring"]}
    }
result = 0
for hashtag in my_tweet['hashtags'] ['entities']:
    result=result+1
print(result)

