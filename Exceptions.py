A = int(input())
for i in range(A):
    try:
        x, y = map(int, input().split())
        print(x//y)
    except Exception as e:
        print("Error Code:",e)