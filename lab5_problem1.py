# ==================================================
# IT 2750 - Scripting Fundamentals for Cybersecurity
# Cuyahoga Community College
# Lab 5 – Problem 1
# ==================================================
# Student Name: Zachary Ratliff
# Student Email: zachary.ratliff@tri-c.edu
# ==================================================

def main():  # DO NOT EDIT THIS LINE

    print("Welcome to the String Tester!")

    # PART A
    # ======
    # Create two variables, string1 and string2. The variable string1 should read
    # ABCDEFG and string2 should read TUVWXYZ. Print each variable to the screen
    # using individual print statements

    string1 = "ABCEDFG"
    string2 = "TUVWXYZ"
    print(string1)
    print(string2)
    # PART B
    # ======
    # Iterate through each character in string1 and print each character to a new
    # line using print statements

    for char in string1:
        print(char)

    # PART C
    # ======
    # Iterate through each character in string1 and print each character to a new
    # line using print statements

    for char in string2:
        print(char)

    # PART D
    # ======
    # Swap the odd characters in string1 with the odd characters in string2 and
    # print string1 and string2 to the screen (using 2 print statements)
    string1_list = list(string1)
    string2_list = list(string2)

    for i in range(1, len(string1_list), 2):
        string1_list[i], string2_list[i] = string2_list[i], string1_list[i]

    string1 = ''.join(string1_list)
    string2 = ''.join(string2_list)

    print(string1)
    print(string2)
    # PART E
    # ======
    # Combine the two strings into one variable called string3. For each character,
    # if the value is a letter between A and M (inclusive), change the letter to the
    # next letter to the right. If the value is a letter between N and Z (inclusive),
    # change the value of the character to the letter to the left. Save to the
    # string3 variable and print the value of that variable to the screen.

    combinedstring = string1 + string2
    string3 = ""

    for char in combinedstring:
        if "A" <=char <= "M"
            string3 += chr(ord(char) + 1)
        elif "N" <= char <= "Z":
            string3 += chr(ord(char) - 1)
        else:
            string3 += char
    print(string3)

    # PART F
    # ======
    # Reverse the value of string3 and print it to the screen

    reverse_string3 = string3[::-1]
    print(reverse_string3)

    return  # DO NOT EDIT THIS LINE

if __name__ == "__main__":  # DO NOT EDIT THIS LINE
    main()                  # DO NOT EDIT THIS LINE
