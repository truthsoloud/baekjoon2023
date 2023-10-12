h, m = map(int, input().split())
howlong = int(input())

h+=howlong//60
m+=howlong%60

if m>=60:
	h+=1
	m-=60
	
if h>23:
	h-=24
    
print(h, m)