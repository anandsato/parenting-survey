from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'surveys.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'submissions.views.profile', name='profile'),
    url(r'^thank-you/$', 'submissions.views.thank_you', name='thank_you'),
    url(r'^results/$', 'submissions.views.results', name='results'),
)
