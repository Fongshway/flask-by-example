import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', default="something-long-and-complicated-that-will-never-be-guessed")
