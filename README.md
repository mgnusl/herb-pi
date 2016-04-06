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
 	
7. 	Visit [http://localhost:8000/plants/](http://localhost:8000/plants/)

**Front-end setup:**

Requirements

`Node 5.0.0` or higher is required.

Install dependencies

1. From web-app directory run `npm install` to setup dependencies

Start development server, and get to work!

1. From web-app directory run `npm run dev`, this will provide module bundling with hot reloading

2. Open your favorite web browser and visit `http://localhost:3000/`, your now ready for work! 

Build Bundle

1. From `web-app` folder run `npm run build` to bundle all modules into a single`bundle.js`, which can be located under `web-app/dist`

Credit to..

Thanks to tsaiDavid for a friendly introduction to Redux + React through [simple-redux-boilerplate][1]

### Notes
-	A `Plant` is a 'static' database field that contains information about each chooseable plant type (humidity, name etc).

- 	A `PlantInstance` is an actual/concrete instance of a `Plant`

-	Each `PlantCollection` contains zero or many `PlantInstances`
-	Each `PlantInstance` is contained in one `PlantCollections`


[1]: https://github.com/tsaiDavid/simple-redux-boilerplate

