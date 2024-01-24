#Print multiplication table from 1 to 10
range_of_numbers = [1,2,3,4,5,6,7,8,9,10]

for i in range (10):
    if i == 1:
        for j in range (1, 11):
            print (i*j, end=' ')
            
