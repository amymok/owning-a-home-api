from django.conf.urls import patterns, url
from mortgageinsurance import views

urlpatterns = patterns(
    '',
    url(r'$', views.MortgageInsurance.as_view()),
)
