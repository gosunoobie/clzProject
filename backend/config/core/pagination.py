
from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = "page_size"
    max_page_size = 10000

    def paginate_queryset(self, queryset, request, view):
        actual_page_size = request.query_params.get(self.page_size_query_param, None)
        if actual_page_size and (str(actual_page_size) in ["0", "none"]):
            self.page_size = queryset.count()
        
        return super().paginate_queryset(queryset, request, view)

    def get_paginated_response(self, data):
        total_page = self.page.paginator.num_pages
        # page_num = int(self.request.query_params.get("page"))
        # if page_num > total_page:
        #     print("greater than page")
        #     data = []
        actual_page_size = self.request.query_params.get(
            self.page_size_query_param, None
        )
        if actual_page_size and str(actual_page_size).lower() == "none":
            return Response(data)
        return Response(
            OrderedDict(
                [
                    ("next", self.get_next_link()),
                    ("previous", self.get_previous_link()),
                    ("current_page", self.page.number),
                    ("page_size", self.get_page_size(self.request)),
                    ("total_pages",total_page),
                    ("total_objects", self.page.paginator.count),
                    ("results", data),
                ]
            )
        )

    def get_paginated_response_schema(self, schema):
        return {
            "type": "object",
            "properties": {
                "count": {
                    "type": "integer",
                    "example": 123,
                },
                "next": {
                    "type": "string",
                    "nullable": True,
                    "format": "uri",
                    "example": "http://api.example.org/accounts/?{page_query_param}=4".format(
                        page_query_param=self.page_query_param
                    ),
                },
                "previous": {
                    "type": "string",
                    "nullable": True,
                    "format": "uri",
                    "example": "http://api.example.org/accounts/?{page_query_param}=2".format(
                        page_query_param=self.page_query_param
                    ),
                },
                "current_page": {
                    "type": "integer",
                    "description": "Current page number",
                    "example": 1,
                },
                "page_size": {
                    "type": "integer",
                    "description": "Number of objects in a page",
                    "example": 10,
                },
                "total_pages": {
                    "type": "integer",
                    "description": "Total number of pages",
                    "example": 100,
                },
                "total_objects": {
                    "type": "integer",
                    "description": "Total number of objects across all pages",
                    "example": 1000,
                },
                "results": schema,
            },
        }
