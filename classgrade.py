total = (int(input("how many students in the class?")))
grades = [] 
for x in range(total):
    element = int(input(f"student number {x+1}: "))
    grades.append(element)

sumOfGrades = sum(grades)
averageScore = sumOfGrades/total
print("average is ", averageScore)
if averageScore >90:
        print("grade is A")
elif averageScore >80:
        print("grade is B")
else:
        print("grade is F")