## api
- http://localhost:9000/api/registration
method: POST
data: {
    "login": "v",
    "password": "1234",
    "email": "pipiska@email.com"
}
response: {
    "access_token": "jwt_token",
    "success": true
}

- http://localhost:9000/api/auth
method: POST
data: {
    "login": "v",
    "password": "1234",
}
response: {
    "access_token": "jwt_token",
    "success": true
}

  - http://localhost:9000/api/categories
  method: POST
  data: {
      "category_name": "transport",
      "color" = "ffffff"
  }
  response: {
      "success": true
  }
  method: GET
  response: [{
        "id": 1, 
        "category_name": "transport", 
        "color": "ffffff"
  }]

- http://localhost:9000/api/money_management
  method: POST
  data: {
      "category_name": "transport",
      "color" = "ffffff"
  }
  response: {
      "success": true
  }
  method: GET
  response: [{
        "id": 1, 
        "category_name": "transport", 
        "color": "ffffff"
  }]