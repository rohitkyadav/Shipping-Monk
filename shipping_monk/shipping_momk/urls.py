from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'newsletter.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),
	url(r'^contact/$', 'newsletter.views.ContactUs', name='ContactUs'),
	url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hub/$','newsletter.views.hub',name="hub"),
    url(r'^search/$','newsletter.views.search',name="search"),
    url('^track/$','newsletter.views.track',name="track"),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)