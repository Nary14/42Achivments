"""
Application configuration
Loads settings from environment variables and defines Flask/OAuth2/database configuration
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Flask application configuration class"""
    
    # Secret key for session encryption and CSRF protection
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")
    
    # PostgreSQL database connection URL
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/42achievements")
    
    # Disable SQLAlchemy modification tracking to reduce memory usage
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # 42 School OAuth2 Client ID
    FT_CLIENT_ID = os.getenv("FT_CLIENT_ID")
    
    # 42 School OAuth2 Client Secret
    FT_CLIENT_SECRET = os.getenv("FT_CLIENT_SECRET")
    
    # Redirect URI after 42 OAuth2 authentication
    FT_REDIRECT_URI = os.getenv("FT_REDIRECT_URI", "http://localhost:5000/auth/callback")
    
    # 42 School OAuth2 authorization endpoint
    FT_AUTH_URL = "https://api.intra.42.fr/oauth/authorize"
    
    # 42 School OAuth2 token endpoint
    FT_TOKEN_URL = "https://api.intra.42.fr/oauth/token"
    
    # 42 School API base URL for user data requests
    FT_API_BASE = "https://api.intra.42.fr/v2"
