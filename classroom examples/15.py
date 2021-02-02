f=open("marks.csv","r")

for line in f:
    fields = line.split(",")
    name = fields[0]
    marks=[]
    for x in fields[1:]:
        marks.append(int(x))
    average = round(sum(marks) / len(marks),2)
    
    print("The average for {} is {}".format(name,average))
f.close()
