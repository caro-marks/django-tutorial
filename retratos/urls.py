from django.urls import path

from . import views

app_name = 'retratos'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),  # ex: /retratos/
    path('<int:pk>', views.DetailView.as_view(),
         name='detail'),  # ex: /retratos/5/
    path('<int:pk>/results/', views.ResultsView.as_view(),
         name='results'),  # ex: /retratos/5/results
    path('<int:question_id>/vote/', views.vote,
         name='vote'),  # ex: /retratos/5/vote
]
