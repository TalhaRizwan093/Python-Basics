#program that reads three edges for a triangle and computes the perimeter if the input is valid. Otherwise, display that the input is invalid

#Promtes user to value of edges of a triangle
e1, e2, e3 = eval(input("Enter thee edges of a triangle:"))

#Valid computation of peremiter
if e1 + e2 > e3 and e1 + e3 > e2 and e2 + e3 > e1:
    print("The perimeter is:",e1 + e2 + e3)
else:
    print("Invalid input")
