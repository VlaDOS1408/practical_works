#14 Version
#First Problem

def count_divisors(num):
    count = 0
    
    if num < 0:
        num = num - num*2
    #print("Num: "+str(num))

    for i in range(1, num+1):
        if num % i == 0:
            #print(i)
            count += 1

    return count;

startIntervalNum = None;
endIntervalNum = None;
numWithMostDivisors = 0;
numsWithMostDivisors = [numWithMostDivisors];


while startIntervalNum == None:
    try:
        startIntervalNum = int(input("Enter start interval num: "))
    except:
        print("\nUncorrect value!")

while endIntervalNum == None:
    try:
        endIntervalNum = int(input("Enter end interval num: "))
        if endIntervalNum < startIntervalNum:
            endIntervalNum = None
            raise;
    except:
        print("\nUncorrect value!")


for i in range(startIntervalNum, endIntervalNum+1, 1):
    divisors = count_divisors(i)

    if divisors > count_divisors(numWithMostDivisors):
        numWithMostDivisors = i
        numsWithMostDivisors = [i]
    elif divisors == count_divisors(numWithMostDivisors):
        numsWithMostDivisors = numsWithMostDivisors + [i]

print(f'''
\nNumbers with most natural divisors = {numsWithMostDivisors}
Count of divisors num in range {startIntervalNum} - {endIntervalNum} = {count_divisors(numWithMostDivisors)}
\n''')
input()