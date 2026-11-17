# ----------1
# with open("file1.txt","r") as f:
#   rs=f.read()
# vow="aAeEiIoOuU"
# cnt=0
# for i in rs:
#   if i in vow:
#     cnt+=1
# print("no.of vowels= ",cnt)

#----------2
# with open("file1.txt") as f:
#   rs2=f.readlines()
# print("Total no.of lines= ",len(rs2))
# print("2nd line : ", rs2[1])
# print("4th line : ", rs2[3])

#------3
# sent=input("Enter a string: ")
# sent_list=sent.split()
# print(sent_list)
# lword=""
# for i in sent_list:
#   if len(lword)<len(i):
#     lword=i
# print("longest word is : ",lword)

#--------4
with open("file1.txt") as f:
  rs3=f.read()
rs_list=rs3.split()
print("Total no.of words in the file : ",len(rs_list))
uni_rs=set(rs3.split())
print("Unique words in the file : ",uni_rs)