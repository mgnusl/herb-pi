# Herb Pi - An automatic watering system for herbs and other plants

SKRIVE INTRO HER OG LEGGE TIL LINK TIL INSTRUCTABLE


### Project setup
**Dependencies:**
-	Python
-	pip
-	Virtualenv (`pip install virtualenv`)

**Setup:**

1.	Set up virtualenv: `virtualenv env`
	
2. 	Activate virtualenv: `source env/bin/activate`
 	
3.  Install requirements `pip install -r requirements.txt`
  
4.	Setup database `python manage.py migrate`
	
5. 	Load initial plant data `python manage.py loaddata plants/fixtures/initial_data.json`

6. 	Start local web server: `python manage.py runserver`
 	
7. 	Visit [http://localhost:8000/](http://localhost:8000/) to see if everything is set up properly


### REST endpoints
-   `api/plants/` *(GET, POST)*
-   `api/plant/{id}` *(GET, PUT, DELETE)*

-   `api/plantinstances/` *(GET, POST)*
-   `api/plantinstance/{id}` *(GET, PUT, DELETE)*

-   `api/wateringlog/{fk}` *(GET*)

-   `api/moisturelog/{fk}` *(GET*)


### Credit to...

Thanks to tsaiDavid for a friendly introduction to Redux + React through [simple-redux-boilerplate][1]

[1]: https://github.com/tsaiDavid/simple-redux-boilerplate
