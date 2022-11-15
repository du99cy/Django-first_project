from rest_framework import filters

class RecordIsActiveFilterBackend(filters.BaseFilterBackend):
    
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(is_active=1)
    