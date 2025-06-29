# Quick Setup Guide

## 👉 Live Demo

**Full Stack Application**: [http://13.127.11.95:8501/](http://13.127.11.95:8501/)

## 🚀 Quick Start

### 1. Activate Virtual Environment
```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment
Create `.env` file with your email settings:
```env
EMAIL_HOST=smtp-relay.brevo.com
EMAIL_PORT=587
EMAIL_USER=your_smtp_username
EMAIL_PASS=your_smtp_password
EMAIL_FROM=your_email@example.com
EMAIL_TO=recipient@example.com
```

### 4. Run the Application
```bash
python run.py
```

### 5. Test the API
```bash
# Get all events
curl http://localhost:5000/api/events/

# Create an event
curl -X POST http://localhost:5000/api/events/ \
  -H "Content-Type: application/json" \
  -d '{"title":"Test Event","description":"Test Description","start_time":"2024-12-25T10:00:00","end_time":"2024-12-25T11:00:00"}'

# Search events
curl "http://localhost:5000/api/events/search?q=test"
```

### 6. Run Tests
```bash
python -m pytest tests/ -v
```

## 📍 Important URLs

- **API Base URL**: http://localhost:5000/api/events
- **Swagger Documentation**: http://localhost:5000/apidocs/
- **Live Demo**: http://13.127.11.95:8501/

## ✅ Verification Checklist

- [ ] Virtual environment activated
- [ ] All dependencies installed
- [ ] Environment variables configured
- [ ] Server starts without errors
- [ ] API endpoints respond correctly
- [ ] All tests pass (24/24)
- [ ] Swagger documentation accessible
- [ ] Email reminders working (if configured)

## 🐛 Troubleshooting

### Common Issues

1. **Module not found errors**
   - Ensure virtual environment is activated
   - Run `pip install -r requirements.txt`

2. **Port already in use**
   - Change port in `run.py` or kill existing process

3. **Email not sending**
   - Check `.env` configuration
   - Verify SMTP credentials

4. **Tests failing**
   - Ensure you're in the project root directory
   - Run with `python -m pytest tests/ -v`

## 📞 Support

For issues and questions:
- Email: ramteker284@gmail.com
- Create an issue in the repository 