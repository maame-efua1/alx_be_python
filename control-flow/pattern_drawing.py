length = int(input("Enter the size of the pattern: "))
i = 0  # row counter

while i < length:   # Outer loop for rows
    # Print asterisks
    j = 0
    while j < (4):
        print("*", end=" ")
        j += 1

    print()   # Move to next line after each row
    i += 1