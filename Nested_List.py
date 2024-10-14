if __name__ == '__main__':
    students_grade=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students_grade.append([name,score])
    Uni_list = sorted(list(set(x[1] for x in students_grade)))
    second_lowest= Uni_list[1]
    low_stu=[]
    for i in students_grade:
        if second_lowest== i[1]:
            low_stu.append(i[0])
    for i in sorted(low_stu):
        print(i)
    
