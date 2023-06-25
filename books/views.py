from rest_framework import viewsets, permissions
from .serializers import FilterSerializer, BooksSerializer
from rest_framework.pagination import PageNumberPagination
from .services import get_books
from drf_yasg.utils import swagger_auto_schema


class BookViewSet(viewsets.ViewSet):
    """
    API endpoint that allows list of books to be viewed.
    """

    page_size = 25
    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(
        query_serializer=FilterSerializer,
        responses={"200": BooksSerializer, "400": "Bad Request"},
    )
    def list(self, request):
        filters = FilterSerializer(data=request.query_params)
        filters.is_valid(raise_exception=True)
        queryset = get_books(**filters.validated_data)
        paginator = PageNumberPagination()
        paginator.page_size = self.page_size
        result_page = paginator.paginate_queryset(queryset, request)
        # serializer = OutputSerializer(result_page, many=True)
        serializer = BooksSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
