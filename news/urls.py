from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>', get_category, name='category'),
    path('news/<int:pk>', ViewNews.as_view(), name='view_news'),
    # path('add-news', add_news, name='add_news'),
    path('add-news', CreateNews.as_view(), name='add_news'),

]