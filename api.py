import requests
from models import Account, Release, Exchange, Hub, HubData, Post

endpoint = 'https://api.ninaprotocol.com/v1/'

def print_error(error, call):
    print(f"{call} responded with a {error} error")
    return None

def get_all_accounts(limit = 20):
    # Returns {limit} long list of account public keys
    response = requests.get(f'{endpoint}/accounts?limit={limit}')
    if response.status_code != 200: return print_error(response, "get_all_accounts") 
    return [acc["publicKey"] for acc in response.json()["accounts"]], response.json()["total"]

def get_account_by_public_key(publicKey):
    # Returns account object with public key = publicKey 
    response = requests.get(f'{endpoint}/accounts/{publicKey}')
    if response.status_code != 200: return print_error(response, "get_account_by_public_key") 
    return Account(response.json(), publicKey)

def get_collected_by_public_key(publicKey):
    # Returns list of Release objects that this account has collected
    response = requests.get(f'{endpoint}/accounts/{publicKey}/collected')
    if response.status_code != 200: return print_error(response, "get_account_by_public_key") 
    return [Release(release) for release in response.json()["collected"]]

def get_exchanges_by_public_key(publicKey):
    # Returns list of Exchange objects that this account has taken part in
    response = requests.get(f'{endpoint}/accounts/{publicKey}/exchanges')
    if response.status_code != 200: return print_error(response, "get_exchanges_by_public_key") 
    return [Exchange(exchange) for exchange in response.json()["exchanges"]]

def get_hubs_by_public_key(publicKey):
    # Returns list of Hub objects that this account is a collaborator on
    response = requests.get(f'{endpoint}/accounts/{publicKey}/hubs')
    if response.status_code != 200: return print_error(response, "get_hubs_by_public_key") 
    return [Hub(hub) for hub in response.json()["hubs"]]

def get_posts_by_public_key(publicKey):
    # TO DO: test this
    # Returns a list of Post objects that this account has published
    response = requests.get(f'{endpoint}/accounts/{publicKey}/posts')
    if response.status_code != 200: return print_error(response, "get_posts_by_public_key") 
    return [Post(post) for post in response.json()["posts"]]

def get_published_by_public_key(publicKey):
    # Return list of Release objects that this account has published
    response = requests.get(f'{endpoint}/accounts/{publicKey}/published')
    if response.status_code != 200: return print_error(response, "get_published_by_public_key")  
    return [Release(release) for release in response.json()["published"]]

def get_all_exchanges(limit = 20):
    # Returns {limit} long list of Exchange objects. 
    # May not contain all the info that get_exchange_by_public_key provides
    response = requests.get(f'{endpoint}/exchanges?limit={limit}')
    if response.status_code != 200: return print_error(response, "get_all_exchanges")
    return [Exchange(exchange) for exchange in response.json()["exchanges"]], response.json()["total"]

def get_exchange_by_public_key(publicKey):
    # Returns Exchange object
    response = requests.get(f'{endpoint}/exchanges/{publicKey}')
    if response.status_code != 200: return print_error(response, "get_published_by_public_key")  
    return Exchange(response.json()["exchange"])

def get_all_hubs(limit = 20):
    # Returns {limit} long list of Hub objects
    # Doesn't contain all the info that get_hub_by_public_key_or_handle provides 
    response = requests.get(f'{endpoint}/hubs?limit={limit}')
    if response.status_code != 200: return print_error(response, "get_all_hubs")
    return [Hub(hub) for hub in response.json()["hubs"]], response.json()["total"]

def get_hub_by_public_key_or_handle(publicKeyOrHandle):
    # Returns HubData object, which in turn contains a Hub object
    response = requests.get(f'{endpoint}/hubs/{publicKeyOrHandle}')
    if response.status_code != 200: return print_error(response, "get_hub_by_public_key")
    return HubData(response.json())  

def get_collaborators_by_public_key_or_handle(publicKeyOrHandle):
    # Returns list of public keys of accounts that collaborate on this hub
    response = requests.get(f'{endpoint}/hubs/{publicKeyOrHandle}/collaborators')
    if response.status_code != 200: return print_error(response, "get_collaborators_by_public_key_or_handle")
    return [key for key in response.json()["collaborators"]], response.json()["publicKey"]

def get_releases_by_public_key_or_handle(publicKeyOrHandle):
    # Returns list of Release objects posted to hub specified by publicKeyOrHandle
    response = requests.get(f'{endpoint}/hubs/{publicKeyOrHandle}/releases')
    if response.status_code != 200: return print_error(response, "get_releases_by_public_key_or_handle")
    return [Release(release) for release in response.json()["releases"]], response.json()["publicKey"]

def get_all_posts(limit = 20):
    # Returns {limit} long list of Post objects
    response = requests.get(f'{endpoint}/posts?limit={limit}')
    if response.status_code != 200: return print_error(response, "get_all_posts")
    return [Post(post) for post in response.json()["posts"]], response.json()["total"]

def get_post_by_public_key(publicKey):
    # Return Post object specified by publicKey
    response = requests.get(f'{endpoint}/posts/{publicKey}')
    if response.status_code != 200: return print_error(response, "get_post_by_public_key")  
    return Post(response.json()["post"])

def get_all_releases(limit = 20):
    # Returns {limit} long list of Release objects
    response = requests.get(f'{endpoint}/releases?limit={limit}')
    if response.status_code != 200: return print_error(response, "get_all_releases")
    return [Release(release) for release in response.json()["releases"]], response.json()["total"]

def get_release_by_public_key(publicKey):
    # Returns Release object specified by publicKey
    response = requests.get(f'{endpoint}/releases/{publicKey}')
    if response.status_code != 200: return print_error(response, "get_release_by_public_key")  
    return Release(response.json()["release"])

def get_collectors_by_public_key(publicKey):
    # Return list of account public keys of accounts that have collected the release specified by publicKey
    response = requests.get(f'{endpoint}/releases/{publicKey}/collectors')
    if response.status_code != 200: return print_error(response, "get_collectors_by_public_key") 
    return [collector for collector in response.json()["collectors"]]

def get_hubs_by_public_key(publicKey):
    # Returns list of Hub objects that this release is part of
    response = requests.get(f'{endpoint}/releases/{publicKey}/hubs')
    if response.status_code != 200: return print_error(response, "get_hubs_by_public_key") 
    return [Hub(hub) for hub in response.json()["hubs"]]

def get_exchanges_by_public_key(publicKey):
    # Returns list of Exchange objects that this release was part of
    response = requests.get(f'{endpoint}/releases/{publicKey}/exchanges')
    if response.status_code != 200: return print_error(response, "get_exchanges_by_public_key") 
    return [Exchange(exchange) for exchange in response.json()["exchanges"]]

def search(query):
    # TO DO: test this more thoroughly
    # Returns dictionary containing 4 lists of public keys: accounts, releases, hubs, and artists
    # that match the search query (str)
    response = requests.post(f'{endpoint}/search', json={"query": query})
    if response.status_code != 200: return print_error(response, "search")
    dict = {}
    dict["accounts"] = [acc["account"] for acc in response.json()["accounts"]]
    dict["releases"] = [release["publicKey"] for release in response.json()["releases"]]
    dict["hubs"] = [hub["publicKey"] for hub in response.json()["hubs"]]
    dict["artists"] = [artist["account"]["publicKey"] for artist in response.json()["artists"]]
    return dict

