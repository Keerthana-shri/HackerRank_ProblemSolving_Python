dm= list(map(int, input().rstrip().split()))
n=dm[0]
m=dm[1]
a=(m-7)//2
b=(n//2)+1
for i in range (1,n+1):
    if i==b:        
        print('-'*a+'WELCOME'+'-'*a)
    elif(i<b):
        print('---'*(b-i)+('.|.'*(i))+('.|.'*(i-1))+('---'*(b-i)))
    else:
        print(('---'*(i-b))+('.|.'*(n-i+1))+('.|.'*(n-i))+('---'*(i-b)))