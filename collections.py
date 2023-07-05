#Bytes and bytearray
#Bytes store data with limit of 1 byte
#Streaming is a sequence of bytes with maximum length of 1 byte 
#1 byte=8 bits. 
#Normal applications dont use bytes 
#Video processing and streaming uses this type of data 
#Limit of size from 0 to 255 (size is 256)
# [] = list - It is mutable. 
# {} = set - It is mutable
# Byte is immutable 
# Bytearray is mutable. It also has a limit of 256

myset={1,2,3,4,1}
mylist=[2,9,5,7,35,26] #Limit of data from 0-255
#mybyte=bytes(mylist) #Bytes and sets are immutabale
mybyte=bytearray(myset) 
print(type(mybyte))
print(myset)

for x in mybyte:
    print(x)

    mylist[3]=100 #Since it is a list, value can be assigned later and changed.
    mybyte[2]=10 