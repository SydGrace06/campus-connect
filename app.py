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

from models import db, Club, Event, CampusLocation, OrgType, EventCategory
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

with app.app_context():
        db.drop_all()
        db.create_all()

        club_instances: tuple[Club,...] = (
            Club(club_name="Women for Computer Science", abrev="WFCS", org_type=OrgType.ACADEMIC_PROFESSIONAL_ORGS, advisor_name="Dr. Jonathan Hutchins", president_name="Wynonna Roberts"),
            Club(club_name="Swing Dance Club", org_type=OrgType.ARTS_ORGS, advisor_name="Dr. Erik Bardy", president_name="Sarah Smith"),
            Club(club_name="Hymn Sing Club", org_type=OrgType.MINISTRY_ORGS, advisor_name="Dr. Paul Munson", president_name="June Lee"),
            Club(club_name="Women's Field Hockey", org_type=OrgType.CLUB_SPORT_ORGS, advisor_name="Mrs. Tori Wright", president_name="Bayleigh Miller"),
            Club(club_name="Speech and Debate Team", org_type=OrgType.ACADEMIC_PROFESSIONAL_ORGS, advisor_name="Dr. Jason Edwards", president_name="Ginger Schiffmayer")
        )

        location_instances: tuple[CampusLocation, ...] = (
            CampusLocation(name="STEM", latitude=41.15555889321571, longitude=-80.07897482206347),
            CampusLocation(name="PEW", latitude=41.15274167584597, longitude=-80.07720453780321),
            CampusLocation(name="Football Field", latitude=41.15705213768561, longitude=-80.08466176556155),
            CampusLocation(name="HAL Courtyard", latitude=41.15489320642377, longitude=-80.0777023538951),
            CampusLocation(name="Harbison Chapel", latitude=41.156951476703156, longitude=-80.08060175968447)
        )


        event_instances: tuple[Event, ...] = (
            Event(title="Hackathon", category=EventCategory.COMPETITION, date=date(2026, 11, 11), time=time(19, 0), locationid=1, club_id=1),
            Event(title="Pineapple on Pizza Debate", category=EventCategory.ACADEMIC_PROFESSIONAL, date=date(2026, 11, 3), time=time(18, 26), locationid=2, club_id=5),
            Event(title="Field Hockey Game", category=EventCategory.COMPETITON, date=date(2026, 11, 7), time=time(8, 30), locationid=3, club_id=4),
            Event(title="Monster Mash Dance", category=EventCategory.SOCIAL, date=date(2026, 10, 30), time=time(20, 0), locationid=4, club_id=2),
            Event(title="Hymn Sing Christmas Recital", category=EventCategory.MINISTRY, date=date(2026, 12, 11), time=time(21, 0), locationid=5, club_id=3)
        )

        db.session.add_all(club_instances)
        db.session.add_all(location_instances)
        db.session.add_all(event_instances)
    
        db.session.commit()

register_event_routes(app)

@app.route("/")
def home():
    return render_template("index.html")

#@app.route('/api/events')

@app.get('/events/')
def get_events():
     query: Select[tuple[Event]] = db.select(Event)
     events: Sequence[Event] = db.session.scalars(query).all()
     return render_template('events.html', events=events)


if __name__ == "__main__":
    app.run(debug=True)
