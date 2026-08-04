"""Task 5"""

amount = int(input('Enter amount in rubles: '))
dollar_exchange_rate = float(input('Enter dollar exchange rate: '))
dollars = amount / dollar_exchange_rate

answer = input('Do you want to know the amount in euro? yes/no: ').lower()

if answer == 'yes':
    euro_exchange_rate = float(input('Enter euro exchange rate: '))
    euros = amount / euro_exchange_rate
    print(euros)
else:
    print(dollars)
