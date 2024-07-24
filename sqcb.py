#this is the simple square , cube and power calulator

import math

def main():
				print("Select Operator ")
				print("1 for the square ")
				print("2 for the cube ")
				print("3 for the powerto ")
				print("4 for the square root ")
				op = int(input("Enter the operator: "))
				first = int(input("Enter the first number: "))
				calc(op , first)
				
def calc(op , first):
				if op == 1:
								print(first ** 2)
				elif op == 2:
								print(first ** 3)
				elif op == 3:
								second = int(input("Enter the second: "))
								print(pow(first , second))
				elif op == 4:
								print(math.sqrt(first))
				else:
								print("INVALID")
				
				
main()