import logging
from render_engine.links import Link
from render_engine.search import Fuse
from render_engine import Site, Page, Collection
from pathlib import Path

hfm_link = Link(
        "HouseKeeping & Facility Maintenance",
        "/housekeeping_facility_maintenance",
    )

laundry_link = Link("Laundry", "/laundry")
warewash_link = Link("Warewash", "/warewash")

site = Site()
site.strict=True
site.SITE_URL = "https://wultra-hamilton-5d107b.netlify.com"
site.SITE_TITLE = "WAXIE ULTRA"
site.search = Fuse
site.output_path = 'docs'

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
    content_path = 'content'
    subcollections = ['category']

    @staticmethod
    def archive_default_sort(cls):
        return (cls.category , cls.waxie_item_number)



site.register_collection(Products)

@site.register_route
class Index(Page):
    template = "index.html"
    no_index = True


class HouseKeeping(Page):
    slug = "housekeeping_facility_maintenance"
    content_path = "content/pages/housekeeping_facility_maint.md"
    template = "all_products.html"

class Laundry(Page):
    slug = "laundry"
    content_path = "content/pages/laundry.md"
    template = "all_products.html"

class Warewash(Page):
    slug = "warewash"
    content_path = "content/pages/warewash.md"
    template = "all_products.html"

site.route(HouseKeeping())
site.route(Warewash())
site.route(Laundry())

site.render()
