
#question 1
# i
from itertools import count
from random import random


roll=1024160046
n=len(str(roll))
l=[]
for i in range(n):
    l.append(int(str(roll)[i])*10)
print(l)
# ii
a=57
l.append(a)
l.insert(3, 7)
print(l)
#iii
l.pop()
print(l)
l.remove(7)
print(l)
#iv
l.sort
print(l)
l.sort(reverse=True)
print(l)
#v
print(l[:3],l[-3:])
#vi
for i in range(n):
    l.append(int(str(roll)[i])*10)
for i in range(len(l)):
    avg= sum(l)/len(l)
    list=[]
    if l[i]>avg:
        list.append(l[i])
print(list)



# question 2
# i
t=(10,0,20,40,10,60,0,0)
filtered_items = [(val, idx) for idx, val in enumerate(t) if val != 0]

non_zero_vals = [val for val, idx in filtered_items]
max_val = max(non_zero_vals)
min_val = min(non_zero_vals)

max_positions = [idx for val, idx in filtered_items if val == max_val]
min_positions = [idx for val, idx in filtered_items if val == min_val]

print(f"Max Value: {max_val}, Frequency: {len(max_positions)}, Positions: {max_positions}")
print(f"Min Value: {min_val}, Frequency: {len(min_positions)}, Positions: {min_positions}")


# ii
lis=list(t)
lis.sort(reverse=True)
print(lis)
   ## the list is immutable whereas tuple is immutable so to do any modification we need to convert tuple into list first and then we can do any
   #  modification and then we can convert it back to tuple if needed.

#iii
a=int(input("Enter a score: "))
if a in t:
    print("Score is present in the tuple at",i)
else:
    print("Score is not present in the tuple")

#iv
t[0]=100
print(t)
   ### the above line will give an error because tuples are immutable and cannot be changed after creation.

#v
first,second,third,fourth,fifth,sixth,seventh,eighth=t
print("First:",first)


#question 3

# i. Set random seed using your roll number
roll_number = 1024160046 
random.seed(roll_number)

# ii. Generate a list of 100 random numbers between 100 and 900
numbers = [random.randint(100, 900) for _ in range(100)]

print("List of 100 random numbers:")
print(numbers)

# Count and print all odd numbers
odd_numbers = [num for num in numbers if num % 2 != 0]

print("\nOdd numbers:")
print(odd_numbers)
print("Number of odd numbers:", len(odd_numbers))


# iii. Count and print all even numbers
even_numbers = [num for num in numbers if num % 2 == 0]

print("\nEven numbers:")
print(even_numbers)
print("Number of even numbers:", len(even_numbers))


# iv. Count and print all prime numbers
def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


# Using list comprehension to build the list of prime numbers
prime_numbers = [num for num in numbers if is_prime(num)]

print("\nPrime numbers:")
print(prime_numbers)
print("Number of prime numbers:", len(prime_numbers))


# v. Find the number occurring most frequently
frequency = {}

for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

most_frequent_number = max(frequency, key=frequency.get)
maximum_frequency = frequency[most_frequent_number]

print("\nMost frequently occurring number:")
print("Number:", most_frequent_number)
print("Occurrences:", maximum_frequency)

#question 4
roll_number = input("Enter your roll number: ")

digits = [int(digit) for digit in roll_number]

# Create set A and set B
A = {digit * 7 for digit in digits}
B = {digit * 9 for digit in digits}

# v. Print both sets
print("Set A =", A)
print("Set B =", B)


# vi. Union of A and B
union = A.union(B)
print("\nUnion of A and B =", union)


# vii. Intersection of A and B
intersection = A.intersection(B)
print("Intersection of A and B =", intersection)


# viii. Difference between A and B
A_minus_B = A.difference(B)
B_minus_A = B.difference(A)

print("A - B =", A_minus_B)
print("B - A =", B_minus_A)

print("difference() gives the values present in one set but not in the other, "
      "while symmetric_difference() gives values present in either set but not both.")


# ix. Symmetric difference
symmetric_diff = A.symmetric_difference(B)
print("Symmetric Difference =", symmetric_diff)


# x. Check subset and superset
print("\nIs A a subset of B?", A.issubset(B))
print("Is B a superset of A?", B.issuperset(A))


# xi. Ask user for X and discard it from A
X = int(input("\nEnter a value X to remove from set A: "))

A.discard(X)

print("Set A after discarding X =", A)

print("discard() is safer than remove() because it does not raise an error "
      "if the value is not present in the set.")


#question 5
# Original dictionary
my_dict = {
    "name": "Vandini",
    "roll_no": "1024160046",
    "branch": "CSE",
    "age": 20,
    "city": "Gurugram"
}

print("Original Dictionary:")
print(my_dict)


# i. Rename "city" to "location" using pop()
my_dict["location"] = my_dict.pop("city")

print("\nAfter renaming city to location:")
print(my_dict)


# ii. Add a new key "cgpa"
my_dict["cgpa"] = 9.08

print("\nAfter adding CGPA:")
print(my_dict)


# iii. Increase age by 1
my_dict["age"] += 1

print("\nAfter increasing age by 1:")
print(my_dict)


# iv. Delete "branch" using pop() and del in two separate copies

# Copy 1 - using pop()
dict_pop = my_dict.copy()
removed_branch = dict_pop.pop("branch")

print("\nDictionary after deleting branch using pop():")
print(dict_pop)
print("Value returned by pop():", removed_branch)


# Copy 2 - using del
dict_del = my_dict.copy()
del dict_del["branch"]

print("\nDictionary after deleting branch using del:")
print(dict_del)

print("\npop() returns the removed value, while del only deletes the key-value pair "
      "and does not return the removed value.")


# v. Iterate over dictionary using .items()
print("\nKey-value pairs:")

for key, value in my_dict.items():
    print(f"{key} → {value}")


# vi. Check whether "email" exists before accessing it
print("\nChecking for email:")

if "email" in my_dict:
    print("Email →", my_dict["email"])
else:
    print("Email not found. No email has been provided.")


# vii. Create friend's dictionary
friend_dict = {
    "name": "Rahul",
    "roll_no": "87654321",
    "branch": "CSE",
    "age": 21,
    "city": "Chandigarh"
}

# Merge using dictionary unpacking
merged_dict = {**my_dict, **friend_dict}

print("\nFriend Dictionary:")
print(friend_dict)

print("\nMerged Dictionary:")
print(merged_dict)

print("\nWhen both dictionaries have the same key, the value from "
      "the second dictionary (friend_dict) wins.")


# viii. Dictionary comprehension
# Keep only key-value pairs where the value is a string
string_values = {
    key: value
    for key, value in my_dict.items()
    if isinstance(value, str)
}

print("\nDictionary containing only string values:")
print(string_values)

