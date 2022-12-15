num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

for num in range(num1, num2+1):
    isPrime = False
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                isPrime = False
                break
            isPrime = True
    if isPrime:
        print(num)
