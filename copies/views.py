from rest_framework.views import Request, Response, status
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permitions import IsAdmAuthentication
from .models import Copy
from .serializers import CopySerializer
from django.shortcuts import get_object_or_404
from books.models import Book


class CopyCreatelView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdmAuthentication]

    queryset = Copy.objects.all()
    serializer_class = CopySerializer

    def perform_create(self, serializer):
        book = self.request.data.pop("book")
        book_obj = get_object_or_404(Book, id=book)

        serializer.save(book=book_obj)


class CopyDateilView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdmAuthentication]

    lookup_url_kwarg = "copy_id"

    queryset = Copy.objects.all()
    serializer_class = CopySerializer
