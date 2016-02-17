# EiT - IT for en bedre verden - Group 5


### Project setup
**Dependencies:**
-	Python
-	pip
-	Virtualenv (`pip install virtualenv`)

**Setup:**

1.	Set up virtualenv: `virtualenv env`
	
2. 	Activate virtualenv: `source env/bin/activate`
 	
3.  Install requirements `pip install -r requirements.txt`
  
4.	`python manage.py migrate`
	
5. 	`python manage.py loaddata plants/fixtures/initial_data.json`
 	
6. 	Start local web server: `python manage.py runserver`
 	
7. 	Visit [http://localhost:8000/plants/](http://localhost:8000/plants/)



### Notes
-	A `Plant` is a 'static' database field that contains information about each chooseable plant type (humidity, name etc).

- 	A `PlantInstance` is an actual/concrete instance of a `Plant`

-	Each `PlantCollection` contains zero or many `PlantInstances`
-	Each `PlantInstance` is contained in one `PlantCollections`
