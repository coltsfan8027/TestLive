from django.urls import path
from . import views


app_name = 'mainpage'
urlpatterns = [
    path('services/', views.ServiceListView.as_view(), name='service_list'),
    path('services/<pk>/', views.ServiceDetailView.as_view(), name='service_detail'),
    path('certificates/', views.CertificateListView.as_view(), name='certificate_list'),
    path('certificate/<pk>/', views.CertificateDetailView.as_view(), name='certificate_detail'),
    path('product/', views.ProductListView.as_view(), name='product_list'),
    path('product/<pk>/', views.ProductDetailView.as_view(), name='product_detail')
]