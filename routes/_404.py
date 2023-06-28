# ---------- Imports ----------

from instances.app import app

@app.errorhandler(404)
def pageNotFound(e):
    return "The url doesnot exist."