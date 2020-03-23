from render_engine.links import Link
from render_engine import Site, Page, Collection

class Products(Collection):
    has_archive = True
    template = "page.html"
    _archive_template = "all_products.html"
    _archive_slug = 'all_products.html'
    subcollections = ['category']

    @staticmethod
    def _archive_default_sort(cls):
        return cls.category

