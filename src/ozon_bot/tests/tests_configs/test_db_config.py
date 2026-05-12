import os
import pytest
from dotenv import load_dotenv
from src.ozon_bot.configs.config_db import settings

load_dotenv()

class TestConfigDB:
    @pytest.fixture
    def get_data_env(self) -> dict[str, str | int]:
        return {
            'USERNAME_PSQL': os.getenv("USERNAME_PSQL"),
            'PASSWORD_PSQL': os.getenv('PASSWORD_PSQL'),
            'HOST': os.getenv('HOST'),
            'PORT': os.getenv('PORT')
        }

    def test_username_psql(self, get_data_env):
        assert settings['USERNAME_PSQL'] == get_data_env['USERNAME_PSQL']
        assert settings['USERNAME_PSQL'] is not None
        assert settings['USERNAME_PSQL'] != ""

    def test_password_psql(self, get_data_env):
        assert settings['PASSWORD_PSQL'] == get_data_env['PASSWORD_PSQL']
        assert settings['PASSWORD_PSQL'] is not None
        assert settings['PASSWORD_PSQL'] != ""

    def test_host(self, get_data_env):
        assert settings['HOST'] ==  get_data_env['HOST']
        assert settings['HOST'] is not None
        assert settings['HOST'] != ""

    def test_port(self, get_data_env):
        assert settings['PORT'] is not None
        assert settings['PORT'] is int(settings['PORT'])