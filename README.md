
# Car Rental 

Designing a API to get top 3 nearest locations from the point we want.

# Hi, I'm Ponith! 👋


## What's this about?


This is a simple GET API build with django and MySQL to get top three nearest locations to the user, with a input of 
latitude and longitude.
## Run Locally
Basic requirement of Xampp, MySQL, Python above 3

Clone the project

```bash
  git clone https://github.com/ran93r1210/Car_Rental.git
```

Go to the project directory

```bash
  cd my-project
```


Setting up virtual environment

```bash
  python -m venv my-name-virtual-env
  source my-name-virtual-env/bin/activate 
```
Install dependencies

```bash
  pip install -r requirements.txt
```
To integrate MySQL with Django

```bash
  python manage.py makemigrations
  python manage.py migrate
```

Start the server

```bash
  python manage.py runserver
```


## Installation

[Documentation](https://github.com/ran93r1210/Car_Rental/blob/main/documentation)

Installation process.


## Running Tests

To run and get result in json, run the following command

```bash
  python basic_api.py
```


## Screenshots
Search view

![App Screenshot](https://github.com/ran93r1210/Car_Rental/blob/main/output_images/Input.png?raw=true)

Add Driver view

![App Screenshot](https://github.com/ran93r1210/Car_Rental/blob/main/output_images/Add_Driver.png?raw=true)

## Result
Web View with located points on map

![App Screenshot](https://github.com/ran93r1210/Car_Rental/blob/main/output_images/Response.png?raw=true)

Basic API Json result

![App Screenshot](https://github.com/ran93r1210/Car_Rental/blob/main/output_images/result.png?raw=true)





## API Reference

#### Get top 3 locations from database

```http
  GET /search/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `search` | `string` | **Required**. Latitude and Longitude |

#### Adding Driver details to database

```http
  GET /AddDriver/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `AddDriver`      | `string` | **Required**. Deatils of the driver |


#### GET details of all cars and drivers in database
```http
  GET /stats/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `stats`      | `string` | **-** |




## Tech Stack

**Client:** HTML, CSS

**Server:** Django


## Lessons Learned

Working with Django, mapbox api, integrations.

## Demo
![gif demo](https://github.com/ran93r1210/Car_Rental/blob/main/output_images/output.gif)


