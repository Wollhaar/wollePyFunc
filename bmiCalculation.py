#Defining function
def bmi(weight, height):
  index = weight / (height * height)
  return index  #sends the return value back

def notification_bmi(bmi):
  if bmi < 18.5:
    print("underweight")
  elif bmi > 27:
    print("overweight")
  else:
    print("good shape")
  print("BMI is by ", bmi)

#todo: make script dynamic. calculate by input
#todo: record input + calculation
#Calling function and using return value
#first patient
patient_5 = bmi(61, 1.83) #stores return value
notification_bmi(patient_5)

#second patient
patient_7 = bmi(75, 1.74)
notification_bmi(patient_7)

#third patient
patient_9 = bmi(70, 1.60)
notification_bmi(patient_9)