from django.urls import path

from .views import DeleteProductView, DetailApiView, ListCreateProductView, ListProductView, ProductMixinsViews, UpdateProductView, api_view



urlpatterns = [
    path('',api_view,name="api_view"),
    path('<int:pk>/',DetailApiView.as_view()),
    path('<int:pk>/update',UpdateProductView.as_view()),
    path('<int:pk>/delete',DeleteProductView.as_view()),
    path('list/',ListProductView.as_view()),
    path('create-list/',ListCreateProductView.as_view()),
    path('<int:pk>/detail',ProductMixinsViews.as_view()),
    path('<int:pk>/update',ProductMixinsViews.as_view()),
    path('list/',ProductMixinsViews.as_view())
]
