import sys

total_arg = len(sys.argv)

print("Script name:",sys.argv[0])
print("Number of argument:",total_arg)

print("Arguments:")
for i in sys.argv:
    print(i)
