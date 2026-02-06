total = (int(input("how many students in the class?")))
grades = [] 
for x in range(total):
    element = int(input(f"student number {x+1}: "))
    grades.append(element)

SUM = sum(grades)
AV = SUM/total
print("average is ", AV)
if AV >90:
        print("grade is A")
elif AV >80:
        print("grade is B")
else:
        print("grade is F")