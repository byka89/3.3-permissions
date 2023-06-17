from django_filters import rest_framework as filters, DateFromToRangeFilter, AllValuesFilter

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    created_at = DateFromToRangeFilter()
    creator = AllValuesFilter(field_name='creator_id')
    status = AllValuesFilter(field_name='status')
    print('Фильтр')

    class Meta:
        print('Мета Фильтр')
        model = Advertisement
        fields = ['created_at', 'creator', 'status']