import sys, os, site

cwd = os.getcwd()

INTERP = "/home/alon10/lbc.alanbeam.net/lbc_env/bin/python"
#INTERP = "/usr/bin/python"
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

sys.path.append(cwd)
sys.path.insert(0, cwd + '/longhornbrewing')

activate_env=os.path.join("/home/alon10/lbc.alanbeam.net/lbc_env/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

os.environ['DJANGO_SETTINGS_MODULE'] = "longhornbrewing.settings"
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

