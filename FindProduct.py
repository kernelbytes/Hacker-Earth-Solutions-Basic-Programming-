answer=1
n = int(input())
x = [int(i) for i in input().split()]
for i in range(0,n):
    answer=(answer*x[i])%(10**9 +7)    
print(answer)
