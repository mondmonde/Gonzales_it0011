science = int(input("Enter science grade: "))
math = int(input("Enter math grade: "))
english = int(input("Enter english grade: "))
g = (math + science + english)/3
print ("Average is: ", g)
if g >= 70:
    print ("passed")
else:
    print("failed")
    