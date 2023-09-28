import os
import datetime
from dotenv import load_dotenv

load_dotenv(".env")


class App_Config:
    """_summary_"""

    SECRET_KEY = os.environ.get("SECRET_KEY", "test")

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI", "sqlite:///test.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    

  