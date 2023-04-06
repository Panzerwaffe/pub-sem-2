from app import app
from routes import UserRoutes

UserRoutes(app)

if __name__ == "__main__":
    app.run()
