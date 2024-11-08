if __name__ == '__main__':
    N = int(input())
    A=[]
    for i in range(0,N):
        check=input().split()
        if check[0] == "insert":
            A.insert(int(check[1]),int(check[2]))
        elif check[0] == "append":
            A.append(int(check[1]))
        elif check[0] == "pop":
            A.pop()
        elif check[0] == "print":
            print(A)
        elif check[0] == "remove":
            A.remove(int(check[1]))
        elif check[0] == "sort":
            A.sort()
        else:
            A.reverse()