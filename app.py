Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import math
... 
... print("HEAT CONDUCTION CALCULATOR")
... print("1. Plane Wall")
... print("2. Cylinder")
... print("3. Sphere")
... 
... choice = int(input("Choose geometry: "))
... 
... k = float(input("Thermal conductivity k (W/mK): "))
... T1 = float(input("Hot temperature (°C): "))
... T2 = float(input("Cold temperature (°C): "))
... 
... if choice == 1:
...     A = float(input("Area (m²): "))
...     L = float(input("Thickness (m): "))
... 
...     Q = k * A * (T1 - T2) / L
... 
... elif choice == 2:
...     L = float(input("Length (m): "))
...     r1 = float(input("Inner radius (m): "))
...     r2 = float(input("Outer radius (m): "))
... 
...     Q = 2 * math.pi * k * L * (T1 - T2) / math.log(r2 / r1)
... 
... elif choice == 3:
...     r1 = float(input("Inner radius (m): "))
...     r2 = float(input("Outer radius (m): "))
... 
...     Q = 4 * math.pi * k * (T1 - T2) / (1/r1 - 1/r2)
... 
... else:
...     print("Invalid choice")
...     exit()
... 
... print(f"\nHeat Transfer Rate = {Q:.2f} W")
