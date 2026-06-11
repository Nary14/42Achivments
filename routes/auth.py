"""
Authentication routes
Handles user login/logout via 42 School OAuth2 provider
"""

import os
import requests
from flask import Blueprint, session, redirect, request, url_for
from config import Config
from extensions import db
from models import User

# Create Blueprint for authentication routes
auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.route("/login", methods=["GET"])
def login():
    """
    Initiates 42 OAuth2 login flow
    Redirects user to 42 authorization page
    """
    # # Generate random state for CSRF protection
    # state = os.urandom(16).hex()
    
    # # Store state in session to verify in callback
    # session["oauth_state"] = state
    
    # Build 42 authorization URL
    auth_url = (
        f"{Config.FT_AUTH_URL}"
        f"?client_id={Config.FT_CLIENT_ID}"
        f"&redirect_uri={Config.FT_REDIRECT_URI}"
        f"&response_type=code"
        # f"&state={state}"
    )
    
    # Redirect user to 42 login page
    return redirect(auth_url)


@auth_bp.route("/callback", methods=["GET"])
def callback():
    """
    OAuth2 callback handler
    Exchanges authorization code for access token and creates/updates user
    """
    # Extract code and state from 42 response
    code = request.args.get("code")
    state = request.args.get("state")
    
    # Verify state matches to prevent CSRF attacks
    # if state != session.get("oauth_state"):
    #     return "Invalid state parameter - CSRF attack detected", 403
    # TODO: réactiver en production avec stockage state en DB
    # Pour le POC, on skip la vérification CSRF
    # Exchange authorization code for access token
    token_data = {
        "grant_type": "authorization_code",
        "client_id": Config.FT_CLIENT_ID,
        "client_secret": Config.FT_CLIENT_SECRET,
        "code": code,
        "redirect_uri": Config.FT_REDIRECT_URI,
    }
    
    token_response = requests.post(Config.FT_TOKEN_URL, data=token_data)
    token_response.raise_for_status()
    
    access_token = token_response.json()["access_token"]
    
    # Use access token to fetch user profile from 42 API
    headers = {"Authorization": f"Bearer {access_token}"}
    user_response = requests.get(f"{Config.FT_API_BASE}/me", headers=headers)
    user_response.raise_for_status()
    
    user_data = user_response.json()
    
    # Create or update user in database (upsert by ft_id)
    user = User.query.filter_by(ft_id=user_data["id"]).first()
    
    if user:
        # Update existing user
        user.login = user_data["login"]
        user.email = user_data["email"]
        user.display_name = user_data.get("displayname", user_data["login"])
    else:
        # Create new user
        user = User(
            ft_id=user_data["id"],
            login=user_data["login"],
            email=user_data["email"],
            display_name=user_data.get("displayname", user_data["login"]),
            is_staff=False,
        )
        db.session.add(user)
    
    # Commit user to database
    db.session.commit()
    
    # Store user ID in session
    session["user_id"] = user.id
    session["user_login"] = user.login
    
    # Clear OAuth state from session
    session.pop("oauth_state", None)
    
    # Redirect to achievements page
    return redirect(url_for("achievements.view_achievements"))


@auth_bp.route("/logout", methods=["GET"])
def logout():
    """
    Logout handler
    Clears user session and redirects to login page
    """
    # Clear all session data
    session.clear()
    
    # Redirect to login page
    return redirect(url_for("auth.login"))
