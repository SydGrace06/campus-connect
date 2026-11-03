from __future__ import annotations

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum as SQLEnum
from sqlalchemy import String, Integer, ForeignKey, CHAR, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class OrgType(SQLEnum):
    ACADEMIC_PROFESSIONAL_ORGS  = 'Academic/Professional'
    ARTS_ORGS      = 'Arts'
    POLY_ORGS       = 'Political'
    PUBLICATION_ORGS       = 'Publications'
    SERVICE_ORGS = 'Service'
    SPECIAL_INTEREST_ORGS = 'Special Interest'
    RECREATION_ORGS = 'Recreation'
    GREEK_LIFE_HOUSING_ORGS = 'Greek Life/Housing Groups'
    MINISTRY_ORGS = 'Ministry'
    HONORARIES_ORGS = 'Honoraries'
    MUSICAL_ORGS = 'Music'
    IM_SPORT_ORGS = 'IM Sports'
    CLUB_SPORT_ORGS = 'Club Sports'



class CampusLocation(db.Model):
    __tablename__ = "campus_locations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    latitude: Mapped[float] = mapped_column(Float, nullable=False)
    longitude: Mapped[float] = mapped_column(Float, nullable=False)

class Event(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(128))
    category: Mapped[str] = mapped_column(String(32))
    date: Mapped[datetime] = mapped_column(datetime)
    time: Mapped[datetime] = mapped_column(datetime)
    locationId: Mapped[int] = mapped_column(Integer, db.ForeignKey('campus_locations.id'))

class Club(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    club_name: Mapped[str] = mapped_column(String(128))
    abrev: Mapped[str] = mapped_column(String(15))
    org_type: Mapped[OrgType] = mapped_column(SQLEnum(OrgType))
    advisor_name: Mapped[str] = mapped_column(String(32))
    president_name: Mapped[str] = mapped_column(String(32))


class Account(db.Model):
    username: Mapped[str] = mapped_column(String(32))
    pass

class Favorite(db.Model):
    pass

class Registration(db.Model):
    pass

# when you add the event model, it will likely need a foreign key to campus_locations.id, so each event can reference a building instead of storing its own coordinates