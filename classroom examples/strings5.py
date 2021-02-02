#string splitting and joining

line = "Ramesh,223,rsannareddy@gmail.com"

fields = line.split(",")
print(fields)

eid = fields[1]

print(eid)


#joining

a = ["how","are","you","doing","today"]


print(" ".join(a))
print("-".join(a))
print("_".join(a))
print("".join(a))
print("\t".join(a))
print("\n".join(a))


