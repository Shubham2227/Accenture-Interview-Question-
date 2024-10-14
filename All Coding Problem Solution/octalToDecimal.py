Program for Octal to Decimal Conversion


def octalToDecimal(n): 
	num = n 
	dec_value = 0
	base = 1
	temp = num 
	while (temp): 
		last_digit = temp % 10
		temp = int(temp / 10) 
		dec_value += last_digit * base 
		base = base * 8
	return dec_value 
num = 123
print(octalToDecimal(num)) 
