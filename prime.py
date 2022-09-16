# Calculate the sum of prime numbers below 100:
for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0:
            print("Not prime")
            break
    else:
        print(i)
