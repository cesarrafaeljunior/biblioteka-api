from rest_framework.urls import path
from .views import LoanView, LoanDetailView, UserLoansView

urlpatterns = [
    path("loans/", LoanView.as_view()),
    path("loans/<int:pk>/", LoanDetailView.as_view()),
    path("user/loans/<int:pk>/", UserLoansView.as_view()),
]
