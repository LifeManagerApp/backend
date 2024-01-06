import os
from dotenv import load_dotenv
from common.logger import logger

if os.path.exists('.env'):
    load_dotenv('.env')
    logger.info('.env loaded successful')
else:
    logger.error('.env file is not detected')

from app.app import app
import finance.routs.auth.routes
import finance.routs.categories.routes
import finance.routs.money_management.routes
from finance.routs.common_rotes import routes
from finance.models.cli import create_db

app.register_blueprint(routes)

if __name__ == '__main__':
    create_db()
    app.run(debug=True, host='0.0.0.0', port=9000)
