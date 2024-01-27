import os
from flask import Flask
from dotenv import load_dotenv
from flask_caching import Cache


class FlaskApp:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FlaskApp, cls).__new__(cls)
            cls._instance._init_app()
        return cls._instance

    def _init_app(self):
        load_dotenv()
        self.app = Flask(__name__)
        self._init_sessions()
        # self.cache = self._cache_config()

    def _init_sessions(self):
        self.app.static_folder = os.path.join(os.path.dirname(__file__), 'frontend', 'static')
        self.app.template_folder = os.path.join(os.path.dirname(__file__), 'frontend', 'templates')

    def _cache_config(self):
        cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
        cache.init_app(self.app)
        return cache

    def create_app(self):
        return self.app
