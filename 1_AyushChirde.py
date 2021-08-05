def numberOfDivisors(num):
    c = 0
    for i in range(1, num + 1) :
        if (num % i == 0) :
            c += 1
         
    return c
def countNumbers(n):
    c = 0
    for i in range(1, n + 1) :
        if (numberOfDivisors(i) > 3):
            c += 1
    return c
if __name__ == "__main__":
    n = int(input())
    if n>0:
        print(countNumbers(n))
    else:
        print('Please Provide valid Positive Valid integer')