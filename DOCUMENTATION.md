## API Documentation
## Standard Formats
## Endpoint: /api/

### POST - Create a New Person
#### Request: /api/
#### Content-Type: application/json

#### Request Body
 {
  "name": "Mark Essien"
}

#### Response:
#### Status Code: 201 Created;
#### Response Body;
  {
  "id": 3,
  "name": "Mark Essien"
}

### GET - Retrieve a Single Person;
#### Request:
 /api/<user_id>
#### Response: 
 Status Code: 200 OK;
 #### Response Body: 
  {
  "id": 3,
  "name": "Mark Essien"
  }

  ### PUT - Update a Person
 #### Request:
  /api/<user_id>/;
 #### Content-Type: application/json;
Request Body: ;
  {
  "name": "Updated Name",
}

#### Response: ;
#### Status Code: 200 OK;
 Response Body:
 {
  "id": 1,
  "name": "Updated Name",
 }
### DELETE - Delete a person
  #### Request:
    /api/<user_id>/
  #### Response:
  - status Code: 204 No Content


## SAMPLE USAGE

- You can access these endpoints by adding '/api/' to your base URL.

##### EXAMPLES

##### Retrieve Persons
- GET http://localhost:8000/api/

##### Create new Person
- POST -H "Content-Type: application/json" -d '{'name': "Mark Essien"}' http://localhost:8000/api/

##### Retrieve a single Person
- GET http://localhost:8000/api/1

##### Update a Person
- PUT -H "Content-Type: application.json" -d '{"name": "Updated Name"}' http://localhost:8000/api/1

##### Retrieve Persons
- DELETE http://localhost:8000/api/1


### Limitations and Assumptions
- The API assumes that each user has a unique identifier ( 'id )
- Pagination and advanced filtering are not implemented in this verson of the API


















