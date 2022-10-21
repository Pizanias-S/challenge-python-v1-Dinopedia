from django.urls import path

from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="index"),
    path("posts", views.AllPostsView.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="post-detail-page"),
    path("favorites", views.FavoritesView.as_view(), name="favorites"),
    path("search", views.SearchResultsView.as_view(), name="search-results"),
    path("favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("dinosaurs/img/favicon.ico")))
]
