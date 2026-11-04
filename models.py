from __future__ import annotations

from pathlib import Path
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum as SQLEnum
from sqlalchemy import String, Integer, ForeignKey, CHAR, Float, Date, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship

# identify the full path to the database file
#scriptdir: Path = Path(__file__).resolve().parent
#dbfile: Path = scriptdir / 'orgs.db'

# configure this web application
#app = Flask(__name__)
#app.config['SECRET_KEY'] = "correcthorsebatterystaple"
#app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{dbfile}"


db = SQLAlchemy()

class OrgType(SQLEnum):
    ACADEMIC_PROFESSIONAL_ORGS  = 'Academic/Professional'
    ARTS_ORGS                   = 'Arts'
    POLY_ORGS                   = 'Political'
    PUBLICATION_ORGS            = 'Publications'
    SERVICE_ORGS                = 'Service'
    SPECIAL_INTEREST_ORGS       = 'Special Interest'
    RECREATION_ORGS             = 'Recreation'
    GREEK_LIFE_HOUSING_ORGS     = 'Greek Life/Housing Groups'
    MINISTRY_ORGS               = 'Ministry'
    HONORARIES_ORGS             = 'Honoraries'
    MUSICAL_ORGS                = 'Music'
    IM_SPORT_ORGS               = 'IM Sports'
    CLUB_SPORT_ORGS             = 'Club Sports'

class EventCategory(SQLEnum):
    ACADEMIC_PROFESSIONAL  = 'Academic/Professional'
    REGULAR                = 'Regular'
    SOCIAL                 = 'Social'
    SERVICE                = 'Service'
    FUNDRAISING            = 'Fundraising'
    COMPETITION            = 'Competition'
    ARTS                   = 'Arts'
    MINISTRY               = 'Ministry'
    OTHER                  = 'Other'



class CampusLocation(db.Model):
    __tablename__ = "campus_locations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    latitude: Mapped[float] = mapped_column(Float, nullable=False)
    longitude: Mapped[float] = mapped_column(Float, nullable=False)
    events: Mapped[list['Event']] = relationship("Event", back_populates="location")

class Event(db.Model):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(128))
    category: Mapped[str] = mapped_column(String(32))
    date: Mapped[Date] = mapped_column(Date)
    time: Mapped[Time] = mapped_column(Time)
    locationId: Mapped[int] = mapped_column(Integer, db.ForeignKey('campus_locations.id'))
    location: Mapped['CampusLocation'] = relationship("CampusLocation", back_populates="events")
    club_id: Mapped[int] = mapped_column(Integer, db.ForeignKey('clubs.id'))
    club: Mapped['Club'] = relationship("Club", back_populates="events")
    registrations: Mapped[list['Registration']] = relationship("Registration", back_populates="event")

class Club(db.Model):
    __tablename__ = "clubs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    club_name: Mapped[str] = mapped_column(String(128))
    abrev: Mapped[str] = mapped_column(String(15), nullable=True)
    org_type: Mapped[OrgType] = mapped_column(SQLEnum(OrgType))
    advisor_name: Mapped[str] = mapped_column(String(32))
    president_name: Mapped[str] = mapped_column(String(32))
    description: Mapped[str] = mapped_column(String(256), nullable=True)
    events: Mapped[list['Event']] = relationship("Event", back_populates="club")
    favorited: Mapped[list['Favorite']] = relationship("Favorite", back_populates="club")

class Account(db.Model):
    __tablename__ = "accounts"

    username: Mapped[str] = mapped_column(String(32), primary_key=True)
    handle: Mapped[str] = mapped_column(String(15), nullable=True)
    password: Mapped[str] = mapped_column(String(32))
    favorites: Mapped[list['Favorite']] = relationship("Favorite", back_populates="account")
    registrations: Mapped[list['Registration']] = relationship("Registration", back_populates="registered_accounts")

class Favorite(db.Model):
    __tablename__ = "favorites"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    account_username: Mapped[str] = mapped_column(String(32), ForeignKey('accounts.username'))
    club_id: Mapped[int] = mapped_column(Integer, ForeignKey('clubs.id'))

    account: Mapped['Account'] = relationship(back_populates='favorites')
    club: Mapped['Club'] = relationship(back_populates='favorited')

class Registration(db.Model):
    __tablename__ = "registrations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    event_id: Mapped[int] = mapped_column(Integer, ForeignKey('events.id'))
    event: Mapped['Event'] = relationship(back_populates='registrations')

    account_username: Mapped[str] = mapped_column(String(32), ForeignKey('accounts.username'))
    registered_accounts: Mapped['Account'] = relationship(back_populates='registrations')


club_instances: tuple[Club,...] = (
            Club(club_name="Women for Computer Science", abrev="WFCS", org_type=OrgType.ACADEMIC_PROFESSIONAL_ORGS, advisor_name="Dr. Jonathan Hutchins", president_name="Wynonna Roberts"),
            Club(club_name="Swing Dance Club", org_type=OrgType.ARTS_ORGS, advisor_name="Dr. Erik Bardy", president_name="Sarah Smith"),
            Club(club_name="Turning Point USA at Grove City College", org_type=OrgType.POLY_ORGS, advisor_name="Keith Graybill", president_name="Moira Donovan"),
            Club(club_name="The Collegian", org_type=OrgType.PUBLICATION_ORGS, advisor_name="Mr. Nick Hildebrand", president_name="Emily Fox"),
            Club(club_name="Association for Women Students", abrev="AWS", org_type=OrgType.SERVICE_ORGS, advisor_name="Hannah Kincer", president_name="Mary God"),
            Club(club_name="Chess Club", org_type=OrgType.SPECIAL_INTEREST_ORGS, advisor_name="Timothy Sweet", president_name="Quinn MacKenzie"),
            Club(club_name="Outing Club", org_type=OrgType.RECREATION_ORGS, advisor_name="Dr. Devin Stauff", president_name="Connor Stoltzfus"),
            Club(club_name="Hymn Sing", org_type=OrgType.MINISTRY_ORGS, advisor_name="Dr. Paul Munson", president_name="June Lee"),
            Club(club_name="Women's Field Hockey", org_type=OrgType.CLUB_SPORT_ORGS, advisor_name="Mrs. Tori Wright", president_name="Bayleigh Miller"),


            Club(club_name="Fencing", org_type=OrgType.CLUB_SPORT_ORGS, advisor_name="Ian Harris", president_name="Rebecca Froyd"),
            Club(club_name="GCC Martial Arts Club", org_type=OrgType.CLUB_SPORT_ORGS, advisor_name="Dr. Jeffrey Buxton", president_name="Wynonna Roberts"),
            Club(club_name="Grove City College Club Ultimate Frisbee", org_type=OrgType.CLUB_SPORT_ORGS, advisor_name="Mr. Isaac Cooke", president_name="James Laird"),
            Club(club_name="Ice Hockey", org_type=OrgType.CLUB_SPORT_ORGS, advisor_name="Luke Tingley", president_name="Josh Elverson"),
            Club(club_name="Men's Rugby", org_type=OrgType.CLUB_SPORT_ORGS, advisor_name="Dr. Charles Kriley", president_name="Trevor Olson"),                 

        )

db.session.add_all(club_instances)

event_instances: tuple[Event, ...] = (

    #Event(title="", category)

)



db.session.add_all(event_instances)


account_instances: tuple[Event, ...] = (

)

db.session.add_all(account_instances)

# when you add the event model, it will likely need a foreign key to campus_locations.id, so each event can reference a building instead of storing its own coordinates