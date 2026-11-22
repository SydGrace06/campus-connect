# contains routes for viewing and searching events
from flask import jsonify
from models import db, Event, CampusLocation, Club

def register_event_routes(app):

    @app.get("/api/events")
    def get_api_events():
        results = db.session.execute(
            db.select(Event, CampusLocation, Club)
            .join(CampusLocation, Event.locationId == CampusLocation.id)
            .outerjoin(Club, Event.club_id == Club.id)
        ).all()

        events = []

        for event, location, club in results:
            events.append({
                "id": event.id,
                "title": event.title,
                "category": event.category.value,
                "date": event.date.isoformat(),
                "time": event.time.strftime("%H:%M"),
                "location": {
                    "name": location.name,
                    "latitude": location.latitude,
                    "longitude": location.longitude
                },
                "club": club.club_name if club else None
            })

        return jsonify(events)

    @app.get("/api/events/<int:event_id>")
    def get_api_event(event_id: int):
        event = db.get_or_404(Event, event_id)
        location = db.get_or_404(CampusLocation, event.locationId)
        club = db.session.get(Club, event.club_id) if event.club_id else None

        return jsonify({
            "id": event.id,
            "title": event.title,
            "category": event.category.value,
            "date": event.date.isoformat(),
            "time": event.time.strftime("%H:%M"),
            "location": {
                "name": location.name,
                "latitude": location.latitude,
                "longitude": location.longitude
            },
            "club": club.club_name if club else None
        })
