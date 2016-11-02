from app import create_app
from app.models import Movie

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8100, debug=True)
