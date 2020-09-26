# Python list VS tuple memory use

# example-1
Tuple = (1,2,3,4,5,6,7,8,9,0,78,34,43,32,43,55,54,212,642,533,43434,54532)  
List = [1,2,3,4,5,6,7,8,9,0,78,34,43,32,43,55,54,212,642,533,43434,54532]  
print('Tuple size =', Tuple.__sizeof__())     
print('List size =', List.__sizeof__())  