from django.urls import path

from tools.views import FindToolView, GetFeaturesView, GetToolsView, GetToolView, RegisterUser, LoginUser

urlpatterns = [

    # opinions
    path('features/', GetFeaturesView.as_view()),
    path('find/', FindToolView.as_view()),

    path('', GetToolsView.as_view()),
    path('<int:pk>/', GetToolView.as_view()),

    path('register/', RegisterUser.as_view()),
    path('login/', LoginUser.as_view()),

]
