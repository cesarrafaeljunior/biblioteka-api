from .models import Loan, Copy
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from .serializers import LoanSerializer
from .permicions import IsCollaboratorOrReadOnly, IsColaborator
from users.models import User
from django.shortcuts import get_object_or_404
from datetime import date, timedelta
from rest_framework.exceptions import PermissionDenied, NotFound


class LoanView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCollaboratorOrReadOnly]

    serializer_class = LoanSerializer

    def get_queryset(self):
        return Loan.objects.filter(user=self.request.user.id)

    def perform_create(self, serializer):
        today = date.today()

        user = get_object_or_404(User, id=serializer.validated_data["user"].id)

        if user.is_blocked:
            raise PermissionDenied("This user is blocked")

        user_loans = Loan.objects.filter(
            user=serializer.validated_data["user"].id, is_receipt=False
        )

        for iten in user_loans:

            if iten.date_devolution < today:
                user.is_blocked = True

                user.save()

                raise PermissionDenied("This user is blocked")

        if user.unlock_date and user.unlock_date + timedelta(days=7) >= today:
            raise PermissionDenied("This user cannot lend a book yet")

        copy_obj = get_object_or_404(Copy, id=serializer.validated_data["copy"].id)

        if copy_obj.copies_avaliable <= 0:
            raise NotFound("Book unavailable")

        copy_obj.copies_avaliable -= 1

        copy_obj.save()

        serializer.save()


class LoanDetailView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsColaborator]

    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def perform_update(self, serializer):
        loan_obj = get_object_or_404(Loan, id=self.kwargs.get("pk"))

        if loan_obj.user.is_blocked:
            loan_obj.user.is_blocked = False
            loan_obj.user.unlock_date = date.today()

        loan_obj.is_receipt = True

        loan_obj.save()

        user_loans = Loan.objects.filter(user=loan_obj.user.id, is_receipt=False)

        for iten in user_loans:

            if iten.date_devolution < date.today():
                loan_obj.user.is_blocked = True
                loan_obj.user.unlock_date = None

                loan_obj.user.save()

        return loan_obj


class UserLoansView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsColaborator]

    serializer_class = LoanSerializer

    def get_queryset(self):
        return Loan.objects.filter(user=self.kwargs.get("pk"))
