"""The whistle (Finnish: pilli, German: Der Pfiff) parsing random DAFIF like data."""
import os
from typing import List

APP_NAME = 'The whistle (Finnish: pilli, German: Der Pfiff) parsing random DAFIF like data.'
APP_ALIAS = 'pilli'
APP_ENV = 'PILLI'
DEBUG = bool(os.getenv(f'{APP_ENV}_DEBUG', ''))
VERBOSE = bool(os.getenv(f'{APP_ENV}_VERBOSE', ''))
QUIET = False
STRICT = bool(os.getenv(f'{APP_ENV}_STRICT', ''))
ENCODING = 'utf-8'
ENCODING_ERRORS_POLICY = 'ignore'
DEFAULT_CONFIG_NAME = '.pilli.json'
DEFAULT_LF_ONLY = 'YES'

# [[[fill git_describe()]]]
__version__ = '2022.7.28+parent.9fb117a4'
# [[[end]]] (checksum: a143e8c8551090fa81324b0683ba1a40)
__version_info__ = tuple(
    e if '-' not in e else e.split('-')[0] for part in __version__.split('+') for e in part.split('.') if e != 'parent'
)
__all__: List[str] = []
