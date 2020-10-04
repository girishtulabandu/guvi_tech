numbers = list()
i = 0
print("Please provide three numbers: ")
while i < 3:
    try:
        n = int(input())
        numbers.append(n)

        i = i + 1
    except ValueError:
        print("Invalid number entered. Please only enter integers.")
        i = 3

if len(numbers) == 3:
    largest_number = max(numbers)
    print("The largest number given is: ", largest_number)
