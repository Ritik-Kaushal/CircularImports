# -------------- IMPORTING THE REQUIRED MODULES --------------- #
import os

# -------------- PATH OF BASE DIRECTORY --------------- #
basedir = os.path.abspath(os.path.dirname(__file__)) # path of the base directory


# -------------- CONFIGURATION CLASSES --------------- #
class Config():
    """
    Base class for some common configurations of the Flask App.
    """

    DEBUG = False
    SQLITE_DB_DIR = None
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class LocalDevelopmentConfig(Config):
    """
    Class for some common configurations of the Flask App related to Local Development.
    """

    ##### Flask APP Config #####
    DEBUG = True

    ##### Database Config #####
    SQLITE_DB_DIR = os.path.join(basedir, '../instances')
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(SQLITE_DB_DIR, "db.sqlite3")