import os
from os.path import dirname
from os.path import join

# from dotenv import load_dotenv

#dotenv_path = join(dirname(__file__), os.getenv("ENVIRONMENT_FILE"))
#load_dotenv(dotenv_path=dotenv_path, override=True)

APP_HOST = "127.0.0.1" # os.environ.get("HOST")
APP_PORT = 8085 # int(os.environ.get("PORT"))
APP_DEBUG = True # bool(os.environ.get("DEBUG"))
DEV_TOOLS_PROPS_CHECK = True # bool(os.environ.get("DEV_TOOLS_PROPS_CHECK"))
