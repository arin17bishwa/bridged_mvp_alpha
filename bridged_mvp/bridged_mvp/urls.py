"""bridged_mvp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import loader_io, home
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('loaderio-39cf266dd5a723050b3f3fa395391151/', loader_io, name='loader_io'),
    path('', home, name='home'),
    path('events/', include('events.urls'), name='events'),
    path('students/', include('students.urls'), name='students'),
    path('contents/', include('contents.urls'), name='contents'),

    #  region API Doc
    path('docs/', include_docs_urls(title='Bridged MVP')),
    path('schema/', get_schema_view(
        title="Bridged MVP",
        description="API for the brigades",
        version="0.1.0"
    ), name='openapi-schema'),
    #  endregion

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
