#string indexing
#string slicing

a = "Good Morning"

print(a[0]) #prints the first character
print(a[1]) #prints the second character

print(a[-1]) #prints the last character
print(a[-3]) #prints the third last character

#slicing

print(a[5:8]) #prints from index 5 to 7
print(a[:8]) #prints from index 0 to 7
print(a[5:]) #prints from index 5 to end of string

print(a[0:10:2]) #prints every alternate char from index 0 to 9
print(a[0:10:1]) #prints every char from index 0 to 9

print(a[:])      #prints whole string
print(a[::1])    #prints whole string
print(a[::])     #prints whole string
print(a[::-1])   #prints whole string in reverse

