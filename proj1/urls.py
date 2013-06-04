from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
      ('^say/', 'app1.views.say'),
      ('^result/', 'app1.views.result'),
      ('^history/', 'app1.views.history'),
      ('^status/', 'app1.views.status'),
      ('^login/', 'app1.views.mylogin'),
      ('^data/', 'app1.views.data'),
      ('^data.csv/', 'app1.views.data_csv'),
      #url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
