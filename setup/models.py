from sqlalchemy import (
    Column, Integer, String, Float,
    ForeignKey, Enum, UniqueConstraint,
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

    player_id   = Column(Integer, primary_key=True)
    name        = Column(String(100))
    nicknames   = Column(JSONB)
    country     = Column(String(100), default="USA")
    school      = Column(String(100))
    birthdate   = Column(String(20))
    height      = Column(String(10))
    weight      = Column(String(10))
    draft_year  = Column(String(10))
    draft_round = Column(String(10))
    draft_pick  = Column(String(10))

    seasons = relationship("SeasonStats", back_populates="player")
    awards  = relationship("Award", back_populates="player")

class SeasonStats(Base):
    __tablename__ = "season_stats"
    __table_args__ = (
        UniqueConstraint("player_id", "season_id", "team_id", "season_type"),
    )

    id              = Column(Integer, primary_key=True, autoincrement=True)
    player_id       = Column(Integer, ForeignKey("players.player_id"), nullable=False)
    season_id       = Column(String(10), nullable=False)
    season          = Column(String(10))
    team_id         = Column(Integer, nullable=False)
    league_id       = Column(String(10))
    team_abbr       = Column(String(10))
    season_type     = Column(Enum(SeasonType), nullable=False, default=SeasonType.regular)
    player_age      = Column(Float)
    gp              = Column(Integer)
    gs              = Column(Integer)
    minutes         = Column(Float)
    fgm             = Column(Float)
    fga             = Column(Float)
    fg_pct          = Column(Float)
    fg3m            = Column(Float)
    fg3a            = Column(Float)
    fg3_pct         = Column(Float)
    ftm             = Column(Float)
    fta             = Column(Float)
    ft_pct          = Column(Float)
    oreb            = Column(Float)
    dreb            = Column(Float)
    reb             = Column(Float)
    ast             = Column(Float)
    stl             = Column(Float)
    blk             = Column(Float)
    tov             = Column(Float)
    pf              = Column(Float)
    pts             = Column(Float)

    player = relationship("Player", back_populates="seasons")

class Award(Base):
    __tablename__ = "awards"

    id         = Column(Integer, primary_key=True, autoincrement=True)
    player_id  = Column(Integer, ForeignKey("players.player_id"), nullable=False)
    season     = Column(String(10))
    award_name = Column(String(100))

    player = relationship("Player", back_populates="awards")