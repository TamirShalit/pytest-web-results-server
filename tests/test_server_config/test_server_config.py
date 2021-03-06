import os

import pytest

from tests import utils
from webresultserver import app_factory
from webresultserver.app_factory import DB_URI_CONFIG_KEY

_CURRENT_DIRECTORY = os.path.dirname(__file__)

_TEST_CONFIG_LOCATION = os.path.join(_CURRENT_DIRECTORY, 'test_config.json')
_EMPTY_CONFIG_LOCATION = os.path.join(_CURRENT_DIRECTORY, 'empty_config.json')


def test_load_config():
    with utils.use_config(_TEST_CONFIG_LOCATION):
        app = app_factory.create_app(__name__)
        assert app.config[DB_URI_CONFIG_KEY] == 'sqlite:///not_exist'


def test_exception_raised_when_no_db_uri():
    with utils.use_config(_EMPTY_CONFIG_LOCATION):
        with pytest.raises(ValueError):
            app_factory.create_app(__name__)
