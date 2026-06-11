"""
Achievements routes
Displays user achievements and handles achievement claiming
"""

from functools import wraps
from datetime import datetime
import requests
from flask import Blueprint, session, redirect, render_template, url_for, jsonify, request
from config import Config
from extensions import db
from models import User, Achievement, Claim

# Create Blueprint for achievements routes
achievements_bp = Blueprint("achievements", __name__, url_prefix="/achievements")


def login_required(f):
    """
    Decorator to protect routes that require authentication
    Redirects to login if user_id not in session
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Check if user_id is in session
        if "user_id" not in session:
            # Redirect to login page if not authenticated
            return redirect(url_for("auth.login"))
        # Call the protected route function
        return f(*args, **kwargs)
    return decorated_function


@achievements_bp.route("/", methods=["GET"])
@login_required
def view_achievements():
    """
    Display all achievements for the current user
    Shows which achievements the user has already claimed
    """
    # Get current user from database using session user_id
    user = User.query.get(session["user_id"])
    if not user:
        # Clear invalid session and redirect to login
        session.clear()
        return redirect(url_for("auth.login"))
    
    # Get all achievements from database
    achievements = Achievement.query.all()
    
    # Get set of achievement IDs that user has approved claims for
    approved_claims = Claim.query.filter_by(
        user_id=user.id,
        status="approved"
    ).all()
    already_claimed = {claim.achievement_id for claim in approved_claims}
    
    # Render achievements page with user, achievements, and claimed status
    return render_template(
        "achievements.html",
        user=user,
        achievements=achievements,
        already_claimed=already_claimed
    )


@achievements_bp.route("/claim/<int:achievement_id>", methods=["POST"])
@login_required
def claim_achievement(achievement_id):
    """
    Handle user claiming an achievement
    Creates a new claim with pending status for review
    """
    # Get current user from database
    user = User.query.get(session["user_id"])
    if not user:
        return jsonify({"error": "User not found"}), 401
    
    # Get achievement by ID from database
    achievement = Achievement.query.get(achievement_id)
    if not achievement:
        # Return 404 if achievement doesn't exist
        return jsonify({"error": "Achievement not found"}), 404
    
    # Check if user already has a pending or approved claim for this achievement
    existing_claim = Claim.query.filter(
        Claim.user_id == user.id,
        Claim.achievement_id == achievement_id,
        Claim.status.in_(["pending", "approved"])
    ).first()
    
    if existing_claim:
        # User already claimed this achievement
        return jsonify({"error": "Already claimed"}), 400
    
    # Create new claim with pending status
    new_claim = Claim(
        user_id=user.id,
        achievement_id=achievement_id,
        status="pending",
        claimed_at=datetime.utcnow()
    )
    
    # Add and commit claim to database
    db.session.add(new_claim)
    db.session.commit()
    
    # Return success response with claim ID
    return jsonify({
        "success": True,
        "claim_id": new_claim.id,
        "message": "Achievement claimed successfully"
    }), 201
