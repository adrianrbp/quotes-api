### **1. Register a New User (Optional, not OAuth2)**
```sh
curl -X POST http://127.0.0.1:8000/api/users/register/ \
     -H "Content-Type: application/json" \
     -d '{"username": "testuser", "password": "securepassword", "email": "test@example.com"}'
```

**Expected Response (201 Created)**:

```json
{
    "status":"success",
    "data": 
        {
            "id":4,
            "username":"testuser",
            "email":"test@example.com"
        },
    "message":"User registered successfully. Please log in to get your token."}

```

### **2. Create an OAuth2 Application (Admin Panel or Django Shell)**

**Django Admin Panel**:

Django OAuth Toolkit requires an **OAuth2 application** to issue tokens.

1. Create a **superuser**:
```sh
python manage.py createsuperuser
```
2. Login to the Django admin panel at `http://127.0.0.1:8000/admin/`  
    Navigate to **OAuth2 Provider** → **Applications** → **Add**
    
    Fill in:
    
    - **Client type**: `Confidential`
    - **Authorization grant type**: `Resource owner password-based`
    - **User**: (select your superuser or service_user)
    - **Redirect URIs**: (leave empty)
3. Save and copy **Client ID** and **Client Secret**.


**Django Shell**:

```sh
make shell
```

Then:

```python
from oauth2_provider.models import Application
from django.contrib.auth import get_user_model

User = get_user_model()
service_user, created = User.objects.get_or_create(username="service_account")

app = Application.objects.create(
    name="TestApp",
    client_type=Application.CLIENT_CONFIDENTIAL,
    authorization_grant_type=Application.GRANT_PASSWORD,
    user=service_user
)

print(f"Client ID: {app.client_id}")
print(f"Client Secret: {app.client_secret}")
```

Copy the `client_id` and `client_secret` for use in the next requests.



### **3. Obtain an OAuth2 Access Token (Login)**

```sh
export YOUR_CLIENT_ID="your_client_id"
export YOUR_CLIENT_SECRET="your_client_secret"

curl -X POST http://127.0.0.1:8000/api/oauth/token/ \
     -d "grant_type=password" \
     -d "username=service_user" \
     -d "password=securepass" \
     -d "client_id=${YOUR_CLIENT_ID}" \
     -d "client_secret=${YOUR_CLIENT_SECRET}"


curl -X POST http://127.0.0.1:8000/api/oauth/token/ \
     -d "grant_type=password" \
     -d "username=testuser" \
     -d "password=securepassword" \
     -d "client_id=${YOUR_CLIENT_ID}" \
     -d "client_secret=${YOUR_CLIENT_SECRET}"


```

**Expected Response (200 OK):**

```json
{
    "access_token": "ACCESS_TOKEN_VALUE",
    "token_type": "Bearer",
    "expires_in": 36000,
    "refresh_token": "REFRESH_TOKEN_VALUE",
    "scope": "read write"
}
```


### **4. List quotes**

```sh
curl -X GET http://127.0.0.1:8000/api/quotes/ | jq
```

**Expected Response (200 OK, if token is valid)**:

```json
{
  "count": 123,
  "next": "http://127.0.0.1:8000/api/quotes/?page=2",
  "previous": null,
  "results": [
    {
      "id": 25,
      "author": "Timothy Scott",
      "content": "While behavior week contain I mean right.",
      "timestamp": "2025-02-18T06:47:40.530Z"
    }
  ]
}
```

### **5. Retrieve a Single Quote** (GET)

```sh
curl -X GET http://127.0.0.1:8000/api/quotes/25/ | jq
```

**Expected Response (200 OK, if quote exists):**

```json
{
  "id": 25,
  "author": "Timothy Scott",
  "content": "While behavior week contain I mean right.",
  "timestamp": "2025-02-16T16:50:42.976450Z"
}
```





### **6. Create a New Quote** (POST)

```sh
export ACCESS_TOKEN_VALUE="token_value"


curl -X POST http://127.0.0.1:8000/api/quotes/ \
     -H "Authorization: Bearer ${ACCESS_TOKEN_VALUE}" \
     -H "Content-Type: application/json" \
     -d "{
           \"author\": \"John Doe\",
           \"content\": \"Life is what happens when you're busy making other plans.\"
         }" | jq
```

**Expected Response (201 Created):**

```json
{
  "id": 32,
  "author": "John Doe",
  "content": "Life is what happens when you're busy making other plans.",
  "timestamp": "2025-02-18T06:50:00.530Z"
}
```

### **7. Update an Existing Quote** (PUT)

```sh
curl -X PUT http://127.0.0.1:8000/api/quotes/32/ \
     -H "Authorization: Bearer ${ACCESS_TOKEN_VALUE}" \
     -H "Content-Type: application/json" \
     -d "{
           \"author\": \"John Doe\",
           \"content\": \"Updated Quote Content.\"
         }" | jq
```

**Expected Response (200 OK):**

```json
{
  "id": 32,
  "author": "John Doe",
  "content": "Updated Quote Content",
  "timestamp": "2025-02-18T06:52:00.530Z"
}
```

### **8. Partially Update a Quote** (PATCH)

```sh
curl -X PATCH http://127.0.0.1:8000/api/quotes/32/ \
     -H "Authorization: Bearer ${ACCESS_TOKEN_VALUE}" \
     -H "Content-Type: application/json" \
     -d "{
           \"content\": \"This is a partially updated quote.\"
         }" | jq
```

**Expected Response (200 OK):**

```json
{
  "id": 32,
  "author": "John Doe",
  "content": "This is a partially updated quote.",
  "timestamp": "2025-02-18T06:55:00.530Z"
}
```

### **9. Delete a Quote** (DELETE)

```sh
curl -X DELETE http://127.0.0.1:8000/api/quotes/32/ \
     -H "Authorization: Bearer ${ACCESS_TOKEN_VALUE}"
```

**Expected Response (204 No Content, Quote Deleted Successfully):**  
No response body.


### **10. Retrieve a random Quote** (GET)

```sh
curl -X GET http://127.0.0.1:8000/api/quotes/random/ | jq
```

**Expected Response (200 OK):**
```json
{
  "status": 200,
  "message": "Random quote retrieved successfully",
  "data": {
    "id": 27,
    "author": "Gina Sullivan",
    "content": "Act behavior produce son attention local serve.",
    "timestamp": "2025-02-16T16:50:42.979471Z"
  }
}

```
