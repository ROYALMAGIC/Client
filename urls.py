from django.urls import path
from . import views

urlpatterns = [
    path('',views.ClientHome,),
    path('Profile/',views.ClientProfile,),
    path('Projectlist/',views.ClientProjectlist,),  
    path('Ticketlist/',views.ClientTicketlist,),
    path('Feedback/',views.ClientFeedback,),
    path('History/',views.ClientHistory,),
]    

