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
    pass


@site.register_route
class AllProducts(Page):
    template = "all_products.html"
    slug = "all_products"

    def __init__(self):
        super().__init__()
        self.title = "WAXIE ULTRA Products"
        self.products = site.collections["products"].pages


@site.register_route
class Warewashing(Page):
    template = "all_products.html"
    slug = "all_warewash"

    def __init__(self):
        super().__init__()
        self.title = "All Warewash Products"
        self.products = list(
            filter(
                lambda x: getattr(x, "category", "").lower() == "warewash",
                site.collections["products"].pages,
            )
        )


@site.register_route
class Laundry(Page):
    template = "all_products.html"
    slug = "all_laundry"

    def __init__(self):
        super().__init__()
        self.title = "All Laundry Products"
        self.products = list(
            filter(
                lambda x: getattr(x, "category", "").lower() == "laundry",
                site.collections["products"].pages,
            )
        )


@site.register_route
class HouseKeeping(Page):
    template = "all_products.html"
    slug = "all_housekeeping"

    def __init__(self):
        super().__init__()
        self.title = "All HouseKeeping Products"
        self.products = list(
            filter(
                lambda x: getattr(x, "category", "").lower() == "housekeeping",
                site.collections["products"].pages,
            )
        )

@site.register_route
class Index(Page):
    template = "index.html"

site.render()
