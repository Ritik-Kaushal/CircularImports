# ---------- Imports ----------

from instances.app import app

@app.route('/')
def home():
    return "<h1>Welcome to demo on preventing circular imports using global configurations</h1>"