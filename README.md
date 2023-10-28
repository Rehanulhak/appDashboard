
# Django App Dashboard

This project provides a backend service for an app dashboard where users can manage all their apps under their account. It uses Django and Django Rest Framework.

## API Endpoints

### 1. User Registration, Login, and Password Reset:

**Registration**:
- Endpoint: `/auth/users/`
- Method: `POST`
- Payload: 
```json
{
"username": "your_username",
"password": "your_password",
"email": "your_email@example.com"
}
```

**Login**:
- Endpoint: `/auth/token/login/`
- Method: `POST`
- Payload:
```json
{
"username": "your_username",
"password": "your_password"
}
```
This will return a token. Include this token in the header of subsequent requests: `Authorization: Token <your_token>`

**Password Reset**:
- Endpoint: `/auth/users/reset_password/`
- Method: `POST`
- Payload:
```json
{
"email": "your_email@example.com"
}
```

### 2. CRUD for Applications:

**Create an App**:
- Endpoint: `/dashboard/createApp`
- Method: `POST`
- Payload:
```json
{
"name": "App Name",
"description": "App Description"
}
```

### 3. Manage Subscriptions:

**Update Subscription for an App**:
- Endpoint: `/dashboard/updateSub/`
- Method: `PATCH`
- Payload:
```json
{
"user_id": <user_id>,
"sub_id": <sub_id>,
"plan_id": <plan_id>,
}
```

**Cancel Subscription for an App**:
- Endpoint: `/dashboard/cancelSub`
- Method: `POST`
```json
{
"user_id": <user_id>,
"sub_id": <sub_id>,
}
```