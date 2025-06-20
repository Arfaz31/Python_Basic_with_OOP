#List
# number=[1,2,3,4,5]
# new_list = number[3:0:-1] #reverse list 3 to 0 index
# print(new_list)

#List comprehension
# numbers = [45, 87, 96, 65, 43, 90, 85, 14, 26, 61, 70]
# odds = []
# for num in numbers:
#     if num % 2 == 1 and num % 5 == 0:
#         odds.append(num)

# Copyodd_numbers = [num for num in numbers if num % 2 == 1 if num % 5 == 0]

# print(Copyodd_numbers)


#nested loop in list comprehension
# players = ['sakib', 'musfik', 'liton']
# ages = [38, 37, 32]

# age_comb = []
# for player in players:
#     for age in ages:
#         age_comb.append([player, age])
        
# print(age_comb)


players = ['sakib', 'musfik', 'liton']
ages = [38, 37, 32]

age_comb = [[player, age] for player in players for age in ages]
print(age_comb)