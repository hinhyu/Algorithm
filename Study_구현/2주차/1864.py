l = ['-','\\','(','@','?','>','&','%']
while True:
  n = list(input())
  if n[0] =='#': break
  for i in range(len(n)):
     for j in l:
       if n[i] == j : 
         n[i] = l.index(j)
       elif n[i] == '/' :
          n[i] = -1
  a = 0
  for i in range(len(n)):
    a += n[i]*(8**(len(n)-1-i))
  print(a)