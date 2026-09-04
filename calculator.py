def main():
	first_number = float(input("Enter first number: "))
	operator = input("Enter operator (+, -, *, /): ")
	second_number = float(input("Enter second number: "))

	if operator == "+":
		result = first_number + second_number
	elif operator == "-":
		result = first_number - second_number
	elif operator == "*":
		result = first_number * second_number
	elif operator == "/":
		if second_number == 0:
			print("Error: cannot divide by zero.")
			return
		result = first_number / second_number
	else:
		print("Error: invalid operator.")
		return

	print(f"Result: {result}")


if __name__ == "__main__":
	main()
