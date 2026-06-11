"""
Database seed script
Initializes the database with default achievements
Run with: python seed.py
"""

from app import app
from models import Achievement
from extensions import db


def seed_database():
    """Initialize database with default achievements"""
    # Create an application context
    with app.app_context():
        # Create all database tables
        db.create_all()
        
        # Define default achievements
        achievements_data = [
            {
                "name": "42 is my answer 1",
                "description": "Être log le jour de son anniversaire",
                "category": "social",
                "condition_type": "manual",
                "wallet_reward": 1,
            },
            {
                "name": "Gally 0",
                "description": "Valider la Milestone 0",
                "category": "project",
                "condition_type": "api_check",
                "condition_data": "milestone-0",
                "wallet_reward": 2,
            },
            {
                "name": "Gally 1",
                "description": "Valider la Milestone 1",
                "category": "project",
                "condition_type": "api_check",
                "condition_data": "milestone-1",
                "wallet_reward": 3,
            },
            {
                "name": "Tyler Durden 1",
                "description": "Valider un projet en groupe",
                "category": "project",
                "condition_type": "manual",
                "wallet_reward": 2,
            },
            {
                "name": "Tongasoa Cadet I 1",
                "description": "Réussir sa piscine",
                "category": "scolarity",
                "condition_type": "manual",
                "wallet_reward": 5,
            },
        ]
        
        # Insert achievements if they don't already exist
        for achievement_data in achievements_data:
            # Check if achievement already exists by name
            existing = Achievement.query.filter_by(name=achievement_data["name"]).first()
            
            if not existing:
                # Create new achievement
                new_achievement = Achievement(
                    name=achievement_data["name"],
                    description=achievement_data["description"],
                    category=achievement_data["category"],
                    condition_type=achievement_data["condition_type"],
                    condition_data=achievement_data.get("condition_data"),
                    wallet_reward=achievement_data["wallet_reward"],
                )
                db.session.add(new_achievement)
        
        # Commit all changes to database
        db.session.commit()
        
        # Print success message
        print("DB initialisée avec succès")


if __name__ == "__main__":
    seed_database()
