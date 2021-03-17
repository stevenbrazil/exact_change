total_change = int(input())
#converting total change
dollar_count = total_change // 100
quarter_count = total_change % 100 // 25
dime_count = total_change % 25 // 10
nickel_count = total_change % 25 % 10 // 5
penny_count = total_change % 5
#use of tenery to display one of more coins
more_than1_dollar = 'Dollar' if dollar_count == 1 else 'Dollars'
more_than1_quarter = 'Quarter' if quarter_count == 1 else 'Quarters'
more_than1_dime = 'Dime' if dime_count == 1 else 'Dimes'
more_than1_nickel = 'Nickel' if nickel_count == 1 else 'Nickels'
more_than1_penny = 'Penny' if penny_count == 1 else 'Pennies'

if total_change <= 0:
    print('No change')

if dollar_count > 0:
    print(dollar_count, more_than1_dollar)

if quarter_count > 0:
    print(quarter_count, more_than1_quarter)

if dime_count > 0:
    print(dime_count, more_than1_dime)

if nickel_count > 0:
    print(nickel_count, more_than1_nickel)

if penny_count > 0:
    print(penny_count, more_than1_penny)
