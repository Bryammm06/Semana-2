def sum_of_two_numbers(number_1, number_2):
    return number_1 + number_2

def sum2_of_two_numbers(number_1:int, number_2:int) -> int:
    return number_1 + number_2

def sum3_of_two_numbers(number_1:int = 0, number_2 = 3 ) -> int:
    return number_1 + number_2

print (sum_of_two_numbers(2,3))
print (sum2_of_two_numbers(2,3))
print (sum3_of_two_numbers(2))

#Una variable global no se puede modificar en una funcion a menos que se use el comando global

def spam():
    global eggs     #Declare that we're modifying the global variable
    eggs = "spam"   #This changes the global variable

eggs = "global"
spam()              #Function modifies global variable
print(eggs)
