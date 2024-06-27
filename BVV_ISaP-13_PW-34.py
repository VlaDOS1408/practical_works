import random

def OneProgramm():
    try:
        potatoCost = int(input("Enter potato cost of the kg: "))
    except:
        print("Uncorrect value")
        return;

    preCommTxt = "\t"
    print("Table of the cost potatoes on kg")
    for i in range(1, 11, +1):
        print(f"{i}kg" + "\t*" + str(potatoCost) +"\t=\t" + str(potatoCost*i))
    

def TwoProgramm():
    rnd = random.randint(2, 12)
    numbers = []
    
    while numbers == []:
        try:
            numbers = input("Enter array: ").split()
            
            for i in range(0, len(numbers), 1):
                numbers[i] = int(numbers[i])
        except:
            print("Uncorrect value!")
            numbers = []

    
    # for i in range(1, rnd, 1):
    #     numbers += [random.randint(1, 10)];
    count = 0
    summ = 0
    
    for i in numbers:
        count += 1
        summ = summ + i
    print(f"\nSum of numbers = {summ}\nCount of numbers = {count}\n\nThere nums is = {numbers}\n")

while True:
    answer = input("Choose programm:\n1.One\n2.Two\n3.Exit\n>>> ")
    answer = answer.lower()
    
    if answer == "one" or answer == "1":
        OneProgramm()
    elif answer == "two" or answer == "2":
        TwoProgramm()
    elif answer == "exit" or answer == "3":
        exit();
    else:
        print("Uncorrect input\n\n")
    