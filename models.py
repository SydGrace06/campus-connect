from __future__ import annotations

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer, ForeignKey, CHAR
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()