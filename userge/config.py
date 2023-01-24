# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020-2022 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/UsergeTeam/Userge/blob/master/LICENSE >
#
# All rights reserved.

from os import environ

import heroku3

from userge import logging
from .sys_tools import secured_env, secured_str

_LOG = logging.getLogger(__name__)

# try to get this value using eval :)
TEST = secured_str("nice! report @UsergeSpam")

API_ID = environ.get("API_ID", "17221046")
API_HASH = secured_env("API_HASH", "233ef51a2c05a3979f95d7c7730cf320")
BOT_TOKEN = secured_env("BOT_TOKEN", "5374347952:AAFiCJWAL3fdi8PB7RROVaq2z93LOYN07rk")
SESSION_STRING = secured_env("SESSION_STRING", " BQEGxbYAt9ZX598VRO1fNHhKI5q0xhuMDwyOSEMRjnREb9JN0a6T59kdN_dnVgm0NtsuYfFyAmPYouoo4I47iH_0xtdwmaR3_4Y212NPjBO-sqZtZgP1bxOHPe1-FyOCWiSwxS3buiHjCum-3uAMuZfvHMqitUFN8jHfJc5d0yyOpU4Av8r4tJOHfyQ0AW951gbBYn2Lt-CtH_4nNkvJOiBXus76JrJDhnySS91Azwy_CCyLaBnVTpwfnNM8u1ctKT7SrwJCPZwJPO6gNm0bpa8COq36fiE3OpoRMy6Qk8XeWWQZp1zECUZKxKGgPKAOjdfjcxaUvd2iN6IigyByHCPZfxwyKAAAAAE-C4dDAA")
DB_URI = secured_env("DATABASE_URL", "postgres://lsggilqx:yNzbAHBmq-qTgSS_UdkuGq8MOF9IXf7_@john.db.elephantsql.com/lsggilqx")

OWNER_ID = tuple(filter(lambda x: x, map(int, environ.get("OWNER_ID", "2139088940").split())))
LOG_CHANNEL_ID = int(environ.get("LOG_CHANNEL_ID", " logxmiaoo"))
AUTH_CHATS = (OWNER_ID[0], LOG_CHANNEL_ID) if OWNER_ID else (LOG_CHANNEL_ID,)

CMD_TRIGGER = environ.get("CMD_TRIGGER", ".")
SUDO_TRIGGER = environ.get("SUDO_TRIGGER", "2139088940")
PUBLIC_TRIGGER = '/'

WORKERS = int(environ.get("WORKERS"))
MAX_MESSAGE_LENGTH = 4096

FINISHED_PROGRESS_STR = environ.get("FINISHED_PROGRESS_STR")
UNFINISHED_PROGRESS_STR = environ.get("UNFINISHED_PROGRESS_STR")

HEROKU_API_KEY = secured_env("HEROKU_API_KEY")
HEROKU_APP_NAME = environ.get("HEROKU_APP_NAME")
HEROKU_APP = heroku3.from_key(HEROKU_API_KEY).apps()[HEROKU_APP_NAME] \
    if HEROKU_API_KEY and HEROKU_APP_NAME else None

ASSERT_SINGLE_INSTANCE = environ.get("ASSERT_SINGLE_INSTANCE", '').lower() == "true"
IGNORE_VERIFIED_CHATS = True


class Dynamic:
    DOWN_PATH = environ.get("DOWN_PATH")

    MSG_DELETE_TIMEOUT = 120
    EDIT_SLEEP_TIMEOUT = 10

    USER_IS_PREFERRED = False
