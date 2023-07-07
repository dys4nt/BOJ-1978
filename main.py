pli = []

for i in range(2,1001):
    isPrime = True
    for j in range(2,31):
        if i%j==0 and i//j!=1:
            isPrime = False
            break
    if isPrime:
        pli.append(i)

n = input()
li = list(map(int,input().split()))
res = 0

for i in range(len(li)):
    if li[i] in pli:
        res += 1

print(res)