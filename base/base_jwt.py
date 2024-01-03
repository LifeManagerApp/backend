import os


class JWT:
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
