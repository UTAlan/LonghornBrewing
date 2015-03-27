SECRET_KEY = 'c+1h2fa6xfr@u^dtt)g(893tn%on^*35s3(a@zqx)+vh+3tz98'

DEBUG = False
TEMPLATE_DEBUG = False

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'longhornbrewing',
    'homepage',
    'beers',
    'eventspage',
    'happenings',
    'store',
    'contact',
    'findus',
    'pagestyle',
    'sociallinks',
    'copyright',
    'tinymce',
    'bgs',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.request',
    "longhornbrewing.context_processors.contact_info",
)

ROOT_URLCONF = 'longhornbrewing.urls'
WSGI_APPLICATION = 'longhornbrewing.wsgi.application'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Chicago'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# Happenings
CALENDAR_START_DAY = 6

# Copyright
COPY_START_YEAR = 2015

TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'plugins': "table",
    'valid_elements': "@[id|class|style|title|dir<ltr?rtl|lang|xml::lang|onclick|ondblclick|onmousedown|onmouseup|onmouseover|onmousemove|onmouseout|onkeypress|onkeydown|onkeyup],a[rel|rev|charset|hreflang|tabindex|accesskey|type|name|href|target|title|class|onfocus|onblur],strong/b,em/i,strike,u,#p,-ol[type|compact],-ul[type|compact],-li,br,img[longdesc|usemap|src|border|alt=|title|hspace|vspace|width|height|align],-sub,-sup,-blockquote,-table[border=0|cellspacing|cellpadding|width|frame|rules|height|align|summary|bgcolor|background|bordercolor],-tr[rowspan|width|height|align|valign|bgcolor|background|bordercolor],tbody,thead,tfoot,#td[colspan|rowspan|width|height|align|valign|bgcolor|background|bordercolor|scope],#th[colspan|rowspan|width|height|align|valign|scope],caption,-div,-span,-code,-pre,address,-h1,-h2,-h3,-h4,-h5,-h6,hr[size|noshade],-font[face|size|color],dd,dl,dt,cite,abbr,acronym,del[datetime|cite],ins[datetime|cite],object[classid|width|height|codebase|*],param[name|value|_value],embed[type|width|height|src|*],script[src|type],map[name],area[shape|coords|href|alt|target],bdo,button,col[align|char|charoff|span|valign|width],colgroup[align|char|charoff|span|valign|width],dfn,fieldset,form[action|accept|accept-charset|enctype|method],input[accept|alt|checked|disabled|maxlength|name|readonly|size|src|type|value],kbd,label[for],legend,noscript,optgroup[label|disabled],option[disabled|label|selected|value],q[cite],samp,select[disabled|multiple|name|size],small,textarea[cols|rows|disabled|name|readonly],tt,var,big,iframe[src|title|width|height|allowfullscreen|frameborder]",
    'theme_advanced_toolbar_location' : "top",
    'theme_advanced_buttons1': "removeformat,fontsizeselect,|,bold,italic,underline,|,forecolor,backcolor,|,bullist,numlist,hr,|,outdent,indent,|,justifyleft,justifycenter,justifyright,justifyfull,|,link,unlink,image,|,code",
    'theme_advanced_buttons2': "tablecontrols,table,row_props,cell_props,delete_col,delete_row,col_after,col_before,row_after,row_before,split_cells,merge_cells",
    'theme_advanced_buttons3': "",
}

try:
    from local_settings import *
except ImportError:
    pass
