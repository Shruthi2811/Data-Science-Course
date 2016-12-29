## 2. Enumerate ##

ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]
for i,item in enumerate(ships):
    print(item)
    print(cars[i])

## 3. Adding Columns ##

things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]
for i, item in enumerate(things):
    item.append(trees[i])

## 4. List Comprehensions ##

apple_prices = [100, 101, 102, 105]
apple_prices_doubled = [(item*2) for item in apple_prices]
apple_prices_lowered = [(item-100) for item in apple_prices]

## 5. Counting Female Names ##

name_counts = {}
for item in legislators:
    if item[3] == 'F' and item[7] > 1940:
        name = item[1]
        if name in name_counts:
            name_counts[name] +=1
        else:
            name_counts[name]=1

## 7. Comparing with None ##

values = [None, 10, 20, 30, None, 50]
checks = []
for item in values:
    status = (item != None and item > 30)
    checks.append(status)

## 8. Highest Female Name Count ##

max_value = None
for item in name_counts.keys():
    count = name_counts[item]
    if (max_value == None or count > max_value):
        max_value = count

## 9. The Items Method ##

plant_types = {"orchid": "flower", "cedar": "tree", "maple": "tree"}
for item,val in plant_types.items():
    print(item)
    print(val)

## 10. Finding the Most Common Female Names ##

top_female_names = []
for item in name_counts.keys():
    if name_counts[item]==2:
        top_female_names.append(item)

## 11. Finding the Most Common Male Names ##

top_male_names = []
male_name_counts ={}
highest_male_count = None
for item in legislators:
    if item[3] == 'M' and item[7] > 1940:
        name = item[1]
        if name in male_name_counts:
            male_name_counts[name] +=1
        else:
            male_name_counts[name]=1

for item in  male_name_counts.keys():
    count =  male_name_counts[item]
    if (highest_male_count == None or count > highest_male_count):
        highest_male_count = count        

for item in male_name_counts.keys():
    if male_name_counts[item]==highest_male_count:
        top_male_names.append(item)        