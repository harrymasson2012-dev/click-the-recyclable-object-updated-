

numbers = [1,5,4,3,7,2]

# print(sum(numbers)/len(numbers))

max_number = 0
for i in range(len(numbers)):
    if max_number > numbers[i]:
        max_number = numbers[i]

print(max_number)