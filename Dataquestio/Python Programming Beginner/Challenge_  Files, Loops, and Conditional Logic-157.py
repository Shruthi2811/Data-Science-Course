## 3. Read the File Into a String ##

file = open('dq_unisex_names.csv','r')
names = file.read()

## 4. Convert the String to a List ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split('\n')
first_five = names_list[:5]
print(first_five)

## 5. Convert the List of Strings to a List of Lists ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split('\n')
nested_list = []
for lst in names_list:
    comma_list = lst.split(',') 
    nested_list.append(comma_list)
print(nested_list[:5])    

## 6. Convert Numerical Values ##

print(nested_list[0:5])
numerical_list = []
for item in nested_list:
    name = item[0]
    value = float(item[1])
    numerical_list.append([name,value])
print(numerical_list[:5])    

## 7. Filter the List ##

# The last value is ~100 people
numerical_list[len(numerical_list)-1]
thousand_or_greater = []
for item in numerical_list:
    if item[1] >= 1000:
        thousand_or_greater.append(item[0])
print(thousand_or_greater[:5])        