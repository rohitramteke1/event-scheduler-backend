from app.models.event_model import Event
from app.utils.file_io import load_events, save_events
from datetime import datetime

# Get all events sorted by start_time
def get_all_events():
    events = load_events()
    events.sort(key=lambda e: e.start_time)
    return [event.to_dict() for event in events]

# Get a single event by ID
def get_event_by_id(event_id):
    events = load_events()
    for event in events:
        if event.id == event_id:
            return event.to_dict()
    raise ValueError("Event not found")

# Create a new event
def create_event(data):
    required_fields = ["title", "description", "start_time", "end_time"]
    for field in required_fields:
        if field not in data:
            raise ValueError(f"{field} is required")

    # optional
    recurrence = data.get("recurrence") 
    email = data.get("email") 

    new_event = Event(
        title=data["title"],
        description=data["description"],
        start_time=data["start_time"],
        end_time=data["end_time"],
        recurrence=recurrence,
        email=email
    )

    events = load_events()
    events.append(new_event)
    save_events(events)
    return new_event.to_dict()


# Update an existing event
def update_event(event_id, data, partial=False):
    events = load_events()
    updated = False

    for i, event in enumerate(events):
        if event.id == event_id:
            if partial:
                # patch
                if "title" in data:
                    event.title = data["title"]
                if "description" in data:
                    event.description = data["description"]
                if "start_time" in data:
                    event.start_time = data["start_time"]
                if "end_time" in data:
                    event.end_time = data["end_time"]
                if "recurrence" in data:
                    event.recurrence = data["recurrence"]
                if "email" in data:
                    event.email = data["email"]
            else:
                # put
                event.title = data.get("title", event.title)
                event.description = data.get("description", event.description)
                event.start_time = data.get("start_time", event.start_time)
                event.end_time = data.get("end_time", event.end_time)
                event.recurrence = data.get("recurrence", event.recurrence)
                event.email = data.get("email", event.email)

            events[i] = event
            updated = True
            break

    if updated:
        save_events(events)
        return event.to_dict()
    else:
        raise ValueError("Event not found")


# Delete an event
def delete_event(event_id):
    events = load_events()
    new_events = [e for e in events if e.id != event_id]

    if len(events) == len(new_events):
        raise ValueError("Event not found")

    save_events(new_events)
    return True

def search_event(query):
    events = load_events()
    query = query.lower()
    matching_events = [
        event.to_dict()
        for event in events
        if query in event.title.lower() or query in event.description.lower()
    ]
    return matching_events