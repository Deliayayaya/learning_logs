from django.urls import path
from django.urls import re_path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('topics/', views.topics, name ="topics"),
    # re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic')
    path('topics/<int:topic_id>/',views.topic,name="topic"),
    path('topics/new_topic/',views.new_topic,name="new_topic"),
    path('new_entry/<int:topic_id>/',views.new_entry,name="new_entry"),
    path('edit_entry/<int:entry_id>/',views.edit_entry,name="edit_entry")
]
