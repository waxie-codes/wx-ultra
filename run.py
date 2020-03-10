from render_engine.links import Link
from render_engine import Site, Page, Collection

site = Site(strict=True)
site.SITE_TITLE = "WAXIE ULTRA"
site.SITE_LINKS = [
        Link('Home', '/'),
        Link('HouseKeeping', '/housekeeping'),
        Link('Laundry', '/Laundry'),
        Link('Warewash', '/warewash'),
        ]

@site.register_collection
class products(Collection):
    pass

@site.register_route
class Index(Page):
    template = 'index.html'

    def __init__(self):
        super().__init__()
        self.products= site.collections['products'].pages


site.render()
