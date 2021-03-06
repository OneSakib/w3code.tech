from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'Web'

urlpatterns = [
    path('html/', views.HtmlView.as_view(), name='html'),
    path('html/<slug>/', views.HTMLDetailView.as_view(), name='htmldetail'),
    path('css/', views.CSSView.as_view(), name='css'),
    path('css/<slug>/', views.CSSDetailView.as_view(), name='cssdetail'),
    path('laravel/', views.LaravelView.as_view(), name='laravel'),
    path('laravel/<slug>/', views.LaravelDetailView.as_view(), name='laraveldetail'),
    path('wordpress/', views.WordpressView.as_view(), name='wordpress'),
    path('wordpress/<slug>/', views.WordpressDetailView.as_view(), name='wordpressdetail'),
    path('json/', views.JSONView.as_view(), name='json'),
    path('json/<slug>/', views.JSONDetailView.as_view(), name='jsondetail'),
    path('ajax/', views.AJAXView.as_view(), name='ajax'),
    path('ajax/<slug>/', views.AJAXDetailView.as_view(), name='ajaxdetail'),
    path('bootstrap/', views.BootstrapView.as_view(), name='bootstrap'),
    path('bootstrap/<slug>/', views.BootstrapDetailView.as_view(), name='bootstrapdetail'),
]
