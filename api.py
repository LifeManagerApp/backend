from app.app import app
import finance.routs.auth.routs
import finance.routs.categories.routes
from finance.routs.common import routes

app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000)
