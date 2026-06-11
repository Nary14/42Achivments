import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "sqlite:///app.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv(
        "SQLALCHEMY_TRACK_MODIFICATIONS"
    )
    # 42 School OAuth2 Client ID
    FT_CLIENT_ID = os.getenv("FT_CLIENT_ID")

    # 42 School OAuth2 Client Secret
    FT_CLIENT_SECRET = os.getenv("FT_CLIENT_SECRET")

    # Redirect URI after 42 OAuth2 authentication
    FT_REDIRECT_URI = os.getenv("FT_REDIRECT_URI")

    # 42 School OAuth2 authorization endpoint
    FT_AUTH_URL = os.getenv("FT_AUTH_URL")

    # 42 School OAuth2 token endpoint
    FT_TOKEN_URL = os.getenv("FT_TOKEN_URL")

    # 42 School API base URL for user data requests
    FT_API_BASE = os.getenv("FT_API_BASE")
