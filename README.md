# Event Scheduler Backend API

## 🚀 Live Demo

**Full Stack Application**: [http://13.127.11.95:8501/](http://13.127.11.95:8501/)

A robust Flask-based REST API for managing events with email reminders, recurring events, and real-time notifications.

## 🌟 Features

- **Event Management**: Create, read, update, and delete events
- **Email Reminders**: Automated email notifications using Brevo SMTP
- **Recurring Events**: Support for daily, weekly, and monthly recurring events
- **Search Functionality**: Search events by title or description
- **Real-time Reminders**: Background thread checking for upcoming events
- **Swagger Documentation**: Interactive API documentation
- **Comprehensive Testing**: 24 test cases with 100% pass rate

## 📚 Documentation

For detailed documentation, please refer to the following guides:

- **[Setup Guide](docs/SETUP_GUIDE.md)** - Complete installation and configuration instructions
- **[API Documentation](docs/API_DOCUMENTATION.md)** - Detailed API reference and examples
- **[Requirements Checklist](docs/REQUIREMENTS_CHECKLIST.md)** - Project requirements and features checklist

## 📋 Prerequisites

- Python 3.8+
- pip (Python package installer)
- SMTP email service (Brevo recommended)

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd event-scheduler-backend
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration
Create a `.env` file in the root directory:
```env
EMAIL_HOST=smtp-relay.brevo.com
EMAIL_PORT=587
EMAIL_USER=your_smtp_username
EMAIL_PASS=your_smtp_password
EMAIL_FROM=your_email@example.com
EMAIL_TO=recipient@example.com
```

### 5. Run the Application
```bash
python run.py
```

The server will start at `http://localhost:5000`

## 🧪 Testing

Run the test suite:
```bash
python -m pytest tests/ -v
```

All 24 tests should pass successfully.

## 📚 API Reference

### Base URL
```
http://localhost:5000/api/events
```

### Endpoints

#### 1. Get All Events
```http
GET /api/events/
```

**Response:**
```json
[
  {
    "id": "uuid",
    "title": "Event Title",
    "description": "Event Description",
    "start_time": "2024-01-15T10:00:00",
    "end_time": "2024-01-15T11:00:00",
    "recurrence": "daily|weekly|monthly|null",
    "email": "user@example.com"
  }
]
```

#### 2. Get Event by ID
```http
GET /api/events/{event_id}
```

**Response:**
```json
{
  "id": "uuid",
  "title": "Event Title",
  "description": "Event Description",
  "start_time": "2024-01-15T10:00:00",
  "end_time": "2024-01-15T11:00:00",
  "recurrence": "daily|weekly|monthly|null",
  "email": "user@example.com"
}
```

#### 3. Create Event
```http
POST /api/events/
```

**Request Body:**
```json
{
  "title": "Event Title",
  "description": "Event Description",
  "start_time": "2024-01-15T10:00:00",
  "end_time": "2024-01-15T11:00:00",
  "recurrence": "daily",
  "email": "user@example.com"
}
```

**Response:** `201 Created`

#### 4. Update Event
```http
PUT /api/events/{event_id}
```

**Request Body:** Same as POST
**Response:** `200 OK`

#### 5. Partial Update Event
```http
PATCH /api/events/{event_id}
```

**Request Body:** Any subset of event fields
**Response:** `200 OK`

#### 6. Delete Event
```http
DELETE /api/events/{event_id}
```

**Response:** `200 OK`

#### 7. Search Events
```http
GET /api/events/search?q={search_query}
```

**Response:** Array of matching events

## 📋 Postman Collection

A comprehensive Postman collection is included for testing all API endpoints:

**File:** `Event_Scheduler_API.postman_collection.json`

### Import Instructions:
1. Open Postman
2. Click "Import" button
3. Select the `Event_Scheduler_API.postman_collection.json` file
4. The collection will be imported with all endpoints ready to test

### Collection Features:
- **12 API endpoints** covering all CRUD operations
- **Environment variables** for easy configuration
- **Pre-request scripts** for automatic setup
- **Test scripts** for response validation
- **Error handling examples** for edge cases
- **Recurring event examples** (daily, weekly, monthly)

### Quick Start with Postman:
1. Import the collection
2. Set environment variable `base_url` to `http://localhost:5000`
3. Start the Flask server: `python run.py`
4. Run the requests in sequence to test the API

## 🔧 Project Structure

```
event-scheduler-backend/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── config.py            # Configuration settings
│   ├── models/
│   │   └── event_model.py   # Event data model
│   ├── routes/
│   │   └── event_routes.py  # API endpoints
│   ├── services/
│   │   └── event_service.py # Business logic
│   ├── tasks/
│   │   └── reminder_task.py # Background reminder system
│   └── utils/
│       ├── email_utils.py   # Email functionality
│       ├── file_io.py       # File operations
│       └── reminder.py      # Reminder utilities
├── tests/
│   └── test_app.py          # Test suite
├── events.json              # Event data storage
├── requirements.txt         # Python dependencies
├── run.py                   # Application entry point
└── .env                     # Environment variables
```

## 🔔 Reminder System

The application includes a background thread that:
- Checks for upcoming events every minute
- Sends email reminders 1 hour before event start time
- Handles recurring events (daily, weekly, monthly)
- Prevents duplicate reminders

## 📧 Email Integration

The system uses Brevo SMTP for sending email reminders:
- Configured via environment variables
- Supports UTF-8 encoding
- Includes event details in reminder emails
- Error handling for failed email sends

## 🛡️ Error Handling

- Input validation for required fields
- Proper HTTP status codes
- JSON error responses
- Exception handling for file operations

## 📖 Swagger Documentation

Access interactive API documentation at:
```
http://localhost:5000/apidocs
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Rohit Ramteke**
- Email: ramteker284@gmail.com
- GitHub: [@rohitramteke1](https://github.com/rohitramteke1)

## 🆘 Support

For support and questions:
- Create an issue in the repository
- Contact: ramteker284@gmail.com

---

**Made with ❤️ using Flask and Python**
