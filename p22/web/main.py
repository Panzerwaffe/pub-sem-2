from .models import db
from .routes import app

from .utils import init_database, fill_database
from .database import basedir

# create app
app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{basedir}/app.db'
db.init_app(app)

init_database(app, db)
fill_database(app, db)
