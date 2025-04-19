from django.urls import path

from . import views

app_name = 'conversation'

urlpatterns = [
    path('', views.inbox, name='inbox'), 
    path('<int:conversation_pk>/', views.conversation_detail, name="conversation_detail"), #conversation_pk
    path('new/<int:pk>/', views.new_conversation, name = 'new'), #item_pk

    ############### NEW CONTENT ###################################
    path('messages/', views.messages, name='messages'),
    path('messages/<int:pk>/', views.messages, name="message_detail"), #message_pk
    # path('conversations/', views.conversation_view, name='conversations'),
    # path('conversations/<int:conversation_id>', views.conversation_view, name='conversation-detail'),
]