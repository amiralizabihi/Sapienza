if __name__ == '__main__':
    records = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    
    unique_scores = sorted(set([score for name, score in records]))
    second_lowest_score = unique_scores[1]
    students_with_second_lowest = [name for name, score in records if score == second_lowest_score]
    for student in sorted(students_with_second_lowest):
        print(student)
