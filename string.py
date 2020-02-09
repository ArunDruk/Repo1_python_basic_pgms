####################################################################################################
#String methods : lower(), upper(), replace(), strip(), find(), count(),


# str="ArunKiranarununarun"
# str=str.lower()
# r=str.replace("arun","kiran")
# k=str.replace("arun","kiran",1) #number of times it has to replace, by default it will replace completely.
# print(r,r.count("kiran"))
# #print(str,r,k)
# # a=str.count("arun")
# #a=str.count("arun",0,4) #"arun" is to search inside the str and '0' is the start position and '4' is the end position to search for in the string.
# #print(a)
# #f=str.find("kiran") #find : If substring exists inside the string, it returns the index of first occurence of the substring else returns -1.
# #print(f)
# print("Contains substring 'be,'")
####################################################################################################
# import re
# def count_code(a):
#     c=re.sub(r'co[a-z]e',"code",a)
#     d=c.count("code")
#     return d
#
#
# print(count_code('cozexxcope'))
####################################################################################################
# str='cozexxcope'
# a=str.strip()
# print(str,a)
# str='cozexxcope'
# a=re.match(r'co[a-z]e',str)
# # print(a)
# # print(a.group(num=0))
# b=re.sub(r'co[a-z]e',"code",str) #Replaces the searched pattern in the string
# print(b)
# c=b.count("code")
# print(c)

#Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

####################################################################################################
# def count_code(str):
#     str=str.lower()
#     count=0
#     start_str=0
#     while(start_str >= 0):
#         b=str.find("co",start_str)
#         start_str = start_str + len("code")
#         if b<0:
#             break
#         a=slice(b+3,b+4) #Searching for the last character in "code" i,e, 'e'
#         if(str[a]=='e'):
#             count+=1
#     return count
#
# print(count_code('AAcodeBBcoleCCccoreDD'))
####################################################################################################
# def count_code(str):
#     count=0
#     start_str=0
#     while(start_str >= 0):
#         b=str.find("co",start_str)
#         if b<0:
#             break
#         #a=slice(b+3,b+4)
#         if(str[b+3]=='e'):
#             count+=1
#             start_str=start_str+len("code")
#     return count
#
# print(count_code('AAcodeBBcoleCCccoreDD'))
#################################################################
#String Strip : By default it wll strip the whitespace characters at the beginning and the end of the string, particular characters to
# stripped need to be mentioned inside the strip("chars")
# letter="    abcdefghijklmn opqrstu vwxyz"
# print(letter.strip("xyz"))

print("#"*100)