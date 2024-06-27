def input_array(input_text):
    numbers = []
    try:
        numbers = input(input_text).split()
            
        for i in range(0, len(numbers), 1):
            numbers[i] = int(numbers[i])
    except:
        print("Uncorrect input!")
        numbers = []
            
    return numbers;

numbers = []
interval = [1, 2, 3]
numbers_in_interval = []

while len(numbers) != 3:
    numbers = input_array("Enter 3 numbers: ")
    
    if len(numbers) != 3:
        print("Enter 3 numbers!\n")
    
for interval_el in interval:
    for el in numbers:
        if el == interval_el:
            numbers_in_interval.append(el)
            
if len(numbers_in_interval) > 0:
    for el in numbers_in_interval:
        print(f"Number in interval {interval} - {el}")
else:
    print(f"None of the entered numbers are in the range {interval}")
    
input()