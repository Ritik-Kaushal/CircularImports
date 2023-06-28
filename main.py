# ---------- Imports ----------

from instances.app import app
from instances.database import db
from application.config import *
import routes


# --------- Binding and Configurations ----------
print("----- Starting the local development -----")
app.config.from_object(LocalDevelopmentConfig) # Configures the LocalDevelopmentConfig data with the app\

db.init_app(app) # A way to safely bind database handler to flask and manage connections
app.app_context().push()

if __name__ == '__main__':
    app.run()