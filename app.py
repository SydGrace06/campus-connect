from __future__ import annotations

from datetime import date, time
from flask import Flask, request, session
from flask import redirect, url_for, render_template, flash
from routes.events import register_event_routes

from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import Enum as SQLEnum, Select, Integer, String, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column
from wtforms.fields import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import InputRequired, NumberRange, Length

from collections.abc import Sequence
from pathlib import Path
from enum import Enum

from flask_login import login_required
from extensions import login_manager, db

from models import Club, Event, CampusLocation, OrgType, EventCategory
from seed_locations import CAMPUS_LOCATIONS
from seed_clubs import CAMPUS_CLUBS
# update for our forms:
# from forms import AuthorForm, BookForm
# from models import db, Author, Book

# identify the full path to the database file
scriptdir: Path = Path(__file__).resolve().parent
dbfile: Path = scriptdir / 'orgs.db'

# configure this web application
app = Flask(__name__)
app.config['SECRET_KEY'] = "aardvarkelephantcapybaraantelope"
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{dbfile}"

db.init_app(app)

with app.app_context():
        db.drop_all()
        db.create_all()

        club_instances: list[Club] = []

        for club in CAMPUS_CLUBS:
            new_club: Club = Club(
                club_name=club["club_name"],
                abrev=club.get("abrev"),
                org_type=club["org_type"],
                advisor_name=club["advisor_name"],
                president_name=club["president_name"],
                description=club.get("description")
            )

        location_instances: list[CampusLocation] = []

        for location in CAMPUS_LOCATIONS:
            new_location: CampusLocation = CampusLocation(
                name=location["name"],
                latitude=location["latitude"],
                longitude=location["longitude"]
            )
            location_instances.append(new_location)

        event_instances: tuple[Event, ...] = (
            Event(title="Hackathon", category=EventCategory.COMPETITION, date=date(2026, 11, 11), time=time(19, 0), locationId=29, club_id=29),
            Event(title="Pineapple on Pizza Debate", category=EventCategory.ACADEMIC_PROFESSIONAL, date=date(2026, 11, 3), time=time(18, 26), locationId=10, club_id=27),
            Event(title="Field Hockey Game", category=EventCategory.COMPETITION, date=date(2026, 11, 7), time=time(8, 30), locationId=30, club_id=99),
            Event(title="Monster Mash Dance", category=EventCategory.SOCIAL, date=date(2026, 10, 30), time=time(20, 0), locationId=1, club_id=36),
            Event(title="Hymn Sing Christmas Recital", category=EventCategory.MINISTRY, date=date(2026, 12, 11), time=time(21, 0), locationId=2, club_id=77)
        )

        db.session.add_all(club_instances)
        db.session.add_all(location_instances)
        db.session.add_all(event_instances)
    
        db.session.commit()

# Application configuration
scriptdir = Path(__file__).resolve().parent
dbfile = scriptdir / "users.db"

app.config['SECRET_KEY'] = 'batteryhorsestapler'
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{dbfile}"

login_manager.init_app(app)
login_manager.login_view = 'auth.get_login'
login_manager.session_protection = 'strong'

# Register authentication routes
from routes.auth import auth
app.register_blueprint(auth)

# Register event routes
from routes.events import register_event_routes
register_event_routes(app)

@app.route("/")
@login_required
def home():
    query: Select[tuple[Event]] = db.select(Event)
    events: Sequence[Event] = db.session.scalars(query).all()
    return render_template("index.html", events=events)

#@app.route('/api/events')

#@app.get('/events/')
#def get_events():
#     query: Select[tuple[Event]] = db.select(Event)
#     events: Sequence[Event] = db.session.scalars(query).all()
#     return render_template('events.html', events=events)


if __name__ == "__main__":
    app.run(debug=True)
