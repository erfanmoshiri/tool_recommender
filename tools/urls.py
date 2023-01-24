from django.urls import path

from tools.views.get_features_view import GetFeaturesView

urlpatterns = [

    # opinions
    path('features/', GetFeaturesView.as_view()),
]
