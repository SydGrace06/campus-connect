from __future__ import annotations

#from pathlib import Path
from flask_sqlalchemy import SQLAlchemy
from enum import Enum
from sqlalchemy import Enum as SQLEnum
from sqlalchemy import String, Integer, ForeignKey, CHAR, Float, Date, Time, VARBINARY
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates
from extensions import db
from flask_login import UserMixin

class OrgType(Enum):
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

class EventCategory(Enum):
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
    category: Mapped[EventCategory] = mapped_column(SQLEnum(EventCategory))
    date: Mapped[Date] = mapped_column(Date)
    time: Mapped[Time] = mapped_column(Time)
    locationId: Mapped[int] = mapped_column(Integer, db.ForeignKey('campus_locations.id'))
    location: Mapped['CampusLocation'] = relationship("CampusLocation", back_populates="events")
    club_id: Mapped[int] = mapped_column(Integer, db.ForeignKey('clubs.id'), nullable=True)
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

class Account(UserMixin, db.Model):
    __tablename__ = "accounts"

    username: Mapped[str] = mapped_column(String(32), primary_key=True)
    handle: Mapped[str] = mapped_column(String(15), nullable=True)
    email: Mapped[str] = mapped_column(String(128))
    pwd_hasher: Mapped[bytes] = mapped_column(VARBINARY(255), nullable=False)
    favorites: Mapped[list['Favorite']] = relationship("Favorite", back_populates="account")
    registrations: Mapped[list['Registration']] = relationship("Registration", back_populates="registered_accounts")


    def get_id(self):
        return self.username

        # make sure that emails are all lowercase
    @validates('email')
    def validate_email(self, key: str, email: str) -> str:
        if email:
            return email.strip().lower()
        return email
    

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


# when you add the event model, it will likely need a foreign key to campus_locations.id, so each event can reference a building instead of storing its own coordinates