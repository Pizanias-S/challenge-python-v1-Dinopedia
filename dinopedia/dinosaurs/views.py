from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import ListView
from .models import Dino
from django.db.models import Q
from .forms import CommentForm
from django.urls import reverse

# Create your views here.


class StartingPageView(View):
    def get(self, request):
        return render(request, "dinosaurs/index.html")


class AllPostsView(ListView):
    template_name = "dinosaurs/all-posts.html"
    model = Dino
    ordering = ["-name"]
    context_object_name = "all_posts"


class SinglePostView(View):
    def is_favorite_post(self, request, post_id):
        favorite_posts = request.session.get("favorite_posts")
        if favorite_posts is not None:
            is_favorite = post_id in favorite_posts
        else:
            is_favorite = False
        return is_favorite

    def get(self, request, slug):
        post = Dino.objects.get(slug=slug)
        context = {
            "post": post,
            "favorite": self.is_favorite_post(request, post.id),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id")
        }
        return render(request, "dinosaurs/post-detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Dino.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
        else:
            context = {
                "post": post,
                "favorite": self.is_favorite_post(request, post.id),
                "comment_form": CommentForm(),
                "comments": post.comments.all().order_by("-id")
            }
        return render(request, "dinosaurs/post-detail.html", context)


class FavoritesView(View):
    def get(self, request):
        favorite_posts = request.session.get("favorite_posts")
        context = {}

        if favorite_posts is None or len(favorite_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Dino.objects.filter(id__in=favorite_posts)
            context["posts"] = posts
            context["has_posts"] = True
        return render(request, "dinosaurs/favorite-posts.html", context)

    def post(self, request):
        favorite_posts = request.session.get("favorite_posts")

        if favorite_posts is None:
            favorite_posts = []
        post_id = int(request.POST["post_id"])

        if post_id not in favorite_posts:
            favorite_posts.append(post_id)
        else:
            favorite_posts.remove(post_id)

        request.session["favorite_posts"] = favorite_posts
        return HttpResponseRedirect("/posts")


class SearchResultsView(ListView):
    model = Dino
    template_name = "dinosaurs/search-results.html"
    context_object_name = "search_results"

    def get_queryset(self):
        search_query = self.request.GET.get("search_dino")
        search_query_result = Dino.objects.filter(Q(name__icontains=search_query))
        if str(search_query_result) == "<QuerySet []>":
            search_query_result = ""
        return search_query_result

