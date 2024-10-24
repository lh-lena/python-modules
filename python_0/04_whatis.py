import sys

n = len(sys.argv)
if (n > 2):
	print("AssertionError: argument is not an integer")
elif (n == 2):
	if int(sys.argv[1]) % 2 != 0: print("I'm Odd.")
	elif int(sys.argv[1]) % 2 == 0: print("I'm Even.")
