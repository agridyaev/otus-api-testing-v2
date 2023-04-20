import json
from jsonschema import validate
from schemas import POST_SCHEMA_PATH, POSTS_SCHEMA_PATH


def assert_valid_schema(data, schema_file):
    with open(schema_file) as f:
        schema = json.load(f)
    return validate(instance=data, schema=schema)


def test_get_post(session, base_url):
    res = session.get(url=f'{base_url}/posts/1')
    assert_valid_schema(res.json(), POST_SCHEMA_PATH)


def test_get_posts(session, base_url):
    res = session.get(url=f'{base_url}/posts')
    assert_valid_schema(res.json(), POSTS_SCHEMA_PATH)
