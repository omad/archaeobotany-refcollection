from django.conf.urls import patterns, include, url
from admin_custom import botany_admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'archaeobotany.views.home', name='home'),
    # url(r'^archaeobotany/', include('archaeobotany.foo.urls')),

    url('', include('apps.botanycollection.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include(botany_admin.urls)),
)
