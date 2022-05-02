numbers = [3,5,7,9,10.5]
print('Initial list:',numbers)

numbers.append('python')
print('Appended list:',numbers)
print('List length:',len(numbers))
print('First element:',numbers[0])
print('Last element:',numbers[-1])
print('Elements from 2 to 4:',numbers[1:5])

numbers.remove('python')
print('List without python:',numbers)