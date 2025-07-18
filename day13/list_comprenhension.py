# Day 13 Exercises - List Comprehension and Lambda

# 1. Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [num for num in numbers if num <= 0]
print("Negative and zero numbers:", negative_and_zero)
# Output: [-4, -3, -2, -1, 0]

# 2. Flatten the following list of lists of lists to a one dimensional list
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened = [num for sublist1 in list_of_lists for sublist2 in sublist1 for num in sublist2]
print("Flattened list:", flattened)
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3. Create list of tuples with powers (0 to 10)
power_tuples = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print("List of power tuples:")
for tpl in power_tuples:
    print(tpl)

# 4. Flatten the list of countries with uppercase and add 3-letter code
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries = [[
    country[0].upper(), 
    country[0][:3].upper(), 
    country[1].upper()] 
    for [country] in countries]
print("Flattened countries list:")
print(flattened_countries)
# Output: [['FINLAND','FIN','HELSINKI'], ['SWEDEN','SWE','STOCKHOLM'], ['NORWAY','NOR','OSLO']]

# 5. Change the above list to a list of dictionaries
dict_countries = [{'country': country[0].upper(), 'city': country[1].upper()} for [country] in countries]
print("Countries as dictionaries:")
print(dict_countries)
# Output: [{'country': 'FINLAND', 'city': 'HELSINKI'}, ...]

# 6. Change the following list of lists to a list of concatenated strings
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
full_names = [f"{name[0]} {name[1]}" for [name] in names]
print("Full names:")
print(full_names)
# Output: ['Asabeneh Yetayeh', 'David Smith', 'Donald Trump', 'Bill Gates']

# 7. Write a lambda function to calculate slope or y-intercept of linear functions
# y = mx + b => slope = m, intercept = b
# We'll create two lambdas, one for slope given two points, and one for intercept given point and slope

slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else None
intercept = lambda x, y, m: y - m * x

# Example:
m = slope(1, 2, 3, 6)  # slope between points (1,2) and (3,6)
b = intercept(1, 2, m)
print(f"Slope: {m}")
print(f"Intercept: {b}")
