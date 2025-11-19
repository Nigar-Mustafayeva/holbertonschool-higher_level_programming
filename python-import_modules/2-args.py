#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
n=len(argv);
if (n == 1):
    print("1 argument :")
else:
  print(f"{n} argument :")

for i in range(n):
    print(f"{i+1}: {argv[i]}")
