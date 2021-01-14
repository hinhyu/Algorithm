#세 수
import sys
a,b,c= (map(int, sys.stdin.readline().split()))
if a+b==c: print("%d+%d=%d"%(a,b,c)); exit()
elif a-b==c: print("%d-%d=%d"%(a,b,c)); exit()
elif a*b==c: print("%d*%d=%d"%(a,b,c)); exit()
elif int (a/b)==c: print("%d/%d=%d"%(a,b,c)); exit()
elif a==b+c: print("%d=%d+%d"%(a,b,c)); exit()
elif a==b-c: print("%d=%d-%d"%(a,b,c)); exit()
elif a==b*c: print("%d=%d*%d"%(a,b,c)); exit()
elif a== int (b/c): print("%d=%d/%d"%(a,b,c)); exit()