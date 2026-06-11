"""
Database models
Defines the structure of User, Achievement, and Claim entities
"""

from datetime import datetime
from extensions import db


class User(db.Model):
    """User model - represents a 42 school student or staff member"""
    __tablename__ = "users"

    # Unique identifier in the application database
    id = db.Column(db.Integer, primary_key=True)
    
    # 42 Intra unique user ID
    ft_id = db.Column(db.Integer, unique=True, nullable=False)
    
    # 42 login (e.g., "jdoe")
    login = db.Column(db.String(50), unique=True, nullable=False)
    
    # User email address
    email = db.Column(db.String(120), nullable=False)
    
    # Display name for the user profile
    display_name = db.Column(db.String(100), nullable=False)
    
    # Whether user has staff/admin privileges
    is_staff = db.Column(db.Boolean, default=False)
    
    # Timestamp when user account was created
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship: Claims made by this user
    claims = db.relationship("Claim", backref="user", lazy=True, foreign_keys="Claim.user_id")
    
    # Relationship: Claims reviewed by this staff member
    reviewed_claims = db.relationship("Claim", backref="reviewer", lazy=True, foreign_keys="Claim.reviewed_by")
    
    def __repr__(self):
        return f"<User {self.login} (ft_id={self.ft_id})>"


class Achievement(db.Model):
    """Achievement model - represents a gamification badge/reward"""
    __tablename__ = "achievements"
    
    # Unique identifier in the achievements database
    id = db.Column(db.Integer, primary_key=True)
    
    # Unique achievement name/title
    name = db.Column(db.String(100), unique=True, nullable=False)
    
    # Description of the achievement and how to earn it
    description = db.Column(db.String(255), nullable=False)
    
    # Category: "project", "social", "scolarity", "pedagogy"
    category = db.Column(db.String(50), nullable=False)
    
    # How to verify the achievement: "api_check", "manual", "photo"
    condition_type = db.Column(db.String(50), nullable=False)
    
    # Data needed for verification (e.g., project slug for API check)
    condition_data = db.Column(db.String(255), nullable=True)
    
    # Wallet points awarded for claiming this achievement
    wallet_reward = db.Column(db.Integer, default=0)
    
    # Relationship: Claims for this achievement
    claims = db.relationship("Claim", backref="achievement", lazy=True)
    
    def __repr__(self):
        return f"<Achievement {self.name} ({self.category})>"


class Claim(db.Model):
    """Claim model - represents a user's claim for an achievement"""
    __tablename__ = "claims"
    
    # Unique identifier for the claim
    id = db.Column(db.Integer, primary_key=True)
    
    # Foreign key: User who claimed the achievement
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    
    # Foreign key: Achievement being claimed
    achievement_id = db.Column(db.Integer, db.ForeignKey("achievements.id"), nullable=False)
    
    # Claim status: "pending", "approved", "rejected"
    status = db.Column(db.String(20), default="pending")
    
    # URL to proof (e.g., screenshot for photo verification)
    proof_url = db.Column(db.String(255), nullable=True)
    
    # Timestamp when the claim was submitted
    claimed_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Timestamp when the claim was reviewed (null if pending)
    reviewed_at = db.Column(db.DateTime, nullable=True)
    
    # Foreign key: Staff member who reviewed the claim (null if not reviewed)
    reviewed_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    
    def __repr__(self):
        return f"<Claim user_id={self.user_id} achievement_id={self.achievement_id} status={self.status}>"
