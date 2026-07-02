import numpy as np

while True:
    print("Select your gender")
    print("1. Male")
    print("2. Female")

    try:
        gender = int(input("Choice (1/2): "))
        if gender not in [1,2]:
            print("Invalid choice")
            continue
        if gender == 1:
            while True:
                try:
                    distance = 