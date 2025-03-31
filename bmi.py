weight_pounds = float(input("Enter weight in pounds: "))

#prompt the user to enter height in feet and inches
feet = int(input("Enter feet: "))
inches = int(input("Enter inches: "))

#Calculate height in inches
height_inches = feet * 12 + inches

#Calcuate BMI
bmi = weight_pounds * 0.4539237 / ((height_inches * 0.0254) * (height_inches * 0.0254))

#BMI display
print("BMI is", bmi)

#Display Output
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
