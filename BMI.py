weight=int(input("please enter your weight in kilograms: "))
height=int(input("please enter your height in meters: "))
BMI=float(weight/((height/100)**2))
print(BMI)

if 0 <BMI < 18.5:
 print(f'Your BMI {round(BMI, 2)} is less than 18.5 which is too light')
elif 18.5 <= BMI < 25:
 print(f'Your BMI {BMI} is between 18.5 and 25 which is normal')
elif 25 <= BMI < 27:
 print(f'Your BMI {BMI} is between 24 and 27 which is overweight')
elif 27 <= BMI < 30:
 print(f'Your BMI {BMI} is between 27 and 30 which is mild obesity')
elif 30 <= BMI < 35:
 print(f'Your BMI {BMI} is between 30 and 35 which is moderate obesity')
elif 35 <= BMI:
 print(f'Your BMI {BMI} is greater >=35 which is severe obesity')
else:
 print("Your BMI is less than zero")