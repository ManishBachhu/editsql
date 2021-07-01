from django.urls import path
from django.urls.conf import include
from .views import EditSQLView
from rest_framework.routers import DefaultRouter


#router = DefaultRouter()
#router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    path('sql/', EditSQLView.as_view())

]
