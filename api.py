import os
from dotenv import load_dotenv

if os.path.exists('../../.env'):
    load_dotenv('../../.env')
    print('.env loaded successful')
else:
    print(os.getcwd())
    load_dotenv('.env')
    print('fuck you')

from app.app import app
import finance.routs.auth.routs
import finance.routs.categories.routes
import finance.routs.money_management.routes
from finance.routs.common import routes
from finance.models.cli import create_db

app.register_blueprint(routes)

if __name__ == '__main__':
    create_db()
    app.run(debug=True, host='0.0.0.0', port=9000)
