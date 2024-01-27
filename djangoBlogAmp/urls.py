from django.contrib import admin
from django.urls import path, include, re_path
from djangoBlogAmpApp.views import AdsView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from djangoBlogAmpApp.sitemaps import PostSitemap
from django.views.static import serve
from django.views.generic.base import TemplateView

sitemaps = {
    "posts": PostSitemap,
}

admin.site.site_url = ''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('djangoBlogAmpApp.urls')),
    # path('ads.txt', AdsView.as_view()),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path("ads.txt", TemplateView.as_view(template_name="ads.txt", content_type="text/plain")),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('summernote/', include('django_summernote.urls')),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
]

# handler404 = "djangoBlogAmpApp.views.page_not_found_view"

"""if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)"""