# This function greets a person
# def greet(person):
#   print("Hello", person)
#   print("How are you?")

# greet("Laura!")

# This function gives you 10 random numbers...exemplifies the for loop and range function
# def main():
#   print("This program is crazy!")
#   x = eval(input("Enter a number between 0 and 1: "))
#   for i in range(10):
#     x = 3.9 * x *(1-x)
#     print(x)

# main()

# This function changes celsius into farenheit
# def temp():
#   celsius = eval(input("What is the temp in celsius? "))
#   farenheit = celsius*(9/5) + 32
#   print("The temp in farenheit is ", farenheit, "degrees!!!")
#   if farenheit > 90:
#     print("HEAT WARNING!!!")
#   elif farenheit < 30:
#     print("COLD WARNING!!!")

# temp()

# This is an example of how to print on one line
# print("The answer is", end = " ")
# print(3 + 4)

# This function averages the scores of two exams
# def main():
#   print("This program averages the scores of two exams.")
#   score1, score2 = eval(input("Enter your scores separated by a comma: "))
#   average = (score1 + score2)/2
#   print("The average score is: ", average)

# main()

# This is for calculating how much your money will grow by.
# def main():
#   principal = eval(input("What is the amount of principal? "))
#   apr = eval(input("What is the annual percentage rate? "))
#   for i in range(10):
#     principal = principal * (1 + apr)
#   print("The value after 10 years will be", principal)

# main()

# This function finds the roots using the quadratic equation
# import math
# def main():
#   a, b, c = eval(input("Please input your coefficients: a, b, c: "))
#   discrim = b * b - 4 * a * c
#   if discrim > 0:
#     discRoot = math.sqrt(discrim)
#     root1 = (-b + discRoot)/(2 * a)
#     root2 = (-b - discRoot)/(2 * a)
#     print("The roots are: ", root1, root2)
#   elif discrim == 0:
#     root = -b/(2*a)
#     print("There is a double root at", root)
#   else:
#     print("\nThe equation has no real roots!")

# main()

# This function computes the factorial of a number
# def main():
#   n = eval(input("What is the number? "))
#   factorial = 1
#   for factor in range(n, 1, -1):
#     factorial = factorial * factor
#   print("The factorial of", n, "is", factorial)

# main()

# Finds the greatest of 3 numbers, not a the most efficient approach, but the easiest to write
# def main():
#   x1, x2, x3 = eval(input("What are the three numbers? "))
#   if x1 >= x2 and x2 >= x3:
#     max = x1
#   elif x2 >= x1 and x2 >= x3:
#     max = x2
#   else:
#     max = x3
#   print("The largest number is", max)

# main()

# Better way to find the greatest of 3 numbers
# def main():
#   x1, x2, x3 = eval(input("What are the three numbers? "))
#   max = x1
#   if x2 > max:
#     max = x2
#   if x3 > max:
#     max = x3
#   print("The biggest number is", max)

# main()

# find the greatest number out of n numbers
# def main():
#   n = eval(input("How many numbers are there? "))
#   max = eval(input("What is the first number? "))
#   for i in range(n-1):
#     x = eval(input("What is the next number? "))
#     if x > max:
#       max = x
#   print("The biggest number is", max)

# main()

# creating a username
# def main():
#   print("This program makes usernames!\n")
#   firstName = input("What is your first name (all lowercase)? ")
#   lastName = input("What is your last name (all lowercase)? ")
#   username = firstName[0] + lastName[:7]
#   print("Your username is", username)

# main()

# This program prints the abbreviation of a month given the month number
# def main():
#   pos = eval(input("What is the month number? "))
#   months = "JanFebMarAprMayJunJulAugSepOctNovDec"
#   # remember: slice goes from first and stops BEFORE last
#   monthAbbrev = months[3*pos - 3: 3*pos]
#   print("The month is", monthAbbrev)

# main()

# This program converts a textual message into a sequence of numbers, using Unicode
# def main():
#   message = input("Please enter the message to be encoded: ")
#   for ch in message:
#     print(ord(ch), end = " ")
#     # end = " " tells it to print a space after the output and print the next output after that
#     # This keeps everything on the same line

# main()

# This program decodes Unicode
# def main():
#   # get the input as a string
#   inString = input("Please enter the numbers: ")
#   # empty variable to store message
#   message = ""
#   # loop through each string of numbers
#   for numStr in inString.split():
#     # convert them into int's
#     codeNum = eval(numStr)
#     # convert the ints into characters and add them to the message
#     message = message + chr(codeNum)
#   print("\nThe message is: ", message)

# main()

# more efficient decoder
# def main():
#   inString = input("Please enter the numbers: ")
#   chars = []
#   for numStr in inString.split():
#     codeNum = eval(numStr)
#     chars.append(chr(codeNum))
#   message = "".join(chars)
#   print("\nThe decoded message is: ", message)

# main()

# Converts a date in form "mm/dd/yyyy" to "month day, year"
# def main():
#     # get the date
#     dateStr = input("Enter a date (mm/dd/yyyy): ")
#     # split into components
#     monthStr, dayStr, yearStr = dateStr.split("/")
#     # convert monthStr to the month name
#     months = ["January", "February", "March", "April",
#               "May", "June", "July", "August",
#               "September", "October", "November", "December"]
#     monthStr = months[int(monthStr)-1]
#     # output result in month day, year format
#     print("The converted date is:", monthStr, dayStr+",", yearStr)

# main()

# #    Program to create a file of usernames in batch mode.
# def main():
#     print("This program creates a file of usernames from a")
#     print("file of names.")
#     # get the file names
#     infileName = input("What file are the names in? ")
#     outfileName = input("What file should the usernames go in? ")
#     # open the files
#     infile = open(infileName, "r")
#     outfile = open(outfileName, "w")
#     # process each line of the input file
#     for line in infile:
#         # get the first and last names from line
#         first, last = line.split()
#         # create the username
#         uname = (first[0]+last[:7]).lower()
#         # write it to the output file
#         print(uname, file=outfile)
#     # close both files
#     infile.close()
#     outfile.close()
#     print("Usernames have been written to", outfileName)
# main()






