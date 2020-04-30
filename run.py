import logging
from render_engine.links import Link
from render_engine import Site, Page, Collection
from pathlib import Path

hfm_link = Link(
        "HouseKeeping & Facility Maintenance Programs",
        "/housekeeping_facility_maintenance",
    )

laundry_link = Link("Laundry Programs", "/laundry")
warewash_link = Link("Warewash Programs", "/warewash")

site = Site(strict=True)
site.SITE_URL = "https://wultra-hamilton-5d107b.netlify.com"
site.SITE_TITLE = "WAXIE ULTRA"

site.categories = [
    hfm_link,
    laundry_link,
    warewash_link,
]


class Products(Collection):
    template = "page.html"
    title = "Products"
    has_archive = True
    archive_slug = "all_products.html"
    archive_template = "all_products.html"

    @staticmethod
    def _archive_default_sort(cls):
        return (cls.category , cls.waxie_item_number)


site.register_collection(Products)


@site.register_route
class Index(Page):
    template = "index.html"


class HouseKeeping(Page):
    slug = "housekeeping_facility_maintenance"
    content_path = "content/pages/housekeeping_facility_maint.md"
    template = "all_products.html"

    def __init__(self):
        pages = [x for x in Products().pages if x.category == "housekeeping & facility maintenance"]
        self.pages = list(sorted(pages, key=lambda x: x.waxie_item_number))
        super().__init__()


class Laundry(Page):
    slug = "laundry"
    content_path = "content/pages/laundry.md"
    template = "all_products.html"

    def __init__(self):
        pages = [x for x in Products().pages if x.category == "laundry"]
        self.pages = list(sorted(pages, key=lambda x: x.waxie_item_number))
        super().__init__()


class Warewash(Page):
    slug = "warewash"
    content_path = "content/pages/warewash.md"
    template = "all_products.html"

    def __init__(self):
        pages = [x for x in Products().pages if x.category == "warewash"]
        self.pages = list(sorted(pages, key=lambda x: x.waxie_item_number))
        super().__init__()


site.route(HouseKeeping())
site.route(Warewash())
site.route(Laundry())

site.render()
