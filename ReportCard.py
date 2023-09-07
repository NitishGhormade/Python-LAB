# Q1 Report Card Of a Student

name = str(input("Enter you name: "))
roll = int(input("Enter your Roll Number: "))
branch = str(input("Enter Your Branch: "))
mathsMarks = int(input("Enter your Maths Marks: "))
phyMarks = int(input("Enter your Physics Marks: "))
chemMarks = int(input("Enter your Chemistry Marks: "))
percentage = (mathsMarks + phyMarks + chemMarks)/3
insentives = 0.5

if(percentage > 90):
    grade = "AA"
elif(50 < percentage < 90):
    grade = "BB"
elif(10 < percentage < 50):
    grade = "CC"
else:
    grade = "DD"

print("Name: ",name)
print("Roll: ",roll)
print("Branch: ",branch)
print("Percentage: ",percentage)
print("Grade: ",grade)
print("Percentage after adding Incentives: ",(percentage + insentives))
