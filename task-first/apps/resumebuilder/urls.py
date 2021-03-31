from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import RedirectView

from ..resume import views as views
from ..user import views as user_views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path(r'', RedirectView.as_view(pattern_name='resume')),



    path(r'resume/', views.resume_view, name='resume'),
    # path('download_resume_pdf/<int:resume_item_id>/', views.resume_download_view, name="download_resume_pdf"),
    path(r'resume/item/edit/<int:resume_item_id>/', views.resume_edit_view, name='resume-item-edit'),
    path(r'resume/item/create/', views.resume_create_view, name='resume-item-create'),

    path(r'user/', user_views.account_edit_view, name='account-edit'),
    path(r'create-account/', user_views.account_create_view, name='account-create'),
   
    path('', views.CustomerListView, name='as_view'),
    # path('pdf/', views.render_pdf_view), 
    path('pdf/<int:resume_item_id>/', views.resume_render_pdf_view, name='employee_render_pdf_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

