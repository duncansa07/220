"""
Name: Scarlett Duncan
lab2.py
Problem: Create codes using for loops to calculate root-mean-square average, harmonic average, and geometric average.
Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
def means():
    value_amt = eval(input("Enter the number of values to be entered: "))

    rms_acc = 0
    harmonic_acc = 0
    geometric_acc = 1

    for i in range(value_amt):
        value = eval(input("enter value"))
        rms_acc += value**2
        harmonic_acc += (1/value)
        geometric_acc *= value
    rms_average = (rms_acc/value_amt)**(1/2)
    rms_avg = round(rms_average, 3)
    harmonic = (value_amt/harmonic_acc)
    harmonic_mean = round(harmonic, 3)
    geometric = geometric_acc**(1/value_amt)
    geometric_mean = round(geometric, 3)
    print("The RMS Average is:", rms_avg)
    print("The harmonic mean is:", harmonic_mean)
    print("The geometric mean is:", geometric_mean)
