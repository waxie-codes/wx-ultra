import logging
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
    template = 'page.html'
    title = 'Products'
    has_archive = True
    _archive_slug = 'all_products.html'
    _archive_template = 'all_products.html'

site.register_collection(Products)

@site.register_route
class Index(Page):
    template = "index.html"


class HouseKeeping(Page):
    slug = 'all_housekeeping'
    content_path = "content/pages/housekeeping.md"
    template = 'all_products.html'

    def __init__(self):
        self.pages = [x for x in Products().pages if x.category ==
                'housekeeping']
        super().__init__()

class Laundry(Page):
    slug = 'all_laundry'
    content_path = "content/pages/Laundry.md"
    template = 'all_products.html'

    def __init__(self):
        self.pages = [x for x in Products().pages if x.category == 'laundry']
        super().__init__()



class Warewash(Page):
    slug = 'all_warewash'
    content_path = "content/pages/warewash.md"
    template = 'all_products.html'

    def __init__(self):
        self.pages = [x for x in Products().pages if x.category == 'warewash']
        super().__init__()


site.route(HouseKeeping())
site.route(Warewash())
site.route(Laundry())

site.render()
