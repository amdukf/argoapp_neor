from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .feeds import LatestPostsFeed

urlpatterns = [
    path('amp/', views.PostListAmp.as_view(), name='blog_amp'),
    path('amp/<slug:slug>/', views.post_detail_amp, name='post_detail_amp'),
    path('', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path("feed/rss", LatestPostsFeed(), name="post_feed")
    
]

"""if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)"""