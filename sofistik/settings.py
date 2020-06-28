from .base import *
from decouple import config, Csv


INSTALLED_APPS += (
	# Proje içi appler
	'home',
	#3. Parti Paketler
	'crispy_forms',
	'ckeditor',
	)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CRISPY_TEMPLATE_PACK = "bootstrap4"

CKEDITOR_jQUERY_URL = os.path.join(STATIC_URL, "assets/vendor/jquery")
CKEDITOR_CONFIGS = {
	'default': {
		'toolbar': 'full',
		'width':'100%',
		'height':'50%',
		'codeSnippet_theme':'school_book',
	},
}



from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}