from app.view import app
import config

config.load_google_credentials()

if __name__ == "__main__":
    app.run(debug=True)
