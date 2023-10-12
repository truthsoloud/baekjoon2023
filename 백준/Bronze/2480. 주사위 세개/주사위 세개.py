a, b, c = map(int,input().split())

if a==b and b==c:
	price=10000+a*1000
elif a==b:
	price=1000+a*100
elif b==c:
	price=1000+b*100
elif a==c:
	price=1000+c*100
else:
    max=a
    if a<b and c<b:
        max=b
    if a<c and b<c:
        max=c 
    price=max*100
print(price)