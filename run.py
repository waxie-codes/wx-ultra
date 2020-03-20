from render_engine.links import Link
from render_engine import Site, Page, Collection

site = Site(strict=True)
site.SITE_URL = "https://wultra-hamilton-5d107b.netlify.com"
site.SITE_TITLE = "WAXIE ULTRA"
site.SITE_LINKS = [
    Link("Home", "/"),
    Link("HouseKeeping", "/all_housekeeping"),
    Link("Laundry", "/all_laundry"),
    Link("Warewash", "/all_warewash"),
]
site.categories = ['', 'Warewash', 'Laundry', 'HouseKeeping']

@site.register_collection
class products(Collection):
    has_archive = True
    template = "page.html"
    _archive_template = "all_products.html"
    subcollections = ['category']


@site.register_route
class Index(Page):
    template = "index.html"

site.render()
