"""bug_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from homepage import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('login/', views.login_view, name="login"),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name="logout"),
    path('addticket/', views.add_ticket, name="addticket"),
    path('ticket/<int:ticket_id>/edit/', views.ticket_edit_view),
    path('ticket/<int:ticket_id>/assign/', views.assign_ticket),
    path('ticket/<int:ticket_id>/done/', views.set_status_done),
    path('ticket/<int:ticket_id>/invalid/', views.set_status_invalid),
    path('ticket/<int:ticket_id>/', views.ticket, name="ticket"),
    path('user/<int:user_id>/', views.user),
    path('admin/', admin.site.urls),
]
