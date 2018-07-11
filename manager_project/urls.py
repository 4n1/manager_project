"""manager_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import include, url
# 対象のページ遷移時に認証されていないとログインを要求する。
from django.contrib.auth.decorators import login_required

import manager.views as manager_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', manager_view.CustomLoginView.as_view()),
    path('logout/', manager_view.logout_view),
    # URLとViewを組み合わせる。
    path('worker_list/', login_required(manager_view.WorkerListView.as_view())),
    path('hijack/', include('hijack.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
