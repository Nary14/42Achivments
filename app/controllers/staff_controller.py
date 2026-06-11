"""
Staff dashboard routes
Admin panel for viewing user data and managing achievements (Bocal only)
"""

from functools import wraps
from datetime import datetime
from flask import Blueprint, session, redirect, render_template, url_for
from flask import jsonify
from app import db
from app.models import User, Claim


# Create Blueprint for staff routes
staff_bp = Blueprint("staff", __name__, url_prefix="/staff")


def staff_required(f):
    """
    Decorator to protect routes that require staff privileges
    First checks if user is logged in, then checks if user is staff
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # First check if user is logged in using login_required logic
        if "user_id" not in session:
            # Redirect to login if not authenticated
            return redirect(url_for("auth.login"))
        # Get user from database
        user = User.query.get(session["user_id"])
        if not user:
            # Clear invalid session if user doesn't exist
            session.clear()
            return redirect(url_for("auth.login"))
        # Check if user has staff privileges
        if not user.is_staff:
            # Return 403 Forbidden if not staff
            return jsonify({"error": "Access denied"}), 403
        # Call the protected route function if all checks pass
        return f(*args, **kwargs)
    return decorated_function


@staff_bp.route("/dashboard", methods=["GET"])
@staff_required
def dashboard():
    """
    Staff dashboard showing pending claims and statistics
    Displays all pending claims for review with user and achievement info
    """
    # Get all pending claims with relationships
    pending_claims = Claim.query.filter_by(status="pending").all()
    # Calculate statistics for the dashboard
    total_claims = Claim.query.count()
    pending_count = Claim.query.filter_by(status="pending").count()
    approved_count = Claim.query.filter_by(status="approved").count()
    rejected_count = Claim.query.filter_by(status="rejected").count()
    # Create statistics dictionary
    stats = {
        "total": total_claims,
        "pending": pending_count,
        "approved": approved_count,
        "rejected": rejected_count,
    }
    # Render staff dashboard with claims and statistics
    return render_template(
        "staff.html",
        claims=pending_claims,
        stats=stats
    )


@staff_bp.route("/claim/<int:claim_id>/approve", methods=["POST"])
@staff_required
def approve_claim(claim_id):
    """
    Approve a pending achievement claim
    Updates claim status and records reviewer information
    """
    # Get claim by ID from database
    claim = Claim.query.get(claim_id)
    if not claim:
        # Return 404 if claim doesn't exist
        return jsonify({"error": "Claim not found"}), 404
    # Get current staff user
    staff_user = User.query.get(session["user_id"])
    # Update claim status to approved
    claim.status = "approved"
    # Record when claim was reviewed
    claim.reviewed_at = datetime.utcnow()
    # Record which staff member reviewed the claim
    claim.reviewed_by = staff_user.id
    # Commit changes to database
    db.session.commit()
    # Return success response
    return jsonify({
        "success": True,
        "message": "Claim approved successfully"
    }), 200


@staff_bp.route("/claim/<int:claim_id>/reject", methods=["POST"])
@staff_required
def reject_claim(claim_id):
    """
    Reject a pending achievement claim
    Updates claim status and records reviewer information
    """
    # Get claim by ID from database
    claim = Claim.query.get(claim_id)
    if not claim:
        # Return 404 if claim doesn't exist
        return jsonify({"error": "Claim not found"}), 404
    # Get current staff user
    staff_user = User.query.get(session["user_id"])
    # Update claim status to rejected
    claim.status = "rejected"
    # Record when claim was reviewed
    claim.reviewed_at = datetime.utcnow()
    # Record which staff member reviewed the claim
    claim.reviewed_by = staff_user.id
    # Commit changes to database
    db.session.commit()
    # Return success response
    return jsonify({
        "success": True,
        "message": "Claim rejected successfully"
    }), 200


@staff_bp.route("/promote/<int:user_id>", methods=["GET"])
@staff_required
def promote_user(user_id):
    """
    Promote a user to staff status
    Grants admin privileges to the specified user
    (used for bootstrapping staff)
    """
    # Get user by ID from database
    user = User.query.get(user_id)
    if not user:
        # Return 404 if user doesn't exist
        return jsonify({"error": "User not found"}), 404
    # Set user as staff
    user.is_staff = True
    # Commit changes to database
    db.session.commit()
    # Return success response
    return jsonify({
        "success": True,
        "message": f"User {user.login} promoted to staff"
    }), 200
