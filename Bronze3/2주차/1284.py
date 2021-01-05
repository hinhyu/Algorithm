while True:
  n = input()
  if n == '0': break
  a = 2+ 3*len(n) + n.count('0') - n.count('1') + (len(n)-1)
  print(a)

#실패한 코드....애초에 len이나 count나 리스트 한정이 아니었다..
# a=0
# b=0
# c=0
# while True:
#     num_list = list(map(int,input()))
#     d=len(num_list) -1
#     if num_list == '0' : break
#     for i in num_list:
#         if num_list[i] == 1:
#             a = a+2
#         elif num_list[i] == 0:
#             b = b+4
#         else:
#             c = c + 3
#     print(a+b+c+d+2)
#     num_list = []
