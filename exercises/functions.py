# Write your solution for 1.4 here!

def is_prime(x):
	i=1
	while i<x:
		if x%i==0:
			if i!=x and i!=1:
				return False
		i=i+1
	return True
print(is_prime(5191))
