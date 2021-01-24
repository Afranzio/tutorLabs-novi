
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
 path('api/messages/<int:sender>/<int:receiver>/<int:idst>/<int:viewss>' , views.message_list  , name="message-details"),  #for viewig messages
 path('api/messages' , views.message_list , name='message-list'),  #for adding messages 
 path('api/users/<int:pk>' ,  views.user_list , name = 'user-details'),
 path('api/users', views.user_list, name='user-list') ,
 path('chat', views.chat_view, name='chats'),
#  path('register', views.register_view, name='register'),
 path('getApi', views.api, name='api'),
 path('show_invitations', views.show_invitations, name='show_invitations'),
 path('myTutors', views.myTutors, name='myTutors'),
 path('myclasses', views.myclass, name='myClasses'),
 path('approve_tutorForm/<int:sender>', views.approve_tutorForm, name='approve_tutorForm'),
 path('create_class', views.create_class, name='create_class'),
 path('invite_tutorForm', views.invite_tutorForm, name='invite_tutorForm'),
 path('invite_tutor', views.invite_tutor, name='invite_tutor'),
 path('list_tutor', views.list_tutor, name='list_tutor'),
 path('class_form', views.class_form, name="class_form"),
 path('getApi/<int:sender>', views.specified, name='specified'),
 path('api/messages/<int:sender>/<int:receiver>', views.message_list, name='message-detail'),
 ]
