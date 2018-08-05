# Write your solution for 1.2 here!
s=0
for i in range(101):
	if i%2==0:
		s=s+i
print(s)

max2=0
max3=0
for j in range(1000):
	if j%6==2:
		max2=j
	if j%3==5:
		max3=j
print(max2)
print(max3)