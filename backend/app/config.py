"""Application configuration for Orion."""

import os
from dotenv import load_dotenv

PROJECT_ROOT_ENV = os.path.join(os.path.dirname(__file__), '../../.env')

if os.path.exists(PROJECT_ROOT_ENV):
    load_dotenv(PROJECT_ROOT_ENV, override=True)
else:
    load_dotenv(override=True)


class Config:
    """Flask configuration."""

    SECRET_KEY = os.environ.get('SECRET_KEY', 'orion-local-dev-secret')
    DEBUG = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    JSON_AS_ASCII = False

    LLM_API_KEY = os.environ.get('LLM_API_KEY')
    LLM_BASE_URL = os.environ.get('LLM_BASE_URL', 'https://api.openai.com/v1')
    LLM_MODEL_NAME = os.environ.get('LLM_MODEL_NAME', 'gpt-4o-mini')

    ZEP_API_KEY = os.environ.get('ZEP_API_KEY')

    MAX_CONTENT_LENGTH = 50 * 1024 * 1024
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), '../uploads')
    ALLOWED_EXTENSIONS = {'pdf', 'md', 'txt', 'markdown', 'html', 'htm'}

    DEFAULT_CHUNK_SIZE = 500
    DEFAULT_CHUNK_OVERLAP = 50

    OASIS_DEFAULT_MAX_ROUNDS = int(os.environ.get('OASIS_DEFAULT_MAX_ROUNDS', '10'))
    OASIS_SIMULATION_DATA_DIR = os.path.join(os.path.dirname(__file__), '../uploads/simulations')

    OASIS_TWITTER_ACTIONS = [
        'CREATE_POST', 'LIKE_POST', 'REPOST', 'FOLLOW', 'DO_NOTHING', 'QUOTE_POST'
    ]
    OASIS_REDDIT_ACTIONS = [
        'LIKE_POST', 'DISLIKE_POST', 'CREATE_POST', 'CREATE_COMMENT',
        'LIKE_COMMENT', 'DISLIKE_COMMENT', 'SEARCH_POSTS', 'SEARCH_USER',
        'TREND', 'REFRESH', 'DO_NOTHING', 'FOLLOW', 'MUTE'
    ]

    REPORT_AGENT_MAX_TOOL_CALLS = int(os.environ.get('REPORT_AGENT_MAX_TOOL_CALLS', '5'))
    REPORT_AGENT_MAX_REFLECTION_ROUNDS = int(os.environ.get('REPORT_AGENT_MAX_REFLECTION_ROUNDS', '2'))
    REPORT_AGENT_TEMPERATURE = float(os.environ.get('REPORT_AGENT_TEMPERATURE', '0.5'))

    @classmethod
    def validate(cls):
        errors = []

        def missing_or_placeholder(value):
            return not value or value.startswith('replace_with_') or value.startswith('your_')

        if missing_or_placeholder(cls.LLM_API_KEY):
            errors.append('LLM_API_KEY is missing or still uses a placeholder value.')
        if missing_or_placeholder(cls.ZEP_API_KEY):
            errors.append('ZEP_API_KEY is missing or still uses a placeholder value.')
        return errors
