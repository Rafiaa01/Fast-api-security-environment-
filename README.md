FastAPI Authentication API

A FastAPI project demonstrating API Key and Bearer Token authentication with CORS configuration.

Setup
Create Virtual Environment
python -m venv venv
Activate

Windows:

venv\Scripts\activate

Install Dependencies
pip install -r requirements.txt

Freeze Dependencies
pip freeze > requirements.txt

Deactivate
deactivate

Reinstall Environment
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

Run the API
uvicorn main:app --reload

CORS

CORS (Cross-Origin Resource Sharing) allows or restricts requests from different origins, such as a frontend application communicating with the FastAPI backend.

Authentication
API Key

The client sends an API key using the X-API-Key header. The server validates the key before allowing access to the protected endpoint.

X-API-Key: secret-value
Bearer Token

The client sends a bearer token using the Authorization header. The server validates the token before allowing access.

Authorization: Bearer secret-value
Postman Testing

Postman was used to test:

Successful API Key authentication
Failed API Key authentication
Successful Bearer Token authentication
Failed Bearer Token authentication

Screenshots of the successful and failed requests are included as evidence.

Security

The virtual environment and secrets are not included in the repository.

.gitignore includes:

.venv
.env
Postmann (Testing):

1. API Key — Successful
Method: GET your protected endpoint

Header:

X-API-Key: secret-value
Expected: 200 OK
Screenshot should show the request and successful response.

2. API Key — Failed

Use an incorrect key:

X-API-Key: wrong-key
Expected: 401 Unauthorized
Screenshot.

3. Bearer Token — Successful

Header:

Authorization: Bearer secret-value
Expected: 200 OK
Screenshot.
4. Bearer Token — Failed

Use an incorrect token:

Authorization: Bearer wrong-token
Expected: 401 Unauthorized
Screenshot.