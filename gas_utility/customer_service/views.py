

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from .models import ServiceRequest

# Function-based view for submitting a request
def submit_request(request):
    return render(request, "customer_service/submit_request.html")

# View for listing service requests
class ServiceRequestListView(LoginRequiredMixin, ListView):
    model = ServiceRequest
    template_name = 'customer_service/service_request_list.html'
    context_object_name = 'service_requests'

    def get_queryset(self):
        return ServiceRequest.objects.filter(customer=self.request.user).order_by('-created_at')

# View for detailed request view
class ServiceRequestDetailView(LoginRequiredMixin, DetailView):
    model = ServiceRequest
    template_name = 'customer_service/service_request_detail.html'
    context_object_name = 'service_request'

# View for submitting a service request
class ServiceRequestCreateView(LoginRequiredMixin, CreateView):
    model = ServiceRequest
    template_name = 'customer_service/submit_request.html'  
    fields = ['service_type', 'description', 'attachment']
    success_url = reverse_lazy('customer_service:service_request_list')  # Ensure correct namespace

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super().form_valid(form)

# Account info view
class AccountInfoView(LoginRequiredMixin, TemplateView):
    template_name = 'customer_service/account_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service_requests'] = ServiceRequest.objects.filter(customer=self.request.user)
        return context
