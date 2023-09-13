API Documentation
Standard Formats
Endpoint: /api/

### GET - Retrieve List of Persons
Request:
  No request body.
  Query Parameters (optional):
  name (string): Filter persons by name

Response:
  Status Code: 200 OK
  Response Body:
  [
  {
    "id": 1,
    "name": "Mark Essien"
  },

  {
    "id": 2,
    "name": "Micheal Smith"
  }
]

### POST - Create a New Person
Request: /api/
Content-Type: application/json
Request Body

 {
  "name": "Mark Essien"
}

Response:
 Status Code: 201 Created
 Response Body
  {
  "id": 3,
  "name": "Mark Essien"
}

### GET - Retrieve a Single Person
Request: 
 /api/<user_id>
 Response:
 Status Code: 200 OK
 Response Body:
 
  {
  "id": 3,
  "name": "Mark Essien"
  }

  ### PUT - Update a Person
Request:
  /api/<user_id>/

Content-Type: application/json
Request Body:
  {
  "name": "Updated Name",
}

Response:
 Status Code: 200 OK
 Response Body:
 {
  "id": 1,
  "name": "Updated Name",
 }


