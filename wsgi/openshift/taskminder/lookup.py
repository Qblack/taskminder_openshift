__author__ = 'Q'

from selectable.base import ModelLookup
from selectable.registry import registry

from taskminder.models import Course, Country, Province, University

class ProvinceLookup(ModelLookup):
    model = Province
    search_fields = ('country__icontains', )

    def get_query(self, request, term):
        results = super(ProvinceLookup, self).get_query(request, term)
        country = request.GET.get('country', '')
        if country:
            results = results.filter(country=country)
        return results

    def get_item_label(self, item):
        return u"%s, %s" % (item.name, item.country)


registry.register(ProvinceLookup)


