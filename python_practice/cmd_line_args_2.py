##Write a Python program that accepts integers from the command line and prints:

#The sum

#The average

#If any non-numeric value is passed, display an error message.


import sys


summ = 0
count = 0
for i in sys.argv[1:]:
    try:
        summ = summ + int(i)
        count = count + 1
    except ValueError as e:
        print("Only integers allowed:",e)
        sys.exit()
    
if not count == 0:
    print("Sum:",summ)
    print("avg:",summ/count)
else:
    print("give some num as arguments")
