# f = open("sample.txt","w")
# f.write('Hello File')
# f.close()
#
# f = open("sample.txt1","w")
# f.write('Hello File1')
# f.write("\nHow are you")
# f.close()
#
# f = open("sample.txt1","a")
# f.write("\nI am fine")
# f.close()
#
#
# l = ["\nHi","\nHow are you","\nI am Fine"]
# f = open("sample.txt1", "a")
# f.writelines(l)
#
# f = open("sample.txt1","r")
# s = f.read()
# print(s)
# f.close()
#
# f = open("sample.txt1","r")
# while True:
#     data = f.readline()
#
#     if data == '':
#         break
#     else:
#         print(data,end='')
# f.close()
#
#
# # with
# with open("sample.txt", "a") as f:
#     f.write("\n Hey")
#
# Big_L = ["Hello World\n" for i in range(1000)]
# with open("Big.text", "w") as f:
#     f.writelines(Big_L)
#
#
# with open("Big.text","r") as f:
#     chunk_size = 100
#     while len(f.read(chunk_size)) > 0:
#         print(f.read(chunk_size),end = "")
#         f.read(chunk_size)
#


#tell function
# with open("Big.text","r") as f:
#     print(f.read(100))
#     print(f.tell())
#     f.seek(0)
#     print(f.read(100))
#     print(f.tell())


# #Seek during write
# with open("sample.txt","w") as f:
#     f.write("Hello")
#     f.seek(0)
#     f.write("Xa")

# Working with binary file
with open("image_1.png","rb") as f:
    with open("image_1_copy.png","wb") as fw:
        fw.write(f.read())