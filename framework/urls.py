"""framework URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView as BaseGraphQLView
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


def test(request):
    return HttpResponse("Git is working")

class GraphQLView(BaseGraphQLView):

    @staticmethod
    def format_error(error):
        formatted_error = super(GraphQLView, GraphQLView).format_error(error)
        del formatted_error['locations']
        del formatted_error['path']
        try:
            formatted_error['context'] = error.original_error.context
        except AttributeError:
            pass

        return formatted_error

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('git_test/', test, name='git_test')
]
admin.site.site_header = 'i69'
admin.site.site_url = ''
admin.empty_value_display = '**Empty**'
admin.site.index_title = 'Admin Dashboard'
admin.site.site_title = 'i69'