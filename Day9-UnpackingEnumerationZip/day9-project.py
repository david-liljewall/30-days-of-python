# ---------------------------------------------------------------------------- #
#*                         Credit Card Validator Project                        #
# ---------------------------------------------------------------------------- #


# ------------------------------ Luhn Algorithm ------------------------------ #


## The Lunh Algorithm (Luhn Formula) is a checksum formula used to validate credit card umbers, ID numbers, Sim Card numbers, and survey codes on receipts. It's not secure in the sense that it prevents against attacks, but it does protect against accidental errors

# The way we're going to use the algorithm is as follows:
# Remove the rightmost digit from the card number. This number is called the checking digit, and it will be excluded from most of our calculations.
# Reverse the order of the remaining digits.
# For this sequence of reversed digits, take the digits at each of the even indices (0, 2, 4, 6, etc.) and double them. If any of the results are greater than 9, subtract 9 from those numbers.
# Add together all of the results and add the checking digit.
# If the result is divisible by 10, the number is a valid card number. If it's not, the card number is not valid.



# Take card input and remove any leading/trailing whitespace, convert into list
user_input = input( "Please enter a 16 digit credit card number: " ).strip()
credit_card_number = list( user_input )

# Need to convert each element into an integer to do inequality evaluations later
# for index in range( 0, len( credit_card_number ) ):
#     credit_card_number[ index ] = int( credit_card_number[ index ] )

for index in range( 0, len(credit_card_number) ):
    credit_card_number[ index ] = int( credit_card_number[ index ] )
    
# remove rightmost digit from card number and set to variable
checking_digit = credit_card_number.pop()


# reverse order of remaining digits
credit_card_number.reverse()


# take digits w/ even indices and double them. If any > 9, subtract 9
for index in range( 0, len( credit_card_number ) ):
    
    if index % 2 == 0:
        credit_card_number[ index ] *= 2
        
        if credit_card_number[ index ] > 9:
            credit_card_number[ index ] -= 9

# If sum + checking digit is divisible by 10, then it's a valid card number
print( "\n" ) # extra whitespace
      
if ( sum( credit_card_number ) + checking_digit ) % 10 == 0:
    print( f"{user_input} is a valid credit card number!" )
else:
    print( f"{user_input} is NOT a valid credit card number!" )