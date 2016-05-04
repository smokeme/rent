#!/usr/bin/env python

import csv
import os
import sys

sys.path.append('..')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

from main.models import Gov, Area 

dir_path = os.path.dirname(os.path.abspath(__file__)) 

city_csv = os.path.join(dir_path, 'list_city.csv')

csv_file = open(city_csv, 'r')

reader = csv.DictReader(csv_file)
#"zip_code","latitude","longitude","city","state","county"
for row in reader:
	try:
		gov, created = Gov.objects.get_or_create(name=row['Governorate'])
		gov.save()
	except Exception, e:
		print e
	print row['Governorate']
	print row['English']
	print gov
	try:	
		new_area, created = Area.objects.get_or_create(name=row['English'])
		
		new_area.gov = gov
		
		new_area.save()
	except Exception, e:
		print e
	



