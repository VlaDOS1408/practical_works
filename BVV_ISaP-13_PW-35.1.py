#14 Version
#First Problem

def count_divisors(num):
    count = 0
    #print("Num: "+str(num))

    for i in range(1, num+1):
        if num % i == 0:
            #print(i)
            count += 1

    return count;

startIntervalNum = None;
endIntervalNum = None;
numWithMostDivisors = 1;
numsWithMostDivisors = [1];


while startIntervalNum == None:
    try:
        startIntervalNum = int(input("Enter start interval num: "))
    except:
        print("\nUncorrect value!\n")

while endIntervalNum == None:
    try:
        endIntervalNum = int(input("Enter end interval num: "))
    except:
        print("\nUncorrect value!\n")


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