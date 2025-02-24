

# from django.urls import path
# from .views import ServiceRequestListView, ServiceRequestDetailView, ServiceRequestCreateView

# urlpatterns = [
#     path('requests/', ServiceRequestListView.as_view(), name='service_request_list'),
#     path('requests/<int:pk>/', ServiceRequestDetailView.as_view(), name='service_request_detail'),
#     path('requests/new/', ServiceRequestCreateView.as_view(), name='service_request_create'),
# ]

from django.urls import path
from .views import ServiceRequestCreateView, ServiceRequestListView, ServiceRequestDetailView, submit_request, AccountInfoView

app_name = "customer_service" 
urlpatterns = [
    path('submit-request/', ServiceRequestCreateView.as_view(), name='submit_request'),
    path('requests/', ServiceRequestListView.as_view(), name='service_request_list'),
    path('requests/<int:pk>/', ServiceRequestDetailView.as_view(), name='service_request_detail'),
     path('track-request/', ServiceRequestListView.as_view(), name='track_request'),
    path('account-info/', AccountInfoView.as_view(), name='account_info'),
]



