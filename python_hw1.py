
arr = []
loc = []
dic = {}

dic['row'] = int(input("Enter row: "))
dic['col'] = int(input("Enter column: "))
print()

for r in range (dic['row']):
    row = []
    print(f"Row {r + 1}")
    for c in range(dic['col']):
        while True:
            num = float(input(f"Enter Number {c + 1}: "))
            row.append(num)
            break
    arr.append(row)
print()
for dis in arr:
    print(" ".join(f"{num:g}" for num in dis))
while True:
    searchNum = float(input("Search: "))
    for ro in range (dic['row']):
        for co in range (dic['col']):
            if arr[ro][co] == searchNum:
                loc.append((ro,co))


    if loc:
        print(f"Number {searchNum:g} found at ", end="")
        locDict = {locate: f"Row {locate[0]+1}, Col {locate[1]+1}" for locate in loc}

        for i, loc_tuple in enumerate(loc):
            print(locDict[loc_tuple], end= "")
            if i < len (loc) - 1:
                print(" and ", end= "")
            print(", ")
        break
    else:
        print(f"Number {searchNum:g} not found")
        
# if loc:
#     print(f"Number {searchNum:g} found at ", end="")
#     locDict = {locate: f"Row {locate[0]+1}, Col {locate[1]+1}" for locate in loc}

#     for i, loc_tuple in enumerate(loc):
#         print(locDict[loc_tuple], end= "")
#         if i < len (loc) - 1:
#             print(" and ", end= "")
#         print(", ")
# else:
#     print(f"Number {searchNum:g} not found")