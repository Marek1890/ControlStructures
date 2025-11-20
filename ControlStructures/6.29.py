N = int(input("How many primes: "))
count = 0
num = 2
while count < N:
    ok = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            ok = False
            break
    if ok:
        print(num, end=" ")
        count += 1
    num += 1
