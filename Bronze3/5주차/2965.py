#캥거루
a,b,c = map(int, input().split())
print(max(b-a-1, c-b-1))