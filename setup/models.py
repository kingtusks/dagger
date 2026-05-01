from sqlalchemy import (
    Column, Integer, String, Float,
    ForeignKey, Enum, UniqueConstraint, Date
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import declarative_base, relationship
import enum

Base = declarative_base()

class SeasonType(enum.Enum):
    regular = "regular"
    playoffs = "playoffs"

class Player(Base):
    __tablename__ = "players"

    player_id = Column(Integer, primary_key=True)
    name = Column(String(100))
    nicknames = Column(JSONB)
    country = Column(String(100), default="USA")
    school = Column(String(100))
    birthdate = Column(Date)
    height = Column(Integer)
    weight = Column(Integer)
    draft_year = Column(Integer)
    draft_round = Column(Integer)
    draft_pick = Column(Integer)

    seasons = relationship("SeasonStats", back_populates="player")
    awards = relationship("Award", back_populates="player")

class SeasonStats(Base):
    __tablename__ = "season_stats"
    __table_args__ = (
        UniqueConstraint("player_id", "season", "team_id", "season_type"),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    player_id = Column(Integer, ForeignKey("players.player_id"), nullable=False)
    season = Column(String(10))
    team_id = Column(Integer)
    team_abbr = Column(String(5))
    season_type = Column(Enum(SeasonType), nullable=False, default=SeasonType.regular)
    player_age = Column(Integer)
    gp = Column(Integer)
    gs = Column(Integer)
    minutes = Column(Integer)
    fgm = Column(Integer)
    fga = Column(Integer)
    fg_pct = Column(Float)
    fg3m = Column(Integer)
    fg3a = Column(Integer)
    fg3_pct = Column(Float)
    ftm = Column(Integer)
    fta = Column(Integer)
    ft_pct = Column(Float)
    oreb = Column(Integer)
    dreb = Column(Integer)
    reb = Column(Integer)
    ast = Column(Integer)
    stl = Column(Integer)
    blk = Column(Integer)
    tov = Column(Integer)
    pf = Column(Integer)
    pts = Column(Integer)

    player = relationship("Player", back_populates="seasons")

class Award(Base):
    __tablename__ = "awards"

    id = Column(Integer, primary_key=True, autoincrement=True)
    player_id = Column(Integer, ForeignKey("players.player_id"), nullable=False)
    season = Column(String(10))
    award_name = Column(String(100))

    player = relationship("Player", back_populates="awards")

class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, autoincrement=True)
    team_id = Column(Integer)
    team_abbr = Column(String(5))
    team_name = Column(String(100))
    players = Column(JSONB)