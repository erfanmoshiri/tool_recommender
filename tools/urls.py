from django.urls import path

from tools.views import FindToolView, GetFeaturesView, GetToolsView, GetToolView, RegisterUser, LoginUser, RateToolView, \
    GetRecommendView, VerifyCode

urlpatterns = [

    # opinions
    path('features/', GetFeaturesView.as_view()),
    path('find/', FindToolView.as_view()),

    path('', GetToolsView.as_view()),
    path('<int:pk>/', GetToolView.as_view()),
    path('recommends/', GetRecommendView.as_view()),

    path('rate/<int:pk>/', RateToolView.as_view()),

    path('register/', RegisterUser.as_view()),
    path('login/', LoginUser.as_view()),
    path('verify/', VerifyCode.as_view()),

]
