from django.urls import path
from . import views

urlpatterns = [
    #path('blog/', views.BlogPostListCreate.as_view(), name="blogpost-view-create")
    path('blog/', views.api_home)
]
