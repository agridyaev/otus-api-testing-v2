import os.path
from lib.helpers import get_path

FILES_DIR = os.path.dirname(__file__)


POST_SCHEMA_PATH = get_path(FILES_DIR, "post_schema.json")
POSTS_SCHEMA_PATH = get_path(FILES_DIR, "posts_schema.json")
