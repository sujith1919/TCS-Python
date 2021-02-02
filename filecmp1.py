#this program compares two files
import filecmp
print filecmp.cmp("1.txt","2.txt")
print filecmp.cmp("1.txt","2.txt",shallow=False)