class Account:
    public_key: str     # Account public key
    published: list     # Releases published by this Account
    collected: list     # Releases collected by this Account
    exchanges: list     # Exchange this Account has has initialized or completed
    hubs: list          # Hubs this Account is a Collaborator on
    posts: list         # Posts this Account has made
    revenue_shares: list    # Releases that this Account has a revenueShare on

    def __init__(self, json_data, publicKey=None):
        self.public_key = publicKey
        self.published = [Release(release) for release in json_data["published"]] 
        self.collected = [Release(release) for release in json_data["collected"]]
        self.exchanges = [Exchange(exchange) for exchange in json_data["exchanges"]]
        self.hubs = [Hub(hub) for hub in json_data["hubs"]]
        self.posts = [Post(post) for post in json_data["posts"]]
        self.revenue_shares = [Release(release) for release in json_data["revenueShares"]]

class File:
    uri: str            # Link to Audio file on Arweave
    track: int          # Track Listing
    track_title: str    # Track Title
    duration: int       # Track Duration in Seconds
    type: str           # File Type

    def __init__(self, json_data):
        self.uri = json_data["uri"]
        self.track = json_data["track"]
        self.track_title = json_data["track_title"]
        self.duration = json_data["duration"] if "duration" in json_data else 0
        self.type = json_data["type"]

class Metadata: 
    name: str           # Artist - Title
    symbol: str         # Token Name
    description: str    # Release Description
    image: str          # Link to Release Image on Arweave
    animation_url: str  # Link to Audio File on Arweave
    external_url: str   # Link to Release on Ninaprotocol.com
    attributes: str     # Array of arrays ?
    collection_name: str # Artist - Title
    collection_family: str # Nina
    artist: str         # Artist Name
    title: str          # Track Name
    date: str           # Release Date
    md5Digest: str      # Hash of Audio File
    files: list         # Array of File objects
    category: str       # File Type
    description_html: str   # Release Description (with Markup)

    def __init__(self, json_data):
        self.name = json_data["name"]
        self.symbol = json_data["symbol"]
        self.description = json_data["description"]
        self.image = json_data["image"]
        self.animation_url = json_data["animation_url"]
        self.external_url = json_data["external_url"]
        self.attributes = json_data["attributes"]
        self.collection_name = json_data["collection"]["name"]
        self.collection_family = json_data["collection"]["family"]
        self.artist = json_data["properties"]["artist"]
        self.title = json_data["properties"]["title"]
        self.date = json_data["properties"]["date"]
        self.md5Digest = json_data["properties"]["md5Digest"] if "md5Digest" in json_data["properties"] else ""
        self.files = [File(file) for file in json_data["properties"]["files"]]
        self.category = json_data["properties"]["category"]
        self.description_html = json_data["descriptionHtml"] if "descriptionHtml" in json_data else ""

class Release:
    public_key: str     # Release public key
    mint: str           # Mint public key
    metadata: Metadata  # Metadata object
    datetime: str       # Release Date
    published_through_hub: str  # publicKey of the Hub the Release was publsihed thrtough
    publisher: str      # publicKey of Publisher's Account

    def __init__(self, json_data):
        self.public_key = json_data["publicKey"]
        self.mint = json_data["mint"]
        self.metadata = Metadata(json_data["metadata"])
        self.datetime = json_data["datetime"]
        self.published_through_hub = json_data["publishedThroughHub"] if "publishedThroughHub" in json_data else ""
        self.publisher = json_data["publisher"]


class Exchange: 
    public_key: str     # The publicKey of the Exchange
    is_sale: bool       # Describes whether the exchange is a sale (if false the Exchange is a Buy Offer)
    expected_amount: str    # If isSale is true, this is the amount of USDC expected to be received by the seller. If isSale is false, this is the amount of Releases expected to be received by the buyer (always = 1)
    initalizer_amount: str  # If isSale is true, this is the amount of Releases to be sold to the buyer (always = 1). If isSale is false, this is the amount of USDC being offered to purchase the Release
    cancelled: bool         # Describes whether the Exchange has been cancelled or not 
    created_at: str     # The datetime the Exchange was created
    updated_at: str     # The datetime the Exchange was last updated (Exchanges are updated when they are cancelled or completed)
    completed_by: str   # The publicKey of the Account that completed the Exchange
    release: str        # The publicKey of the Release associated with the Exchange
    initializer: str    # The publicKey of the Account that initialized the Exchange.

    def __init__(self, json_data):
        self.public_key = json_data["publicKey"]
        self.is_sale = json_data["isSale"]
        self.expected_amount = json_data["expectedAmount"]
        self.initalizer_amount = json_data["initializerAmount"]
        self.cancelled = json_data["cancelled"]
        self.created_at = json_data["createdAt"]
        self.updated_at = json_data["updatedAt"]
        self.completed_by = json_data["completedBy"] if "completedBy" in json_data else ""
        self.release = json_data["release"]
        self.initializer = json_data["initializer"]

class Hub:
    public_key: str     # The Hub publicKey
    handle: str         # the Hub's handle (must be unique)
    display_name: str   # The Hub's display name
    description: str    # the Hub's description
    external_url: str   # The Hub's external URL
    image: str          # The Hub's image
    description_html: str   # The Hub's description in with HTML (user's Rich Text formatting)
    datetime: str       # The time the Hub was created
    authority: str      # The Public Key of the Account that created the Hub

    def __init__(self, json_data):
        self.public_key = json_data["publicKey"]
        self.handle = json_data["handle"]
        self.display_name = json_data["data"]["displayName"]
        self.description = json_data["data"]["description"]
        self.external_url = json_data["data"]["externalUrl"]
        self.image = json_data["data"]["image"]
        self.description_html = json_data["data"]["descriptionHtml"] if "descriptionHtml" in json_data["data"] else ""
        self.datetime = json_data["datetime"]
        self.authority = json_data["authority"] 

class HubData:
    hub: Hub            # Hub object
    collaborators: list # list of privatekeys and hubCollaboratorPublicKeys
    releases: list      # Array of objects (Release)
    posts: list         # Array of objects (Post)

    def __init__(self, json_data): 
        self.hub = Hub(json_data["hub"])
        self.collaborators = []

class Post:
    public_key: str     # The Post's publicKey
    title: str          # The Post's title
    body: str           # The Post's body
    body_html: str      # The Post's body with HTML (user's Rich Text formatting)
    reference: str      # A Reference to a Release associated with the Post
    datetime: str       # The time the post was published
    publisher: str      # publicKey of the Account that published the Post
    published_through: str  # publicKey of the Hub the Post was published through

    def __init__ (self, json_data):
        self.public_key = json_data["publicKey"]
        self.title = json_data["data"]["title"]
        self.body = json_data["data"]["body"]
        self.body_html = json_data["data"]["bodyHtml"]
        self.reference = json_data["data"]["reference"] if "reference" in json_data["data"] else ""
        self.datetime = json_data["datetime"]
        self.publisher = json_data["publisher"]
        self.published_through = json_data["publishedThroughHub"]

