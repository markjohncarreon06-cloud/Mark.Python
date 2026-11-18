# ==========================================
#          PYTHON LEARNING ACADEMY
#       LEARN - EXAMPLE - PRACTICE
# ==========================================

print("==========================================")
print("          PYTHON LEARNING ACADEMY")
print("==========================================")

name = input("Enter your name: ")

print("\nWelcome to Python Learning Academy,", name)
print("Let's start learning Python!")

while True:

    print("\n==========================================")
    print("   MAIN BASIC PYTHON PROGRAMMING LESSON")
    print("==========================================")
    print("1. Python Basic Syntax")
    print("2. Printing Output")
    print("3. Python Comments")
    print("4. Variables and Constants")
    print("5. Basic Data Types")
    print("6. Arithmetic Operators and Expressions")
    print("7. Basic Input and Output")
    print("8. Conditional Statements")
    print("9. Logical Operators")
    print("10. Introduction to Iteration and Loops")
    print("11. Python Knowledge Quiz")
    print("12. Exit Tutorial")
    print("==========================================")

    choice = input("\nEnter your choice (1-12): ")

    # ======================================
    # LESSON 1 - PYTHON BASIC SYNTAX
    # ======================================

    if choice == "1":

        print("\n================================")
        print("LESSON 1")
        print("PYTHON BASIC SYNTAX")
        print("================================")

        print("\nWHAT IS PYTHON SYNTAX?")
        print("Python syntax refers to the rules")
        print("used when writing Python programs.")

        print("\nTOPIC 1: CASE SENSITIVITY")
        print("\nREAD THE TOPIC")
        print("Python is case-sensitive.")
        print("This means uppercase and lowercase")
        print("letters are treated differently.")

        print("\nEXAMPLE PROGRAM")
        print('name = "Alex"')
        print("print(name)")

        print("\nEXAMPLE OUTPUT")
        print("Alex")

        print("\nHOW IT WORKS")
        print("The variable name stores the word Alex.")
        print("The print statement displays its value.")

        print("\nCORRECT PROGRAM")
        print('name = "Alex"')
        print("print(name)")

        print("\nINCORRECT PROGRAM")
        print('name = "Alex"')
        print("print(Name)")

        print("\nWHY IS IT INCORRECT?")
        print("The variable name is lowercase.")
        print("Python does not recognize Name")
        print("as the same variable.")

        print("\nREMEMBER")
        print("Always use the correct uppercase")
        print("and lowercase letters.")

        print("\nTOPIC 2: INDENTATION")
        print("\nREAD THE TOPIC")
        print("Indentation means adding spaces")
        print("before a line of code.")
        print("Python commonly uses four spaces.")

        print("\nEXAMPLE PROGRAM")
        print("age = 18")
        print("if age >= 18:")
        print("    print('You are an adult.')")

        print("\nEXAMPLE OUTPUT")
        print("You are an adult.")

        print("\nHOW IT WORKS")
        print("The print statement is indented.")
        print("It belongs inside the if statement.")

        print("\nCORRECT PROGRAM")
        print("if age >= 18:")
        print("    print('Adult')")

        print("\nINCORRECT PROGRAM")
        print("if age >= 18:")
        print("print('Adult')")

        print("\nWHY IS IT INCORRECT?")
        print("The print statement is not indented.")
        print("Python requires proper indentation.")

        print("\nREMEMBER")
        print("Use proper indentation in your code.")

        print("\nLESSON SUMMARY")
        print("1. Python follows syntax rules.")
        print("2. Python is case-sensitive.")
        print("3. Indentation organizes code.")

        print("\nPRACTICE")
        print("Activity 1: Create a variable named student.")
        print("Store your name and print it.")
        print("Activity 2: Create an age checker")
        print("using an if statement.")

        print("\nBONUS CHALLENGE")
        print("Create a program that checks if")
        print("a person is 18 years old or above.")

        print("\nIMPORTANT")
        print("Remember case sensitivity and indentation.")
        print("Write and run your own program.")

        finished = input("\nDid you finish the activities? (Y/N): ")

        if finished == "Y" or finished == "y":
            print("Amazing! You practiced Python loops.")
        else:
            print("Review the examples and try again.")

    # ======================================
    # LESSON 2 - PRINTING OUTPUT
    # ======================================

    elif choice == "2":

        print("\n================================")
        print("LESSON 2")
        print("PRINTING OUTPUT")
        print("================================")

        print("\nWHAT IS PRINTING OUTPUT?")
        print("Printing output means displaying")
        print("information on the screen.")
        print("Python uses the print() statement.")

        print("\nTOPIC 1: PRINTING TEXT")
        print("\nREAD THE TOPIC")
        print("Text must be placed inside quotation marks.")

        print("\nEXAMPLE PROGRAM")
        print('print("Hello World")')

        print("\nEXAMPLE OUTPUT")
        print("Hello World")

        print("\nHOW IT WORKS")
        print("The print() statement displays")
        print("the text inside the quotation marks.")

        print("\nCORRECT PROGRAM")
        print('print("Welcome to Python")')

        print("\nINCORRECT PROGRAM")
        print("print(Welcome to Python)")

        print("\nWHY IS IT INCORRECT?")
        print("Text must be placed inside quotation marks.")
        print("Without them, Python treats the words")
        print("as variable names.")

        print("\nREMEMBER")
        print("Use quotation marks when printing text.")

        print("\nTOPIC 2: PRINTING NUMBERS")
        print("\nREAD THE TOPIC")
        print("Numbers can be printed without quotation marks.")

        print("\nEXAMPLE PROGRAM")
        print("print(100)")
        print("print(25.5)")

        print("\nEXAMPLE OUTPUT")
        print("100")
        print("25.5")

        print("\nHOW IT WORKS")
        print("Python displays the numbers directly.")

        print("\nCORRECT PROGRAM")
        print("print(50)")

        print("\nINCORRECT PROGRAM")
        print("print(50 + )")

        print("\nWHY IS IT INCORRECT?")
        print("The addition operator is missing")
        print("a number after it.")

        print("\nREMEMBER")
        print("Numbers can be printed directly.")

        print("\nTOPIC 3: PRINTING VARIABLES")
        print("\nREAD THE TOPIC")
        print("A variable can also be displayed")
        print("using the print() statement.")

        print("\nEXAMPLE PROGRAM")
        print('school = "Python Academy"')
        print("print(school)")

        print("\nEXAMPLE OUTPUT")
        print("Python Academy")

        print("\nHOW IT WORKS")
        print("The print statement displays")
        print("the value stored in school.")

        print("\nCORRECT PROGRAM")
        print('student = "Alex"')
        print("print(student)")

        print("\nINCORRECT PROGRAM")
        print('student = "Alex"')
        print("print(Student)")

        print("\nWHY IS IT INCORRECT?")
        print("Student and student are different")
        print("because Python is case-sensitive.")

        print("\nREMEMBER")
        print("You can display text, numbers,")
        print("and variables using print().")

        print("\nLESSON SUMMARY")
        print("1. print() displays information.")
        print("2. Text needs quotation marks.")
        print("3. Numbers can be printed directly.")
        print("4. Variables can be displayed.")

        print("\nPRACTICE")
        print("Activity 1: Print your name.")
        print("Activity 2: Print your age.")
        print("Activity 3: Create a variable for your school")
        print("and display it.")

        print("\nBONUS CHALLENGE")
        print("Create a welcome banner using print().")

        print("\nIMPORTANT")
        print("Practice using print() to display information.")

        finished = input("\nDid you finish the activities? (Y/N): ")

        if finished == "Y" or finished == "y":
            print("Amazing! You practiced Python loops.")
        else:
            print("Review the examples and try again.")
    # ======================================
    # LESSON 3 - PYTHON COMMENTS
    # ======================================

    elif choice == "3":

        print("\n================================")
        print("LESSON 3")
        print("PYTHON COMMENTS")
        print("================================")

        print("\nWHAT ARE PYTHON COMMENTS?")
        print("Comments are notes written inside")
        print("a Python program.")
        print("They are ignored when the program runs.")

        print("\nTOPIC 1: THE # SYMBOL")
        print("\nREAD THE TOPIC")
        print("Python uses the # symbol to create")
        print("a single-line comment.")

        print("\nEXAMPLE PROGRAM")
        print("# This is a comment")
        print('print("Hello")')

        print("\nEXAMPLE OUTPUT")
        print("Hello")

        print("\nHOW IT WORKS")
        print("Python ignores the line beginning")
        print("with the # symbol.")
        print("Only the print statement is displayed.")

        print("\nCORRECT PROGRAM")
        print("# Display a welcome message")
        print('print("Welcome")')

        print("\nINCORRECT EXAMPLE")
        print("Display a welcome message")
        print('print("Welcome")')

        print("\nWHY IS IT INCORRECT?")
        print("The explanation is not marked")
        print("as a comment using the # symbol.")

        print("\nREMEMBER")
        print("Use # before writing a comment.")

        print("\nTOPIC 2: WHY USE COMMENTS?")
        print("\nREAD THE TOPIC")
        print("Comments help explain what a program does.")
        print("They make code easier to understand.")

        print("\nEXAMPLE PROGRAM")
        print("# Store the student's name")
        print('name = "Alex"')
        print("# Display the name")
        print("print(name)")

        print("\nEXAMPLE OUTPUT")
        print("Alex")

        print("\nHOW IT WORKS")
        print("The comments explain the purpose")
        print("of each part of the program.")

        print("\nCORRECT PROGRAM")
        print("# Store age")
        print("age = 18")
        print("print(age)")

        print("\nINCORRECT EXAMPLE")
        print("Store age")
        print("age = 18")
        print("print(age)")

        print("\nWHY IS IT INCORRECT?")
        print("The words Store age are not written")
        print("as a comment, so Python tries to")
        print("interpret them as code.")

        print("\nREMEMBER")
        print("Comments help programmers understand code.")

        print("\nLESSON SUMMARY")
        print("1. Comments explain a program.")
        print("2. Use # for a single-line comment.")
        print("3. Comments are not displayed as output.")

        print("\nPRACTICE")
        print("Activity 1: Write a comment about your name.")
        print("Activity 2: Write a program with two comments.")

        print("\nBONUS CHALLENGE")
        print("Create a student information program")
        print("with comments explaining each line.")

        print("\nIMPORTANT")
        print("Use comments to make your programs easier")
        print("to understand.")

        finished = input("\nDid you finish the activities? (Y/N): ")

        if finished == "Y" or finished == "y":
            print("Amazing! You practiced Python loops.")
        else:
            print("Review the examples and try again.")

    # ======================================
    # LESSON 4 - VARIABLES AND CONSTANTS
    # ======================================

    elif choice == "4":

        print("\n================================")
        print("LESSON 4")
        print("VARIABLES AND CONSTANTS")
        print("================================")

        print("\nWHAT ARE VARIABLES AND CONSTANTS?")
        print("Variables store information that can change.")
        print("Constants are values that should not change.")

        print("\nTOPIC 1: VARIABLES")
        print("\nREAD THE TOPIC")
        print("A variable is a name used to store data.")
        print("You can change its value while the program runs.")

        print("\nEXAMPLE PROGRAM")
        print('name = "Alex"')
        print("age = 18")
        print("print(name)")
        print("print(age)")

        print("\nEXAMPLE OUTPUT")
        print("Alex")
        print("18")

        print("\nHOW IT WORKS")
        print("The variables name and age store values.")
        print("The print statements display those values.")

        print("\nCORRECT PROGRAM")
        print('student = "Maria"')
        print("print(student)")

        print("\nINCORRECT PROGRAM")
        print("student = Maria")
        print("print(student)")

        print("\nWHY IS IT INCORRECT?")
        print("Maria is text and should be inside")
        print("quotation marks.")

        print("\nREMEMBER")
        print("Use meaningful names for variables.")

        print("\nTOPIC 2: CONSTANTS")
        print("\nREAD THE TOPIC")
        print("A constant is a value that should not change.")
        print("Python does not have a special constant keyword.")
        print("Programmers commonly use uppercase names.")

        print("\nEXAMPLE PROGRAM")
        print("PI = 3.14")
        print("print(PI)")

        print("\nEXAMPLE OUTPUT")
        print("3.14")

        print("\nHOW IT WORKS")
        print("PI stores the value 3.14.")
        print("Uppercase letters show that it is")
        print("intended to be a constant.")

        print("\nCORRECT PROGRAM")
        print("SCHOOL_YEAR = 2026")
        print("print(SCHOOL_YEAR)")

        print("\nINCORRECT EXAMPLE")
        print("school_year = 2026")
        print("print(school_year)")

        print("\nWHY IS IT INCORRECT?")
        print("This code is valid Python.")
        print("However, lowercase naming does not")
        print("follow the common uppercase style")
        print("used for constants.")

        print("\nREMEMBER")
        print("Use uppercase names for constants.")

        print("\nLESSON SUMMARY")
        print("1. Variables store information.")
        print("2. Variable values can change.")
        print("3. Constants are intended to stay the same.")
        print("4. Constants are commonly written in uppercase.")

        print("\nPRACTICE")
        print("Activity 1: Create variables for your name and age.")
        print("Activity 2: Create a constant for your school name.")

        print("\nBONUS CHALLENGE")
        print("Create a student profile using variables")
        print("and a constant.")

        print("\nIMPORTANT")
        print("Remember the difference between")
        print("variables and constants.")

        finished = input("\nDid you finish the activities? (Y/N): ")

        if finished == "Y" or finished == "y":
            print("Amazing! You practiced Python loops.")
        else:
            print("Review the examples and try again.")

    # ======================================
    # LESSON 5 - BASIC DATA TYPES
    # ======================================

    elif choice == "5":

        print("\n================================")
        print("LESSON 5")
        print("BASIC DATA TYPES")
        print("================================")

        print("\nWHAT ARE DATA TYPES?")
        print("Data types describe the kind of")
        print("information stored in a variable.")

        print("\nTOPIC 1: INTEGER (int)")
        print("\nREAD THE TOPIC")
        print("An integer is a whole number.")
        print("It does not contain a decimal point.")

        print("\nEXAMPLE PROGRAM")
        print("age = 18")
        print("print(age)")

        print("\nEXAMPLE OUTPUT")
        print("18")

        print("\nHOW IT WORKS")
        print("The variable age stores the whole number 18.")

        print("\nCORRECT PROGRAM")
        print("number = 25")
        print("print(number)")

        print("\nINCORRECT EXAMPLE")
        print('number = "twenty-five"')
        print("print(number)")

        print("\nWHY IS IT INCORRECT?")
        print("This is valid Python, but the value")
        print("is a string instead of an integer.")

        print("\nREMEMBER")
        print("Integers are whole numbers.")

        print("\nTOPIC 2: FLOAT")
        print("\nREAD THE TOPIC")
        print("A float is a number that contains")
        print("a decimal point.")

        print("\nEXAMPLE PROGRAM")
        print("height = 5.5")
        print("print(height)")

        print("\nEXAMPLE OUTPUT")
        print("5.5")

        print("\nHOW IT WORKS")
        print("The variable height stores a decimal number.")

        print("\nCORRECT PROGRAM")
        print("price = 25.50")
        print("print(price)")

        print("\nINCORRECT PROGRAM")
        print("price = 25.50.")
        print("print(price)")

        print("\nWHY IS IT INCORRECT?")
        print("The extra decimal point makes")
        print("the number invalid.")

        print("\nREMEMBER")
        print("Floats contain decimal numbers.")

        print("\nTOPIC 3: STRING (str)")
        print("\nREAD THE TOPIC")
        print("A string is a group of characters.")
        print("Strings are written inside quotation marks.")

        print("\nEXAMPLE PROGRAM")
        print('name = "Alex"')
        print("print(name)")

        print("\nEXAMPLE OUTPUT")
        print("Alex")

        print("\nHOW IT WORKS")
        print("The variable name stores the text Alex.")

        print("\nCORRECT PROGRAM")
        print('food = "Pizza"')
        print("print(food)")

        print("\nINCORRECT PROGRAM")
        print("food = Pizza")
        print("print(food)")

        print("\nWHY IS IT INCORRECT?")
        print("Pizza is text and needs quotation marks.")

        print("\nREMEMBER")
        print("Strings are written inside quotation marks.")

        print("\nTOPIC 4: BOOLEAN (bool)")
        print("\nREAD THE TOPIC")
        print("A Boolean has only two possible values:")
        print("True or False.")

        print("\nEXAMPLE PROGRAM")
        print("is_student = True")
        print("print(is_student)")

        print("\nEXAMPLE OUTPUT")
        print("True")

        print("\nHOW IT WORKS")
        print("The variable stores the Boolean value True.")

        print("\nCORRECT PROGRAM")
        print("is_active = False")
        print("print(is_active)")

        print("\nINCORRECT PROGRAM")
        print('is_active = "False"')
        print("print(is_active)")

        print("\nWHY IS IT INCORRECT?")
        print("This is valid Python, but the value")
        print("is a string instead of a Boolean.")

        print("\nREMEMBER")
        print("Boolean values are True and False.")
        print("They do not need quotation marks.")

        print("\nLESSON SUMMARY")
        print("1. Integer - whole numbers.")
        print("2. Float - decimal numbers.")
        print("3. String - text.")
        print("4. Boolean - True or False.")

        print("\nPRACTICE")
        print("Activity 1: Create an integer for your age.")
        print("Activity 2: Create a float for your height.")
        print("Activity 3: Create a string for your name.")
        print("Activity 4: Create a Boolean variable.")

        print("\nBONUS CHALLENGE")
        print("Create a student profile using all")
        print("four basic data types.")

        print("\nIMPORTANT")
        print("Choose the correct data type for your values.")

        finished = input("\nDid you finish the activities? (Y/N): ")

        if finished == "Y" or finished == "y":
            print("Amazing! You practiced Python loops.")
        else:
            print("Review the examples and try again.")
    
    # ======================================
    # LESSON 6 - ARITHMETIC OPERATORS
    # ======================================

    elif choice == "6":

        print("\n================================")
        print("LESSON 6")
        print("ARITHMETIC OPERATORS AND EXPRESSIONS")
        print("================================")

        print("\nWHAT ARE ARITHMETIC OPERATORS?")
        print("Arithmetic operators are symbols")
        print("used to perform mathematical operations.")

        print("\nTOPIC 1: ADDITION (+) AND SUBTRACTION (-)")
        print("\nREAD THE TOPIC")
        print("Addition adds two values.")
        print("Subtraction subtracts the second value")
        print("from the first value.")

        print("\nEXAMPLE PROGRAM")
        print("print(5 + 3)")
        print("print(10 - 4)")

        print("\nEXAMPLE OUTPUT")
        print("8")
        print("6")

        print("\nHOW IT WORKS")
        print("5 + 3 gives 8.")
        print("10 - 4 gives 6.")

        print("\nCORRECT PROGRAM")
        print("print(20 + 10)")
        print("print(20 - 10)")

        print("\nINCORRECT PROGRAM")
        print("print(20 + )")

        print("\nWHY IS IT INCORRECT?")
        print("The second value is missing.")

        print("\nREMEMBER")
        print("+ means addition.")
        print("- means subtraction.")

        print("\nTOPIC 2: MULTIPLICATION (*) AND DIVISION (/)")
        print("\nREAD THE TOPIC")
        print("Multiplication multiplies two values.")
        print("Division divides two values and")
        print("returns a decimal result.")

        print("\nEXAMPLE PROGRAM")
        print("print(7 * 2)")
        print("print(15 / 3)")

        print("\nEXAMPLE OUTPUT")
        print("14")
        print("5.0")

        print("\nHOW IT WORKS")
        print("7 multiplied by 2 gives 14.")
        print("15 divided by 3 gives 5.0.")

        print("\nCORRECT PROGRAM")
        print("print(8 * 2)")
        print("print(8 / 2)")

        print("\nINCORRECT PROGRAM")
        print("print(8 / )")

        print("\nWHY IS IT INCORRECT?")
        print("The second value is missing.")

        print("\nREMEMBER")
        print("* means multiplication.")
        print("/ means division.")

        print("\nTOPIC 3: FLOOR DIVISION (//)")
        print("\nREAD THE TOPIC")
        print("Floor division divides two values")
        print("and returns the whole-number part")
        print("of the result.")

        print("\nEXAMPLE PROGRAM")
        print("print(17 // 3)")

        print("\nEXAMPLE OUTPUT")
        print("5")

        print("\nHOW IT WORKS")
        print("17 divided by 3 is 5.666...")
        print("Floor division returns 5.")

        print("\nCORRECT PROGRAM")
        print("print(20 // 4)")

        print("\nINCORRECT PROGRAM")
        print("print(20 // )")

        print("\nWHY IS IT INCORRECT?")
        print("The second value is missing.")

        print("\nREMEMBER")
        print("// returns the whole-number")
        print("part of the division result.")

        print("\nTOPIC 4: MODULUS (%)")
        print("\nREAD THE TOPIC")
        print("The modulus operator returns")
        print("the remainder after division.")

        print("\nEXAMPLE PROGRAM")
        print("print(10 % 3)")

        print("\nEXAMPLE OUTPUT")
        print("1")

        print("\nHOW IT WORKS")
        print("10 divided by 3 leaves a remainder of 1.")

        print("\nCORRECT PROGRAM")
        print("print(15 % 4)")

        print("\nINCORRECT PROGRAM")
        print("print(15 % )")

        print("\nWHY IS IT INCORRECT?")
        print("The second value is missing.")

        print("\nREMEMBER")
        print("% gives the remainder.")

        print("\nTOPIC 5: EXPONENTIATION (**)")
        print("\nREAD THE TOPIC")
        print("Exponentiation raises the first value")
        print("to the power of the second value.")

        print("\nEXAMPLE PROGRAM")
        print("print(2 ** 3)")

        print("\nEXAMPLE OUTPUT")
        print("8")

        print("\nHOW IT WORKS")
        print("2 ** 3 means 2 multiplied by itself")
        print("three times.")
        print("2 x 2 x 2 gives 8.")

        print("\nCORRECT PROGRAM")
        print("print(3 ** 2)")

        print("\nINCORRECT PROGRAM")
        print("print(2 ** )")

        print("\nWHY IS IT INCORRECT?")
        print("The second value, which represents")
        print("the power, is missing.")

        print("\nREMEMBER")
        print("** is used for exponentiation.")

        print("\nLESSON SUMMARY")
        print("1. + Addition")
        print("2. - Subtraction")
        print("3. * Multiplication")
        print("4. / Division")
        print("5. // Floor Division")
        print("6. % Modulus")
        print("7. ** Exponentiation")

        print("\nPRACTICE")
        print("Activity 1: Create a mini calculator.")
        print("Ask for two numbers and display their:")
        print("Addition, Subtraction, Multiplication,")
        print("and Division.")

        print("\nActivity 2: Practice Floor Division.")
        print("Use // to divide two numbers.")

        print("\nActivity 3: Practice Modulus.")
        print("Use % to find the remainder.")

        print("\nActivity 4: Practice Exponentiation.")
        print("Use ** to calculate a number's power.")

        print("\nBONUS CHALLENGE")
        print("Create a program that uses all seven")
        print("arithmetic operators.")

        print("\nIMPORTANT")
        print("Remember the seven arithmetic operators")
        print("and understand how each one works.")

        finished = input("\nDid you finish your program? (Y/N): ")

        if finished == "Y" or finished == "y":
             print("Great job! You learned Python Basic Syntax.")
        else:
             print("Take your time. Review the examples and try again.")

    # ======================================
    # LESSON 7 - BASIC INPUT AND OUTPUT
    # ======================================

    elif choice == "7":

        print("\n================================")
        print("LESSON 7")
        print("BASIC INPUT AND OUTPUT")
        print("================================")

        print("\nWHAT ARE INPUT AND OUTPUT?")
        print("Input allows the user to enter information.")
        print("Output displays information on the screen.")

        print("\nTOPIC 1: INPUT")
        print("\nREAD THE TOPIC")
        print("Python uses input() to receive information")
        print("from the user.")

        print("\nEXAMPLE PROGRAM")
        print('name = input("Enter your name: ")')
        print("print(name)")

        print("\nEXAMPLE OUTPUT")
        print("Enter your name: Alex")
        print("Alex")

        print("\nHOW IT WORKS")
        print("The input() statement asks the user")
        print("to enter a name.")
        print("The entered name is stored in the variable.")

        print("\nCORRECT PROGRAM")
        print('age = input("Enter your age: ")')
        print("print(age)")

        print("\nINCORRECT EXAMPLE")
        print('age = input("Enter your age: "')
        print("print(age)")

        print("\nWHY IS IT INCORRECT?")
        print("The closing parenthesis is missing.")

        print("\nREMEMBER")
        print("Use input() to receive information.")

        print("\nTOPIC 2: OUTPUT")
        print("\nREAD THE TOPIC")
        print("Output displays information using print().")

        print("\nEXAMPLE PROGRAM")
        print('name = "Alex"')
        print('print("Welcome", name)')

        print("\nEXAMPLE OUTPUT")
        print("Welcome Alex")

        print("\nHOW IT WORKS")
        print("The print statement displays the message")
        print("and the value stored in name.")

        print("\nCORRECT PROGRAM")
        print('print("Hello Student")')

        print("\nINCORRECT PROGRAM")
        print("print(Hello Student)")

        print("\nWHY IS IT INCORRECT?")
        print("Text must be placed inside quotation marks.")

        print("\nREMEMBER")
        print("Use print() to display information.")

        print("\nLESSON SUMMARY")
        print("1. input() receives information.")
        print("2. print() displays information.")
        print("3. Variables can store user input.")

        print("\nPRACTICE")
        print("Activity 1: Create a personal information form.")
        print("Ask for the user's name, age, and favorite food.")
        print("Display all the information.")

        print("\nActivity 2: Create a welcome message")
        print("that uses the user's name.")

        print("\nBONUS CHALLENGE")
        print("Create a student introduction program")
        print("that asks for name, age, and favorite subject.")

        print("\nIMPORTANT")
        print("Practice receiving and displaying information.")

        finished = input("\nDid you finish your program? (Y/N): ")

        if finished == "Y" or finished == "y":
             print("Great job! You learned Python Basic Syntax.")
        else:
             print("Take your time. Review the examples and try again.")
    # ==========================================
    # LESSON 8 - CONDITIONAL STATEMENTS IN PYTHON
    # ==========================================
    
    elif choice == "8":

        print("\n==========================================")
        print("       LESSON 8")
        print("       CONDITIONAL STATEMENTS IN PYTHON")
        print("==========================================")

        print("\nWHAT ARE CONDITIONAL STATEMENTS?")
        print("------------------------------------------")
        print("Conditional statements allow a program")
        print("to make decisions based on conditions.")
        print("They execute different blocks of code")
        print("depending on whether a condition is")
        print("True or False.")

        print("\nTYPES OF CONDITIONAL STATEMENTS:")
        print("1. if Statement")
        print("2. if-else Statement")
        print("3. if-elif-else Statement")
        print("4. Nested Condition")

        print("\n==========================================")
        print("\nTOPIC 1 - THE IF STATEMENT")
        print("==========================================")

        print("\nWHAT IS AN IF STATEMENT?")
        print("------------------------------------------")
        print("The if statement is used to check")
        print("a condition.")
        print("If the condition is True, the program")
        print("will execute the code inside the if block.")
        print("If the condition is False, the code")
        print("inside the if block will be skipped.")

        print("\nREAD THE LESSON:")
        print("------------------------------------------")
        print("1. if - checks the condition.")
        print("2. condition - the expression being checked.")
        print("3. colon (:) - marks the beginning")
        print("   of the code block.")
        print("4. indentation - separates the code")
        print("   inside the if statement.")

        print("\nEXAMPLE PROGRAM:")
        print("------------------------------------------")
        print("age = 18")
        print("if age >= 18:")
        print('    print("You are an adult.")')

        print("\nOUTPUT:")
        print("------------------------------------------")
        print("You are an adult.")

        print("\nHOW IT WORKS:")
        print("------------------------------------------")
        print("1. The variable age stores the value 18.")
        print("2. The if statement checks if age is")
        print("   greater than or equal to 18.")
        print("3. The condition is True.")
        print("4. The program displays You are an adult.")

        print("\nTOPIC 2- THE IF-ELSE STATEMENT")
        
        print("\nWHAT IS AN IF-ELSE STATEMENT?")
        print("------------------------------------------")
        print("The if-else statement provides an")
        print("alternative when the if condition is False.")
        print()
        print("The if block runs when the condition")
        print("is True.")
        print("The else block runs when the condition")
        print("is False.")
        print("Only one of the blocks will be executed.")

        print("\nEXAMPLE PROGRAM:")
        print("------------------------------------------")
        print("score = 65")
        print("if score >= 75:")
        print('    print("Passed")')
        print("else:")
        print('    print("Failed")')

        print("\nOUTPUT:")
        print("------------------------------------------")
        print("Failed")

        print("\nHOW IT WORKS:")
        print("------------------------------------------")
        print("1. The variable score stores 65.")
        print("2. The program checks if score is")
        print("   greater than or equal to 75.")
        print("3. The condition is False.")
        print("4. The else block is executed.")
        print("5. The program displays Failed.")

        print("\nTOPIC 3 - COMPARISON OPERATORS")
        
        print("\nWHAT ARE COMPARISON OPERATORS?")
        print("------------------------------------------")
        print("Comparison operators are used to compare")
        print("two values.")
        print("They return either True or False.")

        print("\nCOMPARISON OPERATORS:")
        print("------------------------------------------")
        print("==  Equal to")
        print("!=  Not equal to")
        print(">   Greater than")
        print("<   Less than")
        print(">=  Greater than or equal to")
        print("<=  Less than or equal to")

        print("\nEXAMPLES OF IF-ELSE WITH COMPARISON")
        print("OPERATORS:")
        print("------------------------------------------")

        print("\n1. EQUAL TO (==)")
        print("score = 10")
        print("if score == 10:")
        print('    print("Equal")')
        print("else:")
        print('    print("Not Equal")')
        print("Output: Equal")

        print("\n2. NOT EQUAL TO (!=)")
        print("score = 10")
        print("if score != 10:")
        print('    print("Not Equal")')
        print("else:")
        print('    print("Equal")')
        print("Output: Equal")

        print("\n3. GREATER THAN (>)")
        print("score = 10")
        print("if score > 10:")
        print('    print("Greater")')
        print("else:")
        print('    print("Not Greater")')
        print("Output: Not Greater")

        print("\n4. LESS THAN (<)")
        print("score = 10")
        print("if score < 10:")
        print('    print("Less")')
        print("else:")
        print('    print("Not Less")')
        print("Output: Not Less")

        print("\n5. GREATER THAN OR EQUAL TO (>=)")
        print("score = 10")
        print("if score >= 10:")
        print('    print("Greater or Equal")')
        print("else:")
        print('    print("Less")')
        print("Output: Greater or Equal")

        print("\n6. LESS THAN OR EQUAL TO (<=)")
        print("score = 10")
        print("if score <= 10:")
        print('    print("Less or Equal")')
        print("else:")
        print('    print("Greater")')
        print("Output: Less or Equal")

        print("\nREMEMBER:")
        print("------------------------------------------")
        print("Comparison operators help the program")
        print("decide which condition is True or False.")
        
        print("\nTOPIC 4 - IF-ELIF-ELSE STATEMENT")
        
        print("\nWHAT IS AN IF-ELIF-ELSE STATEMENT?")
        print("------------------------------------------")
        print("The if-elif-else statement is used when")
        print("we need to check multiple conditions.")
        print()
        print("The program checks the conditions from")
        print("top to bottom.")
        print("When a condition is True, its block")
        print("will be executed.")

        print("\nEXAMPLE PROGRAM:")
        print("------------------------------------------")
        print("score = 85")
        print("if score >= 90:")
        print('    print("Excellent")')
        print("elif score >= 75:")
        print('    print("Passed")')
        print("else:")
        print('    print("Failed")')

        print("\nOUTPUT:")
        print("------------------------------------------")
        print("Passed")

        print("\nHOW IT WORKS:")
        print("------------------------------------------")
        print("1. The program checks if score is 90 or")
        print("   higher.")
        print("2. The first condition is False.")
        print("3. It checks the elif condition.")
        print("4. The score is greater than or equal")
        print("   to 75.")
        print("5. The program displays Passed.")

        print("\nTOPIC 5- NESTED CONDITION IN PYTHON")
        
        print("\nWHAT IS A NESTED CONDITION?")
        print("------------------------------------------")
        print("A nested condition is a condition")
        print("inside another condition.")
        print()
        print("It means that an if statement can be")
        print("placed inside another if statement.")
        print()
        print("The second condition is checked only")
        print("if the first condition is True.")

        print("\nREAD THE LESSON:")
        print("------------------------------------------")
        print("1. The first condition is checked.")
        print("2. If the first condition is True,")
        print("   the second condition is checked.")
        print("3. If the second condition is True,")
        print("   its code will run.")
        print("4. If the second condition is False,")
        print("   its else block will run.")
        print("5. If the first condition is False,")
        print("   the outer else block will run.")

        print("\nEXAMPLE PROGRAM:")
        print("------------------------------------------")
        print("gender = input('Enter gender (M/F): ')")
        print("age = int(input('Enter age: '))")
        print()
        print("if gender == 'M':")
        print("    if age >= 21:")
        print('        print("You are a MALE DEBUTANT.")')
        print("    else:")
        print('        print("You are a male, but not yet a debutant.")')
        print("else:")
        print("    if age >= 18:")
        print('        print("You are a FEMALE DEBUTANT.")')
        print("    else:")
        print('        print("You are a female, but not yet a debutant.")')

        print("\nEXAMPLE 1:")
        print("------------------------------------------")
        print("Enter gender (M/F): M")
        print("Enter age: 21")
        print("You are a MALE DEBUTANT.")

        print("\nEXAMPLE 2:")
        print("------------------------------------------")
        print("Enter gender (M/F): M")
        print("Enter age: 19")
        print("You are a male, but not yet a debutant.")

        print("\nEXAMPLE 3:")
        print("------------------------------------------")
        print("Enter gender (M/F): F")
        print("Enter age: 18")
        print("You are a FEMALE DEBUTANT.")

        print("\nEXAMPLE 4:")
        print("------------------------------------------")
        print("Enter gender (M/F): F")
        print("Enter age: 16")
        print("You are a female, but not yet a debutant.")

        print("\nHOW IT WORKS:")
        print("------------------------------------------")
        print("1. The program asks for gender and age.")
        print("2. It checks the first condition:")
        print("   gender == 'M'.")
        print("3. If True, it checks the male age.")
        print("4. If False, it goes to the outer else")
        print("   and checks the female age.")
        print("5. The inner condition determines")
        print("   the final result.")

        print("\nREMEMBER:")
        print("------------------------------------------")
        print("A nested condition is an if statement")
        print("inside another if statement.")
        print("The inner condition is only checked")
        print("when the outer condition is True.")

        print("\nCORRECT PROGRAM:")
        print("------------------------------------------")
        print("age = 20")
        print("if age >= 18:")
        print('    print("You can vote.")')
        print("else:")
        print('    print("You cannot vote yet.")')

        print("\nOUTPUT:")
        print("You can vote.")

        print("\nINCORRECT PROGRAM:")
        print("------------------------------------------")
        print("age = 20")
        print("if age >= 18")
        print('    print("You can vote.")')

        print("\nWHY IS IT INCORRECT?")
        print("------------------------------------------")
        print("The colon (:) is missing after the")
        print("if condition.")
        print("Python needs a colon to begin a")
        print("conditional code block.")

        print("\nANOTHER INCORRECT PROGRAM:")
        print("------------------------------------------")
        print("age = 20")
        print("if age >= 18:")
        print('print("You can vote.")')

        print("\nWHY IS IT INCORRECT?")
        print("------------------------------------------")
        print("The print statement is not indented.")
        print("The code inside an if statement must")
        print("have proper indentation.")

        print("\nSUMMARY")
        print("1. if - checks a condition.")
        print("2. if-else - provides an alternative.")
        print("3. if-elif-else - checks multiple conditions.")
        print("4. Nested condition - places a condition")
        print("   inside another condition.")
        print("5. Comparison operators - compare values.")
        print()
        print("IMPORTANT:")
        print("Always remember to use a colon (:)")
        print("and proper indentation in conditional")
        print("statements.")
        
        print("\nPRACTICE ")
        print("\nACTIVITY 1 - IF-ELSE")
        print("------------------------------------------")
        print("Create a program that checks if a number")
        print("is positive or negative.")
        print()
        print("Requirements:")
        print("1. Ask the user to enter a number.")
        print("2. Use an if-else statement.")
        print("3. If the number is greater than 0,")
        print('   display "Positive Number".')
        print("4. Otherwise, display Negative or Zero.")

        print("\nACTIVITY 2 - NESTED CONDITION")
        print("------------------------------------------")
        print("Create a simple school admission checker.")
        print()
        print("Requirements:")
        print("1. Ask the user to enter their age.")
        print("2. Check if the age is 18 or above.")
        print("3. If True, check if the age is 21 or above.")
        print("4. Display the appropriate result.")

        
        print("\nBONUS CHALLENGE")
        print("Create a simple grade checker.")
        print("------------------------------------------")
        print("Requirements:")
        print("1. Ask the user to enter their score.")
        print("2. Use if-elif-else statements.")
        print("3. If score is 90 or above, display Excellent.")
        print("4. If score is 75 or above, display Passed.")
        print("5. Otherwise, display Failed.")

        print("\n==========================================")
        print("       LESSON 8 COMPLETED!")
        print("==========================================")

        finished = input("\nDid you finish your program? (Y/N): ")

        if finished == "Y" or finished == "y":
            print("Great job! You learned Python Basic Syntax.")
        else:
            print("Take your time. Review the examples and try again.")

    # ======================================
    # LESSON 9 - LOGICAL OPERATORS
    # ======================================

    elif choice == "9":

        print("\n================================")
        print("LESSON 9")
        print("LOGICAL OPERATORS")
        print("================================")

        print("\nWHAT ARE LOGICAL OPERATORS?")
        print("Logical operators combine or change")
        print("conditions in a Python program.")

        print("\nTOPIC 1: AND OPERATOR")
        print("\nREAD THE TOPIC")
        print("The and operator returns True only")
        print("when both conditions are True.")

        print("\nEXAMPLE PROGRAM")
        print("age = 20")
        print("grade = 85")
        print("if age >= 18 and grade >= 75:")
        print("    print('Qualified')")

        print("\nEXAMPLE OUTPUT")
        print("Qualified")

        print("\nHOW IT WORKS")
        print("Both conditions are True.")
        print("Therefore, the program displays Qualified.")

        print("\nCORRECT PROGRAM")
        print("age = 20")
        print("grade = 90")
        print("if age >= 18 and grade >= 75:")
        print("    print('Accepted')")

        print("\nINCORRECT PROGRAM")
        print("age = 20")
        print("grade = 90")
        print("if age >= 18 and:")
        print("    print('Accepted')")

        print("\nWHY IS IT INCORRECT?")
        print("The second condition is missing.")

        print("\nREMEMBER")
        print("and requires both conditions to be True.")

        print("\nTOPIC 2: OR OPERATOR")
        print("\nREAD THE TOPIC")
        print("The or operator returns True when")
        print("at least one condition is True.")

        print("\nEXAMPLE PROGRAM")
        print("day = 'Saturday'")
        print("if day == 'Saturday' or day == 'Sunday':")
        print("    print('Weekend')")

        print("\nEXAMPLE OUTPUT")
        print("Weekend")

        print("\nHOW IT WORKS")
        print("At least one condition is True.")
        print("Therefore, Weekend is displayed.")

        print("\nCORRECT PROGRAM")
        print("age = 16")
        print("if age < 18 or age == 18:")
        print("    print('Young')")

        print("\nINCORRECT PROGRAM")
        print("age = 16")
        print("if age < 18 or:")
        print("    print('Young')")

        print("\nWHY IS IT INCORRECT?")
        print("The second condition is missing.")

        print("\nREMEMBER")
        print("or needs at least one True condition.")

        print("\nTOPIC 3: NOT OPERATOR")
        print("\nREAD THE TOPIC")
        print("The not operator reverses a Boolean value.")
        print("True becomes False, and False becomes True.")

        print("\nEXAMPLE PROGRAM")
        print("is_raining = False")
        print("if not is_raining:")
        print("    print('You can go outside.')")

        print("\nEXAMPLE OUTPUT")
        print("You can go outside.")

        print("\nHOW IT WORKS")
        print("The value of is_raining is False.")
        print("The not operator reverses it to True.")

        print("\nCORRECT PROGRAM")
        print("is_open = False")
        print("if not is_open:")
        print("    print('Closed')")

        print("\nINCORRECT EXAMPLE")
        print("is_open = False")
        print("if not:")
        print("    print('Closed')")

        print("\nWHY IS IT INCORRECT?")
        print("The not operator needs a condition")
        print("or Boolean value after it.")

        print("\nREMEMBER")
        print("not reverses a Boolean value.")

        print("\nLESSON SUMMARY")
        print("1. and - both conditions must be True.")
        print("2. or - at least one condition must be True.")
        print("3. not - reverses a Boolean value.")

        print("\nPRACTICE")
        print("Activity 1: Create a school admission checker")
        print("using age and grade with and.")

        print("\nActivity 2: Create a weekend checker")
        print("using or.")

        print("\nActivity 3: Create a program using not.")

        print("\nBONUS CHALLENGE")
        print("Create a school activity checker")
        print("using and, or, and not.")

        print("\nIMPORTANT")
        print("Understand when to use each logical operator.")

        finished = input("\nDid you finish the activities? (Y/N): ")

        if finished == "Y" or finished == "y":
            print("Amazing! You practiced Python loops.")
        else:
            print("Review the examples and try again.")
    # ======================================
    # LESSON 10 - ITERATION AND LOOPS
    # ======================================

    elif choice == "10":

        print("\n================================")
        print("LESSON 10")
        print("INTRODUCTION TO ITERATION AND LOOPS")
        print("================================")

        print("\nWHAT ARE ITERATION AND LOOPS?")
        print("Loops repeat a block of code.")
        print("They help avoid writing the same code")
        print("many times.")

        print("\nTOPIC 1: FOR LOOP")
        print("\nREAD THE TOPIC")
        print("A for loop repeats code for each item")
        print("in a sequence.")
        print("The range() function can be used")
        print("to repeat a specific number of times.")

        print("\nEXAMPLE PROGRAM")
        print("for number in range(1, 4):")
        print("    print(number)")

        print("\nEXAMPLE OUTPUT")
        print("1")
        print("2")
        print("3")

        print("\nHOW IT WORKS")
        print("The for loop repeats three times.")
        print("It displays 1, 2, and 3.")

        print("\nCORRECT PROGRAM")
        print("for number in range(1, 6):")
        print("    print(number)")

        print("\nINCORRECT PROGRAM")
        print("for number in range(1, 6)")
        print("    print(number)")

        print("\nWHY IS IT INCORRECT?")
        print("The colon is missing after the for loop.")

        print("\nREMEMBER")
        print("A for loop repeats code through a sequence.")

        print("\nTOPIC 2: WHILE LOOP")
        print("\nREAD THE TOPIC")
        print("A while loop repeats code as long as")
        print("its condition is True.")

        print("\nEXAMPLE PROGRAM")
        print("count = 1")
        print("while count <= 3:")
        print("    print(count)")
        print("    count = count + 1")

        print("\nEXAMPLE OUTPUT")
        print("1")
        print("2")
        print("3")

        print("\nHOW IT WORKS")
        print("The loop starts at 1.")
        print("It repeats while count is less than")
        print("or equal to 3.")
        print("The count increases by 1 each time.")

        print("\nCORRECT PROGRAM")
        print("count = 1")
        print("while count <= 5:")
        print("    print(count)")
        print("    count = count + 1")

        print("\nINCORRECT PROGRAM")
        print("count = 1")
        print("while count <= 5:")
        print("    print(count)")

        print("\nWHY IS IT INCORRECT?")
        print("The count is never increased.")
        print("The condition stays True, so the loop")
        print("does not stop on its own.")

        print("\nREMEMBER")
        print("Make sure a while loop can eventually stop.")

        print("\nTOPIC 3: BREAK")
        print("\nREAD THE TOPIC")
        print("The break statement immediately stops")
        print("a loop.")

        print("\nEXAMPLE PROGRAM")
        print("for number in range(1, 6):")
        print("    if number == 4:")
        print("        break")
        print("    print(number)")

        print("\nEXAMPLE OUTPUT")
        print("1")
        print("2")
        print("3")

        print("\nHOW IT WORKS")
        print("When number becomes 4, break stops the loop.")

        print("\nCORRECT PROGRAM")
        print("for number in range(1, 6):")
        print("    if number == 3:")
        print("        break")
        print("    print(number)")

        print("\nINCORRECT PROGRAM")
        print("for number in range(1, 6):")
        print("    if number == 3:")
        print("        break")
        print("        print(number)")

        print("\nWHY IS IT INCORRECT?")
        print("The print statement is placed after break")
        print("inside the same block.")
        print("It will not run when break is reached.")

        print("\nREMEMBER")
        print("break stops the loop immediately.")

        print("\nTOPIC 4: CONTINUE")
        print("\nREAD THE TOPIC")
        print("The continue statement skips the current")
        print("iteration and moves to the next one.")

        print("\nEXAMPLE PROGRAM")
        print("for number in range(1, 6):")
        print("    if number == 3:")
        print("        continue")
        print("    print(number)")

        print("\nEXAMPLE OUTPUT")
        print("1")
        print("2")
        print("4")
        print("5")

        print("\nHOW IT WORKS")
        print("When number becomes 3, continue skips")
        print("the print statement for that iteration.")
        print("The loop continues with the next number.")

        print("\nCORRECT PROGRAM")
        print("for number in range(1, 6):")
        print("    if number == 2:")
        print("        continue")
        print("    print(number)")

        print("\nINCORRECT EXAMPLE")
        print("for number in range(1, 6):")
        print("    if number == 2:")
        print("    continue")
        print("    print(number)")

        print("\nWHY IS IT INCORRECT?")
        print("The continue statement is not properly")
        print("indented inside the if statement.")

        print("\nREMEMBER")
        print("continue skips the current iteration.")

        print("\nLESSON SUMMARY")
        print("1. for repeats code through a sequence.")
        print("2. while repeats while a condition is True.")
        print("3. break stops a loop.")
        print("4. continue skips the current iteration.")

        print("\nPRACTICE")
        print("Activity 1: Create a countdown using for.")
        print("Display numbers from 10 down to 1.")

        print("\nActivity 2: Create a while loop")
        print("that counts from 1 to 5.")

        print("\nBONUS CHALLENGE")
        print("Create a for loop from 1 to 10.")
        print("Use continue to skip number 5.")

        print("\nCreate another loop that stops at number 7")
        print("using break.")

        print("\nIMPORTANT")
        print("Understand the difference between")
        print("for, while, break, and continue.")

        finished = input("\nDid you finish the activities? (Y/N): ")

        if finished == "Y" or finished == "y":
            print("Amazing! You practiced Python loops.")
        else:
            print("Review the examples and try again.")

    # ======================================
    # LESSON 11 - PYTHON KNOWLEDGE QUIZ
    # ======================================

    elif choice == "11":

        retry = "Y"

        while retry == "Y":

            score = 0
            wrong = 0

            print("\n================================")
            print("       PYTHON KNOWLEDGE QUIZ")
            print("================================")
            print("1. 10 Questions")
            print("2. 15 Questions")

            quiz_choice = input("\nChoose your quiz (1 or 2): ")

            if quiz_choice == "1":
                total = 10
            elif quiz_choice == "2":
                total = 15
            else:
                print("Invalid quiz choice.")
                continue

            print("\n================================")
            print("          START QUIZ")
            print("================================")

            print("\n1. What does Python syntax mean?")
            print("A. Rules for writing Python code")
            print("B. A type of computer")
            print("C. A programming game")
            print("D. A computer part")
            answer = input("Your answer: ").upper()

            if answer == "A":
                score += 1
            else:
                wrong += 1

            print("\n2. Which function displays output?")
            print("A. input()")
            print("B. print()")
            print("C. display()")
            print("D. show()")
            answer = input("Your answer: ").upper()

            if answer == "B":
                score += 1
            else:
                wrong += 1

            print("\n3. Which symbol is used for comments?")
            print("A. @")
            print("B. $")
            print("C. #")
            print("D. &")
            answer = input("Your answer: ").upper()

            if answer == "C":
                score += 1
            else:
                wrong += 1

            print("\n4. What is the purpose of a variable?")
            print("A. To delete information")
            print("B. To store information")
            print("C. To close a program")
            print("D. To print errors")
            answer = input("Your answer: ").upper()

            if answer == "B":
                score += 1
            else:
                wrong += 1

            print("\n5. Which data type stores whole numbers?")
            print("A. String")
            print("B. Float")
            print("C. Boolean")
            print("D. Integer")
            answer = input("Your answer: ").upper()

            if answer == "D":
                score += 1
            else:
                wrong += 1

            print("\n6. Which symbol is used for multiplication?")
            print("A. +")
            print("B. -")
            print("C. *")
            print("D. /")
            answer = input("Your answer: ").upper()

            if answer == "C":
                score += 1
            else:
                wrong += 1

            print("\n7. Which function receives user information?")
            print("A. print()")
            print("B. input()")
            print("C. output()")
            print("D. show()")
            answer = input("Your answer: ").upper()

            if answer == "B":
                score += 1
            else:
                wrong += 1

            print("\n8. Which statement is used for decisions?")
            print("A. print")
            print("B. input")
            print("C. if")
            print("D. break")
            answer = input("Your answer: ").upper()

            if answer == "C":
                score += 1
            else:
                wrong += 1

            print("\n9. What does AND require?")
            print("A. One condition is True")
            print("B. Both conditions are True")
            print("C. Both conditions are False")
            print("D. No conditions")
            answer = input("Your answer: ").upper()

            if answer == "B":
                score += 1
            else:
                wrong += 1

            print("\n10. What is the purpose of a loop?")
            print("A. To delete a program")
            print("B. To stop Python")
            print("C. To repeat a sequence of code")
            print("D. To change a computer")
            answer = input("Your answer: ").upper()

            if answer == "C":
                score += 1
            else:
                wrong += 1

            if quiz_choice == "2":

                print("\n11. How are constants commonly written?")
                print("A. All lowercase")
                print("B. All uppercase")
                print("C. With spaces")
                print("D. With numbers only")
                answer = input("Your answer: ").upper()

                if answer == "B":
                    score += 1
                else:
                    wrong += 1

                print("\n12. Which data type stores decimal numbers?")
                print("A. Integer")
                print("B. String")
                print("C. Float")
                print("D. Boolean")
                answer = input("Your answer: ").upper()

                if answer == "C":
                    score += 1
                else:
                    wrong += 1

                print("\n13. Which operator gives the remainder?")
                print("A. +")
                print("B. -")
                print("C. *")
                print("D. %")
                answer = input("Your answer: ").upper()

                if answer == "D":
                    score += 1
                else:
                    wrong += 1

                print("\n14. What does OR require?")
                print("A. Both conditions must be True")
                print("B. At least one condition is True")
                print("C. All conditions must be False")
                print("D. No conditions")
                answer = input("Your answer: ").upper()

                if answer == "B":
                    score += 1
                else:
                    wrong += 1

                print("\n15. Which statement stops a loop?")
                print("A. continue")
                print("B. print")
                print("C. break")
                print("D. input")
                answer = input("Your answer: ").upper()

                if answer == "C":
                    score += 1
                else:
                    wrong += 1

            percentage = (score / total) * 100

            print("\n================================")
            print("           QUIZ RESULT")
            print("================================")
            print("Student Name:", name)
            print("Total Questions:", total)
            print("Correct Answers:", score)
            print("Wrong Answers:", wrong)
            print("Percentage:", percentage, "%")

            if percentage >= 90:
                print("Result: Excellent!")
            elif percentage >= 70:
                print("Result: Very Good!")
            elif percentage >= 50:
                print("Result: Good Effort!")
            else:
                print("Result: Keep Learning!")

            print("================================")

            retry = input("\nDo you want to take the quiz again? (Y/N): ").upper()

            if retry == "Y":
                print("\nRestarting quiz...")
            else:
                print("\nReturning to the main lesson.")
                retry = "N"

    # ======================================
    # EXIT LESSON
    # ======================================

    elif choice == "12":

        print("\n==========================================")
        print("Thank you for using Python Learning Academy!")
        print("Keep practicing and continue learning.")
        print("==========================================")
        break

    else:

        print("\nInvalid choice!")
        print("Please enter a number from 1 to 12.")
