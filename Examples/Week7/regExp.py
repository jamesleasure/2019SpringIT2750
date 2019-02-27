
import re

numbers = {'second': 2, 'first': 1, 'third': 3, 'fourth': 4}
print(f"Unsorted: {numbers}")

keyListSorted = sorted(numbers)
print(keyListSorted)

valuesListSorted = sorted(numbers.values())
print(valuesListSorted)

print(numbers)
print(sorted(numbers))

for key in sorted(numbers.keys()):
    print(key, ": ", numbers[key])


myList = [3, 7, 1, 5, 2]
print(sorted(myList))
print(sorted(myList, reverse=True))


str = "The rain in Spain"
#Find all lower case characters alphabetically between "a" and "m":
x = re.findall("[a-m]", str)
print(x)

domain = "http://wwW9.google.com"
x = re.search("[hztp://]*[\w-]*.*google.com", domain)
print(x)


str = "he9&o world"
#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
x = re.findall("he..o", str)
print(x)


strExample = "192345567"
x = re.search("123z", strExample)
print(x)



str = "james.leasure@tri-c.edu"
x = re.findall("Z", str)
print(x)

if (x):
  print("Yes, it is a valid email address!")
else:
  print("Not a valid email address")
