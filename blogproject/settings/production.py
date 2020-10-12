from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
# SECRET_KEY = 'wo$ok6&o#bx_httgy9e(*-+cl6^+1&067d80k#9gqk!9m(35th'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['lechangagriculture.cn']
