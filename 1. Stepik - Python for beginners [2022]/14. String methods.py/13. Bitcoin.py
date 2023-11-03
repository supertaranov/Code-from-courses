# Complete the above code by formatting the lines using the format method so that it outputs the text: 
# "In 2010, someone paid 10k Bitcoin for two pizzas." (without quotes).

year = 2010
paid = '10k'
coin = 'Bitcoin'
s = 'In {0}, someone paid {1} {2} for two pizzas.'
print(s.format(year, paid, coin))