from __future__ import annotations

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer, ForeignKey, CHAR, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class CampusLocation(db.Model):
    __tablename__ = "campus_locations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    latitude: Mapped[float] = mapped_column(Float, nullable=False)
    longitude: Mapped[float] = mapped_column(Float, nullable=False)