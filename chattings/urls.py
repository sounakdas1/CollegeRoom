# chat/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from usersauthentications import views as v
urlpatterns = [
    path('chat_new/<slug:slug>/', views.topic_list, name='topic_list'),   
    path('chat_page/<slug:slug>/<slug:topic_slug>/',views.start_chat, name='start_chat'), 
    path('topic_page/<slug:slug>/', views.start_topic, name='start_topic'),
    path('<int:chat_id>/edit/<slug:slug>/<slug:topic_slug>/', views.edit_chat, name='edit_chat'),
    path('<int:chat_id>/delete/<slug:slug>/<slug:topic_slug>/', views.delete_chat, name='delete_chat'),
    path('<int:chat_id>/reply/<slug:slug>/<slug:topic_slug>/', views.reply_chat, name='reply_chat'),
    path('<int:chat_id>/image/<slug:slug>/<slug:topic_slug>/', views.imagepage, name='image_chat'),
    path('chatting_list/<slug:slug>/<slug:topic_slug>/', views.chat_list, name='chatting_list'), 
    path('<int:chat_id>/replies/<slug:slug>/<slug:topic_slug>/', views.replies_list,name='reply_list'),
    path('',v.home,name='homes')
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)