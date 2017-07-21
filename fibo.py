
global steps
steps = 0
def fibo(n):
    global steps
    steps += 1
    if n <= 2:
        return 1
    return fibo(n-1) + fibo(n-2)
for i in range(20):
    steps = 0
    print(str(i) + ' ' + str(fibo(i)) + ' ' + str(steps))

print(fibo(5))
