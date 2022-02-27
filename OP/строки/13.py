s1 = 'acrd'
s2 = 'abacrdf'
ls1 = len(s1)
for i in range(len(s2)-ls1+1):
    if s2[i: i + ls1] == s1:
        #print(s2[i: i + ls1])
        print('yes')
        break
else:
    print('no')
    #print(s2[i: i + ls1])
#
# s1 = 'a?rd'
# s2 = 'abac?df'
# ls1 = len(s1)
#
# for i in range(len(s2)-ls1+1):
#     check = True
#     text = s2[i: i + ls1]
#     #print(s2[i: i + ls1], s1)
#     for i in range(len(text)):
#         #print(text[i], s1[i])
#         if text[i] == s1[i] or text[i] == '?' or s1[i] == '?':
#             #print(s2[i: i + ls1], s1)
#             continue
#         else:
#             check = False
#     if check == True:
#         print(text, s1)
#         break
# print(check)
#     if s2[i: i + ls1] == s1:
#         #print(s2[i: i + ls1])
#         print('yes')
#         break
# else:
#     print('no')
#     #print(s2[i: i + ls1])