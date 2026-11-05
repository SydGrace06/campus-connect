# contains routes for viewing and searching events
from flask import jsonify
from models import db, Event, CampusLocation

def register_event_routes(app):

    @app.get("/api/events")
    def get_api_events():
        results = db.session.execute(
            db.select(Event, CampusLocation)
            .join(CampusLocation, Event.locationId == CampusLocation.id)
        ).all()

        events = []

        for event, location in results:
            events.append({
                "title": event.title,
                "category": event.category.value,
                "date": event.date.isoformat(),
                "time": event.time.strftime("%H:%M"),
                "location": {
                    "name": location.name,
                    "latitude": location.latitude,
                    "longitude": location.longitude
                }
            })

        return jsonify(events)


#def register_event_routes(app):

#    @app.route("/events")
#    def list_events():
#        return "Here are the campus events!"
