import os
from flask_reddit import app

def runserver():
    port = int(os.environ.get('PORT', 8000))
    app.run(host='127.0.0.1', port=port, debug=True)

if __name__ == '__main__':
    runserver()
