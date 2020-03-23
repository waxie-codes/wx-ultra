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

class Products(Collection):
    template = 'all_products.html'
    title = 'Products'

site.register_collection(Products)

@site.register_route
class Index(Page):
    template = "index.html"

@site.register_route
class HouseKeeping(Page):
    slug = 'all_housekeeping'
    content_path = "content/pages/housekeeping.html"
    template = 'all_products.html'
    products = [x for x in Products().pages if x.category == 'housekeeping']

@site.register_route
class Laundry(Page):
    slug = 'all_laundry'
    content_path = "content/pages/Laundry.html"
    template = 'all_products.html'
    products = [x for x in Products().pages if x.category == 'laundry']

@site.register_route
class Warewash(Page):
    slug = 'all_warewash'
    content_path = "content/pages/warewash.html"
    template = 'all_products.html'
    products = [x for x in Products().pages if x.category == 'warewash']
site.render()
