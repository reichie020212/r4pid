# Test

### Install python3

	sudo apt install python3

### Install virtual environment

	sudo apt-get install python3-venv

### Create virtual environment

	python3 -m venv myvenv

### Activate virtual environment

	source myvenv/bin/activate

### Install Requirements

	python -m pip install --upgrade pip
	pip install -r requirements.txt

### Migrate

	python manage.py migrate

### Runserver

	python manage.py runserver

### Endpoints
	/registration/
	/login/
	/triangle/
	/triangle/<id_of_triangle>/
	/square/
	/square/<id_of_square>/
	/rectangle/
	/rectangle/<id_of_rectangle>/
	/diamond/
	/diamond/<id_of_diamond>/

### Explanation
	Open Postman

	<domain> = localhost:8000 (depends on what port you will going to use)

	url: <domain>/registration/
	method: POST
	purpose: Creation of account
	sample data: {"username": "test_user", "password": "test2", "confirm_password": "test2", "first_name":"first1", "last_name":"last1"}
	output: "User has been created"

	url: <domain>/login/
	method: POST
	purpose: Account Login
	sample data: {"username": "test_user", "password": "test2"}
	output: {
	    "expiry": "2020-08-11T01:24:08.468679Z",
	    "token": "8d75a9ae3032355e687b533a747a0cd67543e727971d745ba805f1276aea61e2"
	}
	Take note of the "token", it will be use on other endpoint

	<token> = "8d75a9ae3032355e687b533a747a0cd67543e727971d745ba805f1276aea61e2"

	url: <domain>/triangle/
	method: POST
	purpose: Create a new object for triangle
	sample data: {"base": 5, "height": 3}
	sample headers: {"Authorization": "Token <token>"}
	output: {
			    "id": 6,
			    "base": 5.0,
			    "height": 3.0
			}

	url: <domain>/triangle/<id_of_triangle>/
	method: PUT
	purpose: Update the triangle object
	sample data: {"base": 7, "height": 8}
	sample headers: {"Authorization": "Token <token>"}
	output: {
			    "id": 6,
			    "base": 7.0,
			    "height": 8.0
			}

	url: <domain>/triangle/<id_of_triangle>/
	method: GET
	purpose: Get the Area and Perimeter triangle object
	sample data: {}
	sample headers: {"Authorization": "Token <token>"}
	output: {
			    "Area": 28.0,
			    "Perimiter": 28.2602916254693
			}

	url: <domain>/triangle/<id_of_triangle>/
	method: DELETE
	purpose: Delete the triangle object
	sample data: {}
	sample headers: {"Authorization": "Token <token>"}
	output: "Object successfully deleted"

	url: <domain>/square/
	method: POST
	purpose: Create a new object for square
	sample data: {"length": 5}
	sample headers: {"Authorization": "Token <token>"}
	output: {
			    "id": 7,
			    "length": 5.0
			}

	url: <domain>/square/<id_of_square>/
	method: PUT
	purpose: Update the square object
	sample data: {"length": 8}
	sample headers: {"Authorization": "Token <token>"}
	output: {
			    "id": 7,
			    "length": 8.0
			}

	url: <domain>/square/<id_of_square>/
	method: GET
	purpose: Get the Area and Perimeter triangle object
	sample data: {}
	sample headers: {"Authorization": "Token <token>"}
	output: {
			    "Area": 64.0,
			    "Perimiter": 32.0
			}

	url: <domain>/square/<id_of_square>/
	method: DELETE
	purpose: Delete the square object
	sample data: {}
	sample headers: {"Authorization": "Token <token>"}
	output: "Object successfully deleted"

	url: <domain>/rectangle/
	method: POST
	purpose: Create a new object for rectangle
	sample data: {"length": 8, "width": 6}
	sample headers: {"Authorization": "Token <token>"}
	output: {
			    "id": 2,
			    "width": 6.0,
			    "length": 8.0
			}

	url: <domain>/rectangle/<id_of_rectangle>/
	method: PUT
	purpose: Update the rectangle object
	sample data: {"length": 9, "width": 7}
	sample headers: {"Authorization": "Token <token>"}
	output: {
			    "id": 2,
			    "width": 7.0,
			    "length": 9.0
			}

	url: <domain>/rectangle/<id_of_rectangle>/
	method: GET
	purpose: Get the Area and Perimeter rectangle object
	sample data: {}
	sample headers: {"Authorization": "Token <token>"}
	output: {
			    "Area": 63.0,
			    "Perimiter": 32.0
			}

	url: <domain>/rectangle/<id_of_rectangle>/
	method: DELETE
	purpose: Delete the rectangle object
	sample data: {}
	sample headers: {"Authorization": "Token <token>"}
	output: "Object successfully deleted"

	url: <domain>/diamond/
	method: POST
	purpose: Create a new object for diamond
	sample data: {"length": 9, "width": 7, "angle": 95}
	sample headers: {"Authorization": "Token <token>"}
	output: {
			    "id": 5,
			    "width": 7.0,
			    "length": 9.0,
			    "angle": 95.0
			}

	url: <domain>/diamond/<id_of_diamond>/
	method: PUT
	purpose: Update the diamond object
	sample data: {"length": 10, "width": 8, "angle": 96}
	sample headers: {"Authorization": "Token <token>"}
	output: {
			    "id": 5,
			    "width": 8.0,
			    "length": 10.0,
			    "angle": 96.0
			}

	url: <domain>/diamond/<id_of_diamond>/
	method: GET
	purpose: Get the Area and Perimeter diamond object
	sample data: {}
	sample headers: {"Authorization": "Token <token>"}
	output: {
			    "Area": 80.0,
			    "Perimiter": 36.0
			}

	url: <domain>/diamond/<id_of_diamond>/
	method: DELETE
	purpose: Delete the diamond object
	sample data: {}
	sample headers: {"Authorization": "Token <token>"}
	output: "Object successfully deleted"