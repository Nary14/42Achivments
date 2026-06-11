from datetime import datetime, timezone
from enum import Enum
from sqlalchemy import String, Boolean, DateTime, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app import Base


class ClaimStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


class AchievementCategory(str, Enum):
    PROJECT = "project"
    SOCIAL = "social"
    SCOLARITY = "scolarity"
    PEDAGOGY = "pedagogy"


class ConditionType(str, Enum):
    API_CHECK = "api_check"
    MANUAL = "manual"
    PHOTO = "photo"


class User(Base):
    """User model - represents a 42 school student or staff member"""
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    ft_id: Mapped[int] = mapped_column(Integer, unique=True)
    login: Mapped[str] = mapped_column(String(50), unique=True)
    email: Mapped[str] = mapped_column(String(120))
    display_name: Mapped[str] = mapped_column(String(100))
    is_staff: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(timezone.utc)
    )
    claims: Mapped[list["Claim"]] = relationship(
        back_populates="user",
        foreign_keys="Claim.user_id",
        cascade="all, delete-orphan"
    )
    reviewed_claims: Mapped[list["Claim"]] = relationship(
        back_populates="reviewer",
        foreign_keys="Claim.reviewed_by",
        cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<User {self.login} (ft_id={self.ft_id})>"


class Achievement(Base):
    """Achievement model - represents a gamification badge/reward"""
    __tablename__ = "achievements"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    description: Mapped[str] = mapped_column(String(255))
    category: Mapped[AchievementCategory] = mapped_column(String(50))
    condition_type: Mapped[ConditionType] = mapped_column(String(50))
    condition_data: Mapped[str | None] = mapped_column(
        String(255), nullable=True, default=None
    )
    wallet_reward: Mapped[int] = mapped_column(Integer, default=0)
    claims: Mapped[list["Claim"]] = relationship(
        back_populates="achievement", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<Achievement {self.name} ({self.category.value})>"


class Claim(Base):
    """Claim model - represents a user's claim for an achievement"""
    __tablename__ = "claims"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    achievement_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("achievements.id")
    )
    status: Mapped[ClaimStatus] = mapped_column(
        String(20), default=ClaimStatus.PENDING
    )
    proof_url: Mapped[str | None] = mapped_column(
        String(255), nullable=True, default=None
    )
    claimed_at: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(timezone.utc)
    )
    reviewed_at: Mapped[datetime | None] = mapped_column(
        DateTime, nullable=True, default=None
    )
    reviewed_by: Mapped[int | None] = mapped_column(
        Integer, ForeignKey("users.id"), nullable=True, default=None
    )

    user: Mapped["User"] = relationship(
        back_populates="claims", foreign_keys=[user_id]
    )
    reviewer: Mapped["User | None"] = relationship(
        back_populates="reviewed_claims", foreign_keys=[reviewed_by]
    )
    achievement: Mapped["Achievement"] = relationship(back_populates="claims")

    def __repr__(self) -> str:
        return (
            f"<Claim user_id={self.user_id} " +
            f"achievement_id={self.achievement_id} " +
            f"status={self.status.value}>"
        )
