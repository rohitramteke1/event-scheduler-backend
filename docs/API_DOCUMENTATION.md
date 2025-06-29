# Event Scheduler API Documentation

## Overview

The Event Scheduler API is a RESTful service built with Flask that provides comprehensive event management capabilities including CRUD operations, search functionality, and automated email reminders.

## Base URL

```
http://localhost:5000/api/events
```

## Authentication

Currently, the API does not require authentication. All endpoints are publicly accessible.

## Data Models

### Event Object

```json
{
  "id": "uuid-string",
  "title": "string",
  "description": "string", 
  "start_time": "ISO-8601 datetime",
  "end_time": "ISO-8601 datetime",
  "recurrence": "daily|weekly|monthly|null",
  "email": "email@example.com"
}
```

## API Endpoints

### 1. Get All Events

Retrieves all events sorted by start time.

**Endpoint:** `GET /api/events/`

**Response:**
- **200 OK**: List of events
- **500 Internal Server Error**: Server error

**Example Request:**
```bash
curl -X GET http://localhost:5000/api/events/
```

**Example Response:**
```json
[
  {
    "id": "af11d760-91e2-4a1d-8fae-4b6781cb58e5",
    "title": "Team Meeting",
    "description": "Weekly team sync",
    "start_time": "2024-01-15T10:00:00",
    "end_time": "2024-01-15T11:00:00",
    "recurrence": "weekly",
    "email": "team@company.com"
  }
]
```

### 2. Get Event by ID

Retrieves a specific event by its UUID.

**Endpoint:** `GET /api/events/{event_id}`

**Parameters:**
- `event_id` (path, required): Event UUID

**Response:**
- **200 OK**: Event details
- **404 Not Found**: Event not found
- **500 Internal Server Error**: Server error

**Example Request:**
```bash
curl -X GET http://localhost:5000/api/events/af11d760-91e2-4a1d-8fae-4b6781cb58e5
```

**Example Response:**
```json
{
  "id": "af11d760-91e2-4a1d-8fae-4b6781cb58e5",
  "title": "Team Meeting",
  "description": "Weekly team sync",
  "start_time": "2024-01-15T10:00:00",
  "end_time": "2024-01-15T11:00:00",
  "recurrence": "weekly",
  "email": "team@company.com"
}
```

### 3. Create Event

Creates a new event.

**Endpoint:** `POST /api/events/`

**Request Body:**
```json
{
  "title": "string (required)",
  "description": "string (required)",
  "start_time": "ISO-8601 datetime (required)",
  "end_time": "ISO-8601 datetime (required)",
  "recurrence": "daily|weekly|monthly|null (optional)",
  "email": "email@example.com (optional)"
}
```

**Response:**
- **201 Created**: Event created successfully
- **400 Bad Request**: Missing required fields
- **500 Internal Server Error**: Server error

**Example Request:**
```bash
curl -X POST http://localhost:5000/api/events/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Project Review",
    "description": "Monthly project status review",
    "start_time": "2024-01-20T14:00:00",
    "end_time": "2024-01-20T15:00:00",
    "recurrence": "monthly",
    "email": "manager@company.com"
  }'
```

**Example Response:**
```json
{
  "id": "new-uuid-here",
  "title": "Project Review",
  "description": "Monthly project status review",
  "start_time": "2024-01-20T14:00:00",
  "end_time": "2024-01-20T15:00:00",
  "recurrence": "monthly",
  "email": "manager@company.com"
}
```

### 4. Update Event (Full Update)

Updates an existing event with complete replacement.

**Endpoint:** `PUT /api/events/{event_id}`

**Request Body:** Same as POST (all fields required)

**Response:**
- **200 OK**: Event updated successfully
- **404 Not Found**: Event not found
- **500 Internal Server Error**: Server error

**Example Request:**
```bash
curl -X PUT http://localhost:5000/api/events/af11d760-91e2-4a1d-8fae-4b6781cb58e5 \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Updated Team Meeting",
    "description": "Updated weekly team sync",
    "start_time": "2024-01-15T10:00:00",
    "end_time": "2024-01-15T11:00:00",
    "recurrence": "weekly",
    "email": "team@company.com"
  }'
```

### 5. Update Event (Partial Update)

Updates specific fields of an existing event.

**Endpoint:** `PATCH /api/events/{event_id}`

**Request Body:** Any subset of event fields

