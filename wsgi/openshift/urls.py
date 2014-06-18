from django.conf.urls import patterns, include, url

from django.contrib import admin

from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'views.home', name='home'),
    # url(r'^$', 'openshift.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^load/','views.load'),
    url(r'^login/','taskminder.views.login_view'),
    url(r'^register/','taskminder.views.register'),
    url(r'^thanks/','taskminder.views.thanks'),
    url(r'^assignments/', 'taskminder.views.show_assignments'),
    url(r'^course_add/', 'taskminder.views.course_add_view'),
)
