# -*- coding: utf-8 -*-
from __future__ import unicode_literals

try:
    from django.utils.six import text_type
except ImportError:
    import sys
    PY3 = sys.version_info[0] == 3
    text_type = str if PY3 else unicode

VERSION = (0, 12, 0)

__version__ = '.'.join(map(text_type, VERSION))
