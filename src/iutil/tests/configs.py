import os


FAST_MODE = os.environ.get('FAST_MODE', 'FALSE').upper() == 'TRUE'
