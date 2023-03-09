from rest_framework import pagination


class SmallPagination(pagination.PageNumberPagination):
    page_size = 2


class LargePagination(pagination.PageNumberPagination):
    page_size = 5