**Response:**
- **200 OK**: Event updated successfully
- **404 Not Found**: Event not found
- **500 Internal Server Error**: Server error

**Example Request:**
```bash
curl -X PATCH http://localhost:5000/api/events/af11d760-91e2-4a1d-8fae-4b6781cb58e5 \
  -H "Content-Type: application/json" \
  -d '{
    "title": "New Meeting Title",
    "description": "Updated description"
  }'
```

### 6. Delete Event

Deletes an existing event.

**Endpoint:** `DELETE /api/events/{event_id}`

**Response:**
- **200 OK**: Event deleted successfully
- **404 Not Found**: Event not found
- **500 Internal Server Error**: Server error

**Example Request:**
```bash
curl -X DELETE http://localhost:5000/api/events/af11d760-91e2-4a1d-8fae-4b6781cb58e5
```

**Example Response:**
```json
{
  "message": "Event deleted"
}
```

### 7. Search Events

Searches events by title or description.

**Endpoint:** `GET /api/events/search?q={search_query}`

**Query Parameters:**
- `q` (required): Search query string

**Response:**
- **200 OK**: Matching events
- **400 Bad Request**: Missing search query
- **500 Internal Server Error**: Server error

**Example Request:**
```bash
curl -X GET "http://localhost:5000/api/events/search?q=meeting"
```

**Example Response:**
```json
[
  {
    "id": "af11d760-91e2-4a1d-8fae-4b6781cb58e5",
    "title": "Team Meeting",
    "description": "Weekly team sync",
    "start_time": "2024-01-15T10:00:00",
    "end_time": "2024-01-15T11:00:00",
    "recurrence": "weekly",
    "email": "team@company.com"
  }
]
```

## Error Responses

All error responses follow this format:

```json
{
  "error": "Error message description"
}
```

### Common HTTP Status Codes

- **200 OK**: Request successful
- **201 Created**: Resource created successfully
- **400 Bad Request**: Invalid request data
- **404 Not Found**: Resource not found
- **500 Internal Server Error**: Server error

## Data Validation

### Required Fields for Event Creation
- `title`: Non-empty string
- `description`: Non-empty string
- `start_time`: Valid ISO-8601 datetime string
- `end_time`: Valid ISO-8601 datetime string

### Optional Fields
- `recurrence`: One of "daily", "weekly", "monthly", or null
- `email`: Valid email address format

### DateTime Format
All datetime fields must be in ISO-8601 format: `YYYY-MM-DDTHH:MM:SS`

## Rate Limiting

Currently, no rate limiting is implemented. Use responsibly.

## CORS

CORS is not configured by default. For production use, consider adding CORS headers.

## Swagger Documentation

Interactive API documentation is available at:
```
http://localhost:5000/apidocs
```

## Testing the API

### Using curl

```bash
# Get all events
curl http://localhost:5000/api/events/

# Create an event
curl -X POST http://localhost:5000/api/events/ \
  -H "Content-Type: application/json" \
  -d '{"title":"Test","description":"Test event","start_time":"2024-01-15T10:00:00","end_time":"2024-01-15T11:00:00"}'

# Search events
curl "http://localhost:5000/api/events/search?q=test"
```

### Using Python requests

```python
import requests

# Get all events
response = requests.get('http://localhost:5000/api/events/')
events = response.json()

# Create an event
event_data = {
    "title": "Python Test Event",
    "description": "Testing with Python",
    "start_time": "2024-01-15T10:00:00",
    "end_time": "2024-01-15T11:00:00",
    "email": "test@example.com"
}
response = requests.post('http://localhost:5000/api/events/', json=event_data)
```

## Email Reminder System

The API includes a background reminder system that:

1. **Checks every minute** for upcoming events
2. **Sends email reminders** 1 hour before event start time
3. **Handles recurring events** automatically
4. **Prevents duplicate reminders** using a tracking system

### Email Configuration

Configure email settings in your `.env` file:

```env
EMAIL_HOST=smtp-relay.brevo.com
EMAIL_PORT=587
EMAIL_USER=your_smtp_username
EMAIL_PASS=your_smtp_password
EMAIL_FROM=your_email@example.com
```

### Recurring Events

Supported recurrence patterns:
- `daily`: Event repeats every day
- `weekly`: Event repeats every week
- `monthly`: Event repeats every month (approximately 30 days)
- `null`: One-time event (default)

## Support

For API support and questions:
- Email: rramteke8201@gmail.com
- Create an issue in the repository 