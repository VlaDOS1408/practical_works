#PW 39
#Problem 1

def input_array(input_text):
    numbers = []
    try:
        numbers = input(input_text).split()
        
    except:
        print("Uncorrect input!")
        numbers = []
            
    return numbers;

input_list = []
duplicates = []

while len(input_list) < 1:
    input_list = input_array("Enter array: ")
    
for el in input_list:
    if input_list.count(el) > 1 and el not in duplicates:
        duplicates.append(el)
        
if len(duplicates) > 0:
    print(f"Dublicates: {duplicates}")
else:
    print("List don't have dublicates")
    
input("\nContinue ->")
#PW 39
#Problem 2

def input_int_array(input_text):
    numbers = []
    try:
        numbers = input(input_text).split()
            
        for i in range(0, len(numbers), 1):
            numbers[i] = int(numbers[i])
    except:
        print("Uncorrect input!")
        numbers = []
            
    return numbers;

input_list = []
exit_list = []

while len(input_list) < 1:
    input_list = input_int_array("Enter int list: ")
    

for i in input_list:
    if i % 2 == 0:
        exit_list.append(i)
        
exit_list.reverse()

print(f"Exit list: {exit_list}")