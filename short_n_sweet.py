def AreNumbersEven(numbers):
  bool_list = []
  for n in numbers:
    bool_list.append(((n % 2) == 0))
  return bool_list

# numbers = raw_input()
numbers = "66 0 -47"
integer_list = [int(i) for i in numbers.split(' ')]
even_odd_boolean_list = AreNumbersEven(integer_list)
print(even_odd_boolean_list)
