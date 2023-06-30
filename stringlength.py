string=input("Enter a string")

sp=0 #space
al=0 #alphabets
dg=0 #digits 
nr=0 #numericals 

for i in range(0,len(string)):  # for each character in string 
    if string[i].isspace():     # search through each index of string 
        sp=sp+1
    if string[i].isdigit():
        dg=dg+1
    if string[i].isalpha():
        al=al+1
    if string[i].isnumeric():
        nr=nr+1

length=sp+dg+al+nr  
print(length)
print("Spaces are %d " %sp)
print("Digits are %d" %dg)
print("Alphabets are %d" %al)
