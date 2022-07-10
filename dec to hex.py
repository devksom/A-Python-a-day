#Convert Decimal to hexadecimal 
#place conversion table in a dictionary
conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
					5: '5', 6: '6', 7: '7',
					8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
					13: 'D', 14: 'E', 15: 'F'}


# function to convert decimal value to hexadecimal value

def dectohex(dec):
	hex = ''
    #while decimal (dec) is greater than 0, continue dividing by 16 to get a remainder (rem)
    #match the rem (as key) through the dictionary (conversion_table) to get it's value (in string)
	while(dec > 0):
		rem = dec % 16
		hex = conversion_table[rem] + hex
		dec = dec // 16
        
	return hex
#receive user input
user_dec_input=int(input('Please Enter decimal value to be converted '))
#display result
print("The hexadecimal form of", user_dec_input,
	"is", dectohex(user_dec_input))
