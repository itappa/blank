import os
from pathlib import Path

from .base import *

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DEBUG = True
USE_TAILWIND_CDN = True

INSTALLED_APPS += ("debug_toolbar",)
MIDDLEWARE += ("debug_toolbar.middleware.DebugToolbarMiddleware",)

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
