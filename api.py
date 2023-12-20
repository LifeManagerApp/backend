from app.app import app
from finance.routs.auth.routs import routes

app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9000)
