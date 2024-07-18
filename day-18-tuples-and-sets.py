# tuples are immutable
months = ('jan', 'feb', 'march', 'april', 'may', 'june', 'july', 'aug', 'sept', 'oct', 'nov', 'dec')

#accessing data
print(months[0])

#data cannot be changes -> this will result in an error
months[0] = 'january'

#sets
countries = ['singapore', 'malaysia', 'vietnam', 'thailand', 'singapore', 'malaysia', 'vietnma', 'thailand', 'tokyo', 'germany', 'america','tokyo', 'germany', 'america', 'tokyo', 'germany', 'america'] 
countries = list(set(countries))
print(countries)

#calculating number of unique countries
print(len(countries))