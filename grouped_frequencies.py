#Dataquest Dictionaries and Frequency tabkes

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
rating_counts = []
rating_frequency = {'0 - 600000 ratings': 0, '600000 - 1200000 ratings': 0, '1200000 - 1800000 ratings': 0, '1800000 - 2600000 ratings': 0, '2600000 ratings +': 0}

for row in apps_data[1:]:
    rating_count = float(row[5])
    rating_counts.append(rating_count)
    total_ratings = len(rating_counts)
    min_rating = min(rating_counts)
    max_rating = max(rating_counts)
    
    
for rating_count in rating_counts:
    if rating_count <= 600000:
        rating_frequency['0 - 600000 ratings'] += 1
    elif 600000 < rating_count <= 1200000:
        rating_frequency['600000 - 1200000 ratings'] += 1
    elif 1200000 < rating_count <= 1800000:
        rating_frequency['1200000 - 1800000 ratings'] += 1
    elif 1800000 < rating_count <= 2600000:
        rating_frequency['1800000 - 2600000 ratings'] += 1
    elif rating_count > 2600000:
        rating_frequency['2600000 ratings +'] += 1

print('Total number of apps:', total_ratings)
print('Rating frequecy:', rating_frequency)
print('Total (check):', sum(rating_frequency.values()))
