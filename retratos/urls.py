from django.urls import path

from . import views

app_name = 'retratos'
urlpatterns = [
    path('', views.index, name='index'),  # ex: /retratos/
    path('<int:question_id>', views.detail, name='detail'),  # ex: /retratos/5/
    path('<int:question_id>/results/', views.results,
         name='results'),  # ex: /retratos/5/results
    path('<int:question_id>/vote/', views.vote,
         name='vote'),  # ex: /retratos/5/vote
]
