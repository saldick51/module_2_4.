numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Primes = []
Not_Primes = []
for i in numbers:
    is_=True
    if i > 1:
        for j in range(2,i):
            if i%j == 0:
                is_ = False
                break
        if is_ == True:
            Primes.append(i)
        else:
            Not_Primes.append(i)
print(Primes)
print(Not_Primes)
