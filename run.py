from render_engine.links import Link
from render_engine import Site, Page, Collection

site = Site(strict=True)
site.SITE_TITLE = "WAXIE ULTRA"
site.SITE_LINKS = [
    Link("Home", "/"),
    Link("HouseKeeping", "/housekeeping"),
    Link("Laundry", "/Laundry"),
    Link("Warewash", "/warewash"),
]


@site.register_collection
class products(Collection):
    pass


@site.register_route
class AllProducts(Page):
    template = "all_products.html"
    title = "WAXIE ULTRA Products"
    slug = "all_products"

    def __init__(self):
        super().__init__()
        self.products = site.collections["products"].pages


@site.register_route
class Warewashing(Page):
    template = "all_products.html"
    slug = "all_warewash"
    title = "All Warewash Products"

    def __init__(self):
        super().__init__()
        self.products = list(
            filter(
                lambda x: getattr(x, "category", "").lower() == "warewash",
                site.collections["products"].pages,
            )
        )


@site.register_route
class Index(Page):
    template = "index.html"

site.render()
