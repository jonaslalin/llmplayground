import os
import re

import pytest


def get_openai_api_key() -> str:
    with open(".env") as f:
        dot_env = f.read()
    p = re.compile(r"^OPENAI_API_KEY=(?P<openai_api_key>.*)$", re.MULTILINE)
    m = p.search(dot_env)
    assert m, "Couldn't find OPENAI_API_KEY in .env"
    openai_api_key = m.group("openai_api_key")
    return openai_api_key


@pytest.fixture(scope="session", autouse=True)
def set_openai_api_key() -> None:
    os.environ["OPENAI_API_KEY"] = get_openai_api_key()
