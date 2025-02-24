"""
URL configuration for gas_utility project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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


# from .views import home
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('service/', include('customer_service.urls')),
#       path('', home, name='home'),
    
# ]

# from django.contrib.auth import views as auth_views
 
# from .views import home, submit_request, track_request, account_info

# urlpatterns = [
#     path('', home, name='home'),
#     path('submit-request/', submit_request, name='submit_request'),
#     path('track-request/', track_request, name='track_request'),
#     path('account-info/', account_info, name='account_info'),

#     # Authentication URLs
#     path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
# ]



from django.contrib import admin
from django.urls import path,include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
   
     path('service/', include('customer_service.urls', namespace='customer_service')),
]
