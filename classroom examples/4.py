a=[2,4,6,7,8,9,100,3,123,456,3,4,12]

#break when 100 is found
for x in a:
    print(x,end=" ")
    if x == 100:
        break

#skip all 3 digit numbers
for x in a:
    if x > 99:
        continue
    print(x)
