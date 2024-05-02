from django.urls import path
from .views import AiHelp

app_name = 'aihelp'

url_patterns = [
    path("aihelp/", AiHelp.as_view(), name="aihelp"),
]