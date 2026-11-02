# contains routes for viewing and searching events

def register_event_routes(app):

    @app.route("/events")
    def list_events():
        return "Here are the campus events!"