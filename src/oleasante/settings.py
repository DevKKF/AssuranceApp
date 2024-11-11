"""
Django settings for oleasante project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from datetime import timedelta
import os
from pathlib import Path
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

from environ import environ

env = environ.Env()
environ.Env.read_env(env_file=str(BASE_DIR / "oleasante" / ".env"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", False)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

BASE = env("BASE")  # PROD OU PREPROD

# Application definition

INSTALLED_APPS = [
    "admin_custom",
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_json_widget",
    "configurations",
    "production",
    "sinistre",
    "comptabilite",
    "import_export",
    "django_dump_die",
    "django_crontab",
    "rest_framework",
    "rest_framework_simplejwt",
    "api",
    "grh",
]

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
    ],
    #
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
}

MIDDLEWARE = [
    "django_dump_die.middleware.DumpAndDieMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    #'django_session_timeout.middleware.SessionTimeoutMiddleware',
    "django.middleware.locale.LocaleMiddleware",
    # 'crum.CurrentRequestUserMiddleware',  # added on 01072022
    "configurations.middlewares.ForcePasswordChangeMiddleware",  # added on 30082023
    #'configurations.middlewares.AnonymousUserMiddleware',  # added on 16122023
    # GRH
    "grh.middleware.AuthenticationMiddleware",
    # 2fa
    "configurations.middlewares.AuthRedirectMiddleware",  # added on 16122023
    "django_currentuser.middleware.ThreadLocalUserMiddleware",
]

ROOT_URLCONF = "oleasante.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.media",
            ],
        },
    },
]

WSGI_APPLICATION = "oleasante.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": env("DATABASE_NAME"),
        "USER": env("DATABASE_USER"),
        "PASSWORD": env("DATABASE_PWD"),
        "HOST": env("DATABASE_HOST"),
        "PORT": env("DATABASE_PORT"),
        # "OPTIONS": {"ssl_mode": "DISABLED"},
        #'OPTIONS': {
        #   'charset': 'utf8mb3',
        # },
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "fr-fr"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Provide a lists of languages which your site supports.
LANGUAGE = (
    ("fr", _("Français")),
    ("en", _("English")),
)

PAGE_LANGUAGES = "PAGE_LANGUAGES"

# LOGIN_REDIRECT_URL = 'https://google.com'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = "/static/"
MEDIA_URL = "/media/"
if env.str("ENVIRONMENT", "DEV") == "PROD":
    STATIC_ROOT = env.str("STATIC_ROOT", "/home/oleasante.com/public_html/static/")
    MEDIA_ROOT = env.str("MEDIA_ROOT", "/home/oleasante.com/public_html/media/")


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "configurations.User"

# Contains the path list where Django should look into for django.po files for all supported languages
LOCALE_PATHS = (os.path.join(BASE_DIR, "locale"),)


JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Assurance App",
    "site_brand": "Assurance App",
    "site_header": "Assurance App",
    "site_logo": "configurations/images/logo_sante.png",
    "site_logo_classes": "custom-logo",
    # "logo_for_carte": "https://storage.gra.cloud.ovh.net/v1/AUTH_e15f6f9849b947e9845253c522fb5927/oleasante/public/medias/original/mxkiNNUNxvlYW5uYQidvYKxUVVgB5VfKEDtl02hg.png",
    "logo_for_carte": "http://127.0.0.1:8000/static/configurations/images/logo_sante.png",
    # "search_model": AUTH_USER_MODEL,
    "order_with_respect_to": [
        "auth",
        "configurations",
        "production",
        "sinistre",
        "comptabilite",
        "Rubriques",
        "Sous-rubriques",
        "Sous actes",
    ],
    "custom_links": {
        "auth": [
            {
                "name": "Utilisateurs",
                "url": "admin:configurations_user_changelist",
                "icon": "fa fa-user",
                # "icon": "fa fa-list",
                "permissions": ["auth.view_user"],
            }
        ],
        "production": [
            {
                "name": "Mouvements GRH",
                "url": "prospects",
                # "icon": "fa fa-user",
                # "icon": "fa fa-list",
                # "permissions": ["production.view_prospect"]
            },
            # {
            #    "name": "Assurance universelle",
            #    "url": "formules_universelles",
            #    # "icon": "fa fa-user",
            #    # "icon": "fa fa-list",
            #    #"permissions": ["production.view_prospect"]
            # },
            {
                "name": "Annuler une quittance",
                "url": "annuler_quittance",
                "icon": "fa fa-times",
                "permissions": ["production.can_do_annulation_quittance"],
            },
        ],
        "sinistre": [
            {
                "name": "Demandes Remb. app mobile",
                "url": "admin:sinistre_demanderemboursementmobile_changelist",
                "permissions": ["sinistre.can_do_saisie_gestionnaire"],
            },
            {
                "name": "Liste des dossiers traités",
                "url": "dossierstraites",
                # "icon": "fa fa-checked",
                "permissions": ["sinistre.review_sinistre"],
            },
            {
                "name": "Saisir un dossier sinistre",
                "url": "saisie_prestation",
                "icon": "fa fa-plus-circle",
                "permissions": ["sinistre.can_do_saisie_gestionnaire"],
            },
            {
                "name": "Générer facture remb.",
                "url": "generation_bordereau",
                "icon": "fas fa-file-invoice",
                "permissions": ["sinistre.can_do_generation_bordereau_facturation"],
            },
            {
                "name": "Bordereau de facturation",
                "url": "liste_bordereau",
                "icon": "fa fa-file-alt",
                "permissions": ["sinistre.can_view_bordereaux_facturations"],
            },
            {
                "name": "Factures à traiter",
                "url": "facturesprestataires",
                "icon": "fa fa-file-o",
                "permissions": ["sinistre.can_view_facturesprestataires_en_attente"],
            },
            {
                "name": "Générer Brouillard de saisie",
                "url": "generation_br_validation",
                "icon": "fa fa-check",
                "permissions": ["sinistre.can_view_remboursements_validees"],
            },
            {
                "name": "Liste dossiers sinistres",
                "url": "liste_prestations",
                "icon": "fa fa-list",
                "permissions": ["sinistre.can_view_prestations"],
            },
            {
                "name": "Factures traitées validées",
                "url": "facturesprestataires_traite",
                "icon": "fa fa-check-circle",
                "permissions": ["sinistre.can_view_facturesprestataires_validees"],
            },
            {
                "name": "Ordonnancement",
                "url": "generation_br_ordonnancement",
                "icon": "fa fa-money",
                "permissions": ["sinistre.can_do_ordonnancement"],
            },
            {
                "name": "Bordereaux ordonnancés",
                "url": "bordereaux_ordonnances",
                "icon": "far fa-credit-card",
                "permissions": ["sinistre.can_view_bordereaux_ordonnancement"],
            },
            {
                "name": "Bordereaux payés",
                "url": "bordereaux_payes",
                "icon": "far fa-credit-card",
                "permissions": ["sinistre.can_view_bordereaux_ordonnancement"],
            },
            {
                "name": "Exec. requêtes excel",
                "url": "execution_requete_excel",
                "icon": "far fa-file-excel-o",
                "permissions": ["sinistre.can_view_bordereaux_ordonnancement"],
            },
            {
                "name": "Requête en arrière-plan",
                "url": "admin:configurations_backgroundquerytask_changelist",
                "icon": "far fa-file-excel-o",
                # "icon": "fa fa-list",
                "permissions": ["sinistre.can_view_bordereaux_ordonnancement"],
            },
            {
                "name": "Annuler un sinistre",
                "url": "annuler_sinistre",
                "icon": "fa fa-times",
                "permissions": ["sinistre.can_do_annulation_sinistre"],
            },
            {
                "name": "Annuler une facture",
                "url": "annuler_facture",
                "icon": "fa fa-times",
                "permissions": ["sinistre.can_do_annulation_facture"],
            },
        ],
        "comptabilite": [
            {
                "name": "Bordereaux payés",
                "url": "bordereaux_payes_compta",
                # "icon": "fa fa-times",
                "permissions": ["comptabilite.can_do_reglement_compagnie"],
            },
            {
                "name": "Edition de lettre chèque",
                "url": "edition-lettre-cheque",  #
                # "icon": "fa fa-times",
                "permissions": ["comptabilite.can_do_reglement_compagnie"],
            },
            {
                "name": "Historique des lettres Chèques",
                "url": "admin:configurations_bordereaulettrecheque_changelist",
                # "icon": "far fa-file-excel-o",
                # "icon": "fa fa-list",
                # "permissions": ["configuration.can_do_reglement_compagnie"]
            },
            {
                "name": "Paiements réalisés",
                "url": "paiements-realises",  #
                # "icon": "fa fa-times",
                "permissions": ["comptabilite.can_do_reglement_compagnie"],
            },
            {
                "name": "Règlements compagnies",
                "url": "reglements_compagnies",
                "icon": "fa fa-money",
                "permissions": ["comptabilite.can_do_reglement_compagnie"],
            },
            {
                "name": "Encais. com. courtage",
                "url": "encaissement_commissions_court_gest_courtage",
                "icon": "fa fa-money",
                "permissions": ["comptabilite.can_do_reglement_compagnie"],
            },
            {
                "name": "Encais. com. gestion",
                "url": "encaissement_commissions_court_gest_gestion",
                "icon": "fa fa-money",
                "permissions": ["comptabilite.can_do_reglement_compagnie"],
            },
            # {
            #    "name": "Règlements Apporteurs",
            #    "url": "reglements_apporteurs",
            #    "icon": "fa fa-money",
            #    "permissions": ["comptabilite.can_do_reglement_compagnie"]
            # },
            # A commenter sur jusqu'à la mise en prod de ces fonctionnalités
            {
                "name": "Fonds de roulements",
                "url": "initialisation_fonds_de_roulements",
                # "icon": "fa fa-times",
                "permissions": ["comptabilite.can_do_reglement_compagnie"],
            },
            {
                "name": "Refacturation garant",
                "url": "refacturation_assureur",
                # "icon": "fa fa-times",
                "permissions": [
                    "comptabilite.can_do_reglement_compagnie"
                ],  # remplacer sinistre par comptabilite
            },
            {
                "name": "Suivi factures garants",
                "url": "factures_compagnies",
                # "icon": "fa fa-times",
                "permissions": ["comptabilite.can_do_reglement_compagnie"],
            },
            {
                "name": "Suivi de la tresorerie",
                "url": "suivi-tresorerie",
                # "icon": "fa fa-chart-pie",
                "permissions": [
                    "comptabilite.can_do_reglement_compagnie"
                ],  # remplacer sinistre par comptabilite
            },
            # A commenter sur jusqu'à la mise en prod de ces fonctionnalités
            {
                "name": "Exec. requêtes excel",
                "url": "execution_requete_excel_compta",
                "icon": "far fa-file-excel-o",
                # "permissions": ["sinistre.can_view_bordereaux_ordonnancement"]
            },
            {
                "name": "Requête en arrière-plan",
                "url": "admin:configurations_backgroundquerytask_changelist",
                "icon": "far fa-file-excel-o",
                # "icon": "fa fa-list",
                # "permissions": ["configuration.can_view_backgroundquerytask"]
            },
        ],
        "configurations": [
            {
                "name": "Gestion Ws Boby",
                "url": "ws_bobys",
                # "icon": "fa fa-times",
                "permissions": ["configurations.view_wsbooby"],
            },
            {
                "name": "Action super admin",
                "url": "db_super_admin_query",
                # "icon": "fa fa-times",
                "permissions": ["configurations.view_wsbooby"],
            },
        ],
    },
    "hide_models": [
        #'configurations.User',
        "comptabilite.ReglementApporteurs",
        "configurations.BackgroundQueryTask",
        "configurations.BordereauLettreCheque",
    ],
    "icons": {
        "configurations": "fas fa-cogs",
        "production": "fas fa-box",
        "sinistre": "fas fa-head-side-cough",
        "comptabilite": "fas fa-money-bill",
        "auth": "fas fa-user-shield",
        "auth.Group": "fas fa-users",
    },
    "related_modal_active": True,
    "navigation_expanded": False,
    "custom_css": "admin_custom/css/style.css",
    "custom_js": "admin_custom/js/custom_js.js",
    "copyright": "OLEA SANTE",
    "version": "2.0",
    "environnement": BASE,
    # Add a language dropdown into the admin
    "language_chooser": True,
    "PAGE_LANGUAGES": LANGUAGE,
}


# HELP HERE : https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=365),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=365),
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(days=365),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=365),
    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}

X_FRAME_OPTIONS = "SAMEORIGIN"

IMPORT_EXPORT_USE_TRANSACTIONS = True


CRONJOBS = [
    # ('0 22 * * *', 'oleasante.cron.cron_pays'),
    # ('0 22 * * *', 'oleasante.cron.cron_bureau'),
    # ('0 22 * * *', 'oleasante.cron.cron_devise'),
    ("0 0 1 * *", "oleasante.cron.cron_periode_comptable"),  # Exécute à 00:00 le 1er de chaque mois
    # ('0 22 * * *', 'oleasante.cron.cron_compagnie'),
    # ('0 02 * * *', 'oleasante.cron.cron_client'), #ok
    # ('0 02 * * *', 'oleasante.cron.cron_police'), #ok
    # ('0 02 * * *', 'oleasante.cron.cron_formule'), #ok
    # ('0 03 * * *', 'oleasante.cron.cron_aliment'),
    ##('0 03 * * *', 'oleasante.cron.cron_specialite'),
    # ('0 04 * * *', 'oleasante.cron.cron_sinistre'),
    # ('0 05 * * *', 'oleasante.cron.cron_prestataire'),
    # ('0 05 * * *', 'oleasante.cron.cron_prescripteur'),
    ("0 22 * * *", "django.core.management.call_command", ["generateqrcode"]),
    # ('0 22 * * *', 'django.core.management.call_command', ['load_background_request_task']),
    # ('0 12 * * *', 'django.core.management.call_command', ['load_background_request_task']),
    ("0 04 * * *", "django.core.management.call_command", ["getphotosfromveos"]),
    ("0 04 * * *", "oleasante.cron.cron_vue_quittances"),
    (
        "*/30 * * * *",
        "oleasante.cron.cron_import_sinistre",
    ),  # Chaque jour 09h pour test
    (
        "0 10 * * *",
        "oleasante.cron.cron_get_clients_from_veos",
    ),  # Chaque jour 09h pour test
    # ('0 15 * * *', 'oleasante.cron.cron_get_clients_from_veos'),  # Chaque jour 09h pour test
]

# 1 minutes
# SESSION_EXPIRE_SECONDS = 30
# SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
# SESSION_TIMEOUT_REDIRECT = '/'
# SESSION_EXPIRE_AT_BROWSER_CLOSE = True

OTP_SECRET_KEY = "DHSEWPADGZSWQB6SQMCVWURWXAPHQGT6"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.office365.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "noreply.sante@olea.africa"
EMAIL_HOST_PASSWORD = "Rec7tteP@ss"
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_USE_TLS = True
EMAIL_HOST_NAME = "Noreply OLEA SANTE"

CORS_ORIGIN_ALLOW_ALL = True
