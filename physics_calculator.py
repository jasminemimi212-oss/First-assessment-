# This program calculates different physics formulas based on user selection

import math

# Note: Formula Reference
# a = Wave Speed (v = fλ)
# b = Period (T = 1/f)
# c = Lens Formula (1/f = 1/v + 1/u)
# d = Refractive Index (n = c/v)
# e = Mass-Energy Equivalence (E = mc²)

print("Welcome to Physics Formula Calculator")
print("=====================================")
print()
print("FORMULA REFERENCE:")
print("a - Wave Speed (v = fλ)")
print("b - Period (T = 1/f)")
print("c - Lens Formula (1/f = 1/v + 1/u)")
print("d - Refractive Index (n = c/v)")
print("e - Mass-Energy Equivalence (E = mc²)")
print()
print("=====================================")

# main loop for the program
while True:
    print()
    print("Select which formula you want to calculate:")
    print("a - Wave Speed")
    print("b - Period")
    print("c - Lens Focal Length")
    print("d - Refractive Index")
    print("e - Mass-Energy")
    print("q - Quit program")
    print()
    
    # get user choice
    choice = input("Enter your choice: ")
    
    # check if user wants to quit
    if choice == 'q' or choice == 'Q':
        print("Thank you for using this calculator!")
        break
    
    # option a - calculate wave speed
    if choice == 'a' or choice == 'A':
        print()
        print("Wave Speed Calculation (v = fλ)")
        print("--------------------------------")
        # get inputs from user
        f = float(input("Enter frequency in Hz: "))
        wavelength = float(input("Enter wavelength in meters: "))
        # calculate wave speed
        v = f * wavelength
        # show result
        print("Wave Speed = " + str(v) + " m/s")
        print()
    
    # option b - calculate period
    elif choice == 'b' or choice == 'B':
        print()
        print("Period Calculation (T = 1/f)")
        print("----------------------------")
        # get input
        f = float(input("Enter frequency in Hz: "))
        # calculate period
        T = 1 / f
        # display result
        print("Period = " + str(T) + " s")
        print()
    
    # option c - calculate lens focal length
    elif choice == 'c' or choice == 'C':
        print()
        print("Lens Formula (1/f = 1/v + 1/u)")
        print("------------------------------")
        # get image distance and object distance
        v = float(input("Enter image distance in cm: "))
        u = float(input("Enter object distance in cm: "))
        # calculate focal length
        f = 1 / ((1/v) + (1/u))
        # print answer
        print("Focal Length = " + str(f) + " cm")
        print()
    
    # option d - calculate refractive index
    elif choice == 'd' or choice == 'D':
        print()
        print("Refractive Index Calculation (n = c/v)")
        print("--------------------------------------")
        # speed of light
        c = 299792458
        print("Speed of light c = 299,792,458 m/s")
        # get speed in medium
        v = float(input("Enter speed of light in medium in m/s: "))
        # calculate refractive index
        n = c / v
        # show answer
        print("Refractive Index = " + str(n))
        print()
    
    # option e - calculate mass-energy
    elif choice == 'e' or choice == 'E':
        print()
        print("Mass-Energy Equivalence (E = mc²)")
        print("---------------------------------")
        # get mass
        m = float(input("Enter mass in kg: "))
        # speed of light
        c = 299792458
        print("Speed of light c = 299,792,458 m/s")
        # calculate energy
        E = m * (c ** 2)
        # display result
        print("Energy = " + str(E) + " J")
        print("Energy = " + str(E) + " Joules (that's a LOT of energy!)")
        print()
    
    # if user enters wrong option
    else:
        print()
        print("Invalid choice! Please select a, b, c, d, e, or q")
        print()