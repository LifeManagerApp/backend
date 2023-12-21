from app.app import app
import finance.routs.auth.routs
import finance.routs.categories.routes
from finance.routs.common import routes
from finance.models.cli import create_db

app.register_blueprint(routes)

if __name__ == '__main__':
    create_db()
    app.run(debug=True, host='0.0.0.0', port=9000)
