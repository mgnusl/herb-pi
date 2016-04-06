# EiT - IT for en bedre verden - Group 5


### Project setup
**Dependencies:**
-	Python
-	pip
-	Virtualenv (`pip install virtualenv`)

**Back-end setup:**

1.	Set up virtualenv: `virtualenv env`
	
2. 	Activate virtualenv: `source env/bin/activate`
 	
3.  Install requirements `pip install -r requirements.txt`
  
4.	`python manage.py migrate`
	
5. 	`python manage.py loaddata plants/fixtures/initial_data.json`
 	
6. 	Start local web server: `python manage.py runserver`
 	
7. 	Visit [http://localhost:8000/plants/](http://localhost:8000/plants/) to see if everything is set up properly

**Front-end setup:**

### REST endpoints
-   `api/plants/` *(GET, POST)*
-   `api/plant/{id}` *(GET, PUT, DELETE)*

-   `api/plantinstances/` *(GET, POST)*
-   `api/plantinstance/{id}` *(GET, PUT, DELETE)*

-   `api/wateringlog/{fk}` *(GET*)

-   `api/moisturelog/{fk}` *(GET*)
