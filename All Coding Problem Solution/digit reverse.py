Write a program to reverse digits of a number


n = 4562
rev = 0
while(n > 0): 
	a = n % 10
	rev = rev * 10 + a 
	n = n // 10

print(rev) 

