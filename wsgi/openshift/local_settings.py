__author__ = 'Q'
# SECURITY WARNING: keep the secret key used in production secret!
import imp
import os


ON_OPENSHIFT = False
if 'OPENSHIFT_REPO_DIR' in os.environ:
    ON_OPENSHIFT = True

default_keys = { 'SECRET_KEY': 'tjy&7h%c=q01+c5i@_-t)&n2c+y*tn7v_)vbdksnlv@s5qh%e_' }
use_keys = default_keys
if ON_OPENSHIFT:
    imp.find_module('openshiftlibs')
    import openshiftlibs
    use_keys = openshiftlibs.openshift_secure(default_keys)

SECRET_KEY = use_keys['SECRET_KEY']