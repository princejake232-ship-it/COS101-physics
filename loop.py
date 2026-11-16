# Function For Force
def force():
    mass = float(input("Enter mass (kg):"))
    acceleration = float(input("Enter acceleration (m/s^2):"))
    result = (mass * acceleration)
    print("Force =", result, "N")

#Function For Kinetic Energy
def kinetic_energy():
    mass = float(input("Enter mass (kg):"))
    velocity = float(input("Enter velocity (m/s):"))
    result = 0.5 * mass * velocity ** 2
    print("Kinetic energy =", result, "J")

#Function For Voltage
def voltage():
    current = float(input("Enter current (A):"))
    resistance = float(input("Enter resistance (B):"))
    result = current * resistance
    print("Voltage =", result, "V")

#Function For Potential Energy
def potential_energy():
    mass = float(input("Enter mass (kg):"))
    height = float(input("Enter height (m):"))
    gravity = 9.8
    result = mass * gravity * height
    print("Potential energy =", result, "J")

#Function For Work
def work():
    force_value = float(input("Enter force (N):"))
    distance = float(input("Enter distance (m):"))
    result = force_value * distance
    print("Work Done =", result, "J")


#Main Program
while True:
    print("\n===== PHYSICS CALCULATOR=====")
    print("1. Force")
    print("2. Kinetic Energy")
    print("3. Voltage")
    print("4. Potential Energy")
    print("5. Work")

    choice = int(input("Choose an operation (1-5): "))
    if choice == 1:
        force()
    elif choice == 2:
        kinetic_energy()
    elif choice == 3:
        voltage()
    elif choice == 4:
        potential_energy()
    elif choice == 5:
        work()
    else:
        print("Invalid choice. Please choose between 1-5")
    #Ask user if they  want to continue
    continue_program = input("Do you want to continue? (yes/no):")
    if continue_program.lower() != "yes":
        print("\n====== PHYSICS CALCULATOR=====")
        break