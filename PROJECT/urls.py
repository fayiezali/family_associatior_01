"""PROJECT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path , include
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from home import  views
from django.contrib.auth.models import User
#
from accounts.models import * #  استيراد كل المودل/الجداول من التطبيق المطلوب
#
# Aplications OTP
from django_otp.admin import OTPAdminSite
from django_otp.plugins.otp_totp.models import TOTPDevice
#
#
#
urlpatterns = [
    # path('admin/'            , admin.urls),
    path('admin/'            , admin.site.urls),
]
#
# Path App sms
# urlpatterns += [
#     path('sms/', include('sms.urls')), # This Path I was Created From My App
# ]
# Path App Accounts
urlpatterns += [
    path('accounts/', include('accounts.urls')), # This Path I was Created From My App
]
#
# Path App Public_Pages 
urlpatterns += [
    path(''          , views.IndexPage.as_view(),   name='index_pageURL'),
    path('about/'    , views.AboutPage.as_view(),   name='about_pageURL'),
    path('contact/'  , views.ContactPage.as_view(), name='contact_pageURL'),
    
] 
#
#
#
#
if settings.DEBUG is True:
    # (13) Step:----->(14) Step:-----> base.html
    # لكي يستطيع المشروع الوصول إليها"static" تعريف ملفات مجلد 
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # (25) Step:----->(26) Step:-----> account/templates/user/show_user_profile_list.html
    # لكي يستطيع المشروع الوصول إليها"media" تعريف ملفات مجلد 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)