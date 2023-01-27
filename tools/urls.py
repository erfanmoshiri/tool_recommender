from django.urls import path

from tools.views import FindToolView, GetFeaturesView

urlpatterns = [

    # opinions
    path('features/', GetFeaturesView.as_view()),
    path('find/', FindToolView.as_view()),
]
