from flask import Flask, jsonify, request
from flask.json import load

from os.path import join
from sqlite3 import connect, Row

# Flask setup
app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE = join(app.root_path, "cdh", "cdh.db"),
    SECRET_KEY="super special and very secret k3y",
    USERNAME = "captain",
    PASSWORD = "joshua"
))
app.config.from_envvar("DAIKAN_SETTINGS", silent=True)

# Database setup
def connectDB():
    """Connects to the ship database."""
    dbConnection = connect(app.config["DATABASE"])
    dbConnection.row_factory = Row
    return dbConnection

def getDBConnection():
    """Gets the current database connection. If none exist yet, will open a new one!"""

    if not hasattr(g, "sqliteDB"):
        g.sqliteDB = connectDB()
    return g.sqliteDB

@app.teardown_appcontext
def closeDB(error):
    """Closes any open database connection at the end of a request"""
    if hasattr(g, "sqliteDB"):
        g.sqliteDB.close()

def initDB():
    db = getDBConnection()
    with open(join("cdh", "schema.sql"), mode="r") as scheme:
        db.cursor().executescript(scheme.read())
    db.commit()

@app.cli.command("initdb")
def initdbCommand():
    """Initializes the database."""
    initDB()
    print("Database initialized")

# routing
@app.route("/")
def index():
    return "Welcome to the DAIKA command and data handling subsystem"

@app.route("/daikan/CDH/api/v0.1/subsystems", methods=["GET"])
def getSubsystems():
    return jsonify({"subsystems":subsystems})

@app.route("/daikan/<controllerID>/status")
@app.route("/daikan/CDH/api/v0.1/subsystems/<controllerID>", methods=["GET"])
def getSubsystemController(controllerID):
    controller = [ controller for controller in subsystems if controller ["id"]==controllerID]
    if len(controller) == 0:
        abort(404)
    elif len(controller) != 1:
        abort(400)

    return jsonify({"subsystems":controller[0]})


if __name__ == "__main__":
    app.run(debug=True)
