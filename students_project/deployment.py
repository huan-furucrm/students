import os
from .settings import *
from .settings import BASE_DIR
from azure.identity import DefaultAzureCredential
import psycopg2

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET']
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]
CSRF_TRUSTED_ORIGINS = ['https://' + os.environ['WEBSITE_HOSTNAME']]
DEBUG = False

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Uncomment the following lines corresponding to the authentication type you want to use.
# For system-assigned identity.
cred = DefaultAzureCredential()

# For user-assigned identity.
# managed_identity_client_id = os.getenv('AZURE_POSTGRESQL_CLIENTID')
# cred = ManagedIdentityCredential(client_id=managed_identity_client_id)    

# For service principal.
# tenant_id = os.getenv('AZURE_POSTGRESQL_TENANTID')
# client_id = os.getenv('AZURE_POSTGRESQL_CLIENTID')
# client_secret = os.getenv('AZURE_POSTGRESQL_CLIENTSECRET')
# cred = ClientSecretCredential(tenant_id=tenant_id, client_id=client_id, client_secret=client_secret)

# Acquire the access token.
accessToken = cred.get_token('https://ossrdbms-aad.database.windows.net/.default')
# In your setting file, eg. settings.py
host = os.getenv('AZURE_POSTGRESQL_HOST')
user = os.getenv('AZURE_POSTGRESQL_USER')
password = accessToken.token # this is accessToken acquired from above step.
database = os.getenv('AZURE_POSTGRESQL_NAME')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': database,
        'USER': user,
        'PASSWORD': password,
        'HOST': host,
        'PORT': '5432',  # Port is 5432 by default 
        'OPTIONS': {'sslmode': 'require'},
    }
}