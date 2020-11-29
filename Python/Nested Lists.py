if __name__ == '__main__':
    score_set = set()
    students = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_set.add(score)
        students.append([name, score])
        
    second_lowest = sorted(score_set)[1]
    names = list()
    for i in students:
        if i[1] == second_lowest:
            names.append(i[0])
    names.sort()
    for i in names:
        print(i)
