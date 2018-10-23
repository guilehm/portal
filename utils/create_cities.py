import csv

from register.models import City

cities_to_create = []
with open('utils/cities_ibge.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        cities_to_create.append(City(
            ibge_code=row[0],
            name=row[1],
            state_code=row[3],
            state=row[4],
            SIC=row[6],
            SCI=row[7],
        ))

City.objects.bulk_create(cities_to_create)
