import requests
from models import Account, Release, Exchange, Hub, HubData, Post

endpoint = 'https://api.ninaprotocol.com/v1/'

def print_error(error, call):
    print(f"{call} responded with a {error} error")

def get_all_accounts():
    response = requests.get(f'{endpoint}/accounts')
    if response.status_code != 200: print_error(response, "get_all_accounts") 
    # TODO
    return [], response.json()["total"]
    
def get_account_by_public_key(publicKey):
    response = requests.get(f'{endpoint}/accounts/{publicKey}')
    if response.status_code != 200: print_error(response, "get_account_by_public_key") 
    return Account(response.json(), publicKey)

def get_collected_by_public_key(publicKey):
    response = requests.get(f'{endpoint}/accounts/{publicKey}/collected')
    if response.status_code != 200: print_error(response, "get_account_by_public_key") 
    return [Release(release) for release in response.json()["collected"]]

def get_exchanges_by_public_key(publicKey):
    response = requests.get(f'{endpoint}/accounts/{publicKey}/exchanges')
    if response.status_code != 200: print_error(response, "get_exchanges_by_public_key") 
    return [Exchange(exchange) for exchange in response.json()["exchanges"]]

def get_hubs_by_public_key(publicKey):
    response = requests.get(f'{endpoint}/accounts/{publicKey}/hubs')
    if response.status_code != 200: print_error(response, "get_hubs_by_public_key") 
    return [Hub(hub) for hub in response.json()["hubs"]]

def get_posts_by_public_key(publicKey):
    # untested
    response = requests.get(f'{endpoint}/accounts/{publicKey}/posts')
    if response.status_code != 200: print_error(response, "get_posts_by_public_key") 
    return [Post(post) for post in response.json()["posts"]]

def get_published_by_public_key(publicKey):
    response = requests.get(f'{endpoint}/accounts/{publicKey}/published')
    if response.status_code != 200: print_error(response, "get_published_by_public_key")  
    return [Release(release) for release in response.json()["published"]]

def get_all_exchanges():
    response = requests.get(f'{endpoint}/exchanges')
    if response.status_code != 200: print_error(response, "get_all_exchanges")
    return [Exchange(exchange) for exchange in response.json()["exchanges"]], response.json()["total"]

def get_exchange_by_public_key(publicKey):
    response = requests.get(f'{endpoint}/exchanges/{publicKey}')
    if response.status_code != 200: print_error(response, "get_published_by_public_key")  
    return Exchange(response.json()["exchange"])

def get_all_hubs():
    response = requests.get(f'{endpoint}/hubs')
    if response.status_code != 200: print_error(response, "get_all_hubs")
    return [Hub(hub) for hub in response.json()["hubs"]], response.json()["total"]

def get_hub_by_public_key_or_handle(publicKeyOrHandle):
    response = requests.get(f'{endpoint}/hubs/{publicKeyOrHandle}')
    if response.status_code != 200: print_error(response, "get_hub_by_public_key")
    return HubData(response.json())  

def get_collaborators_by_public_key_or_handle(publicKeyOrHandle):
    response = requests.get(f'{endpoint}/hubs/{publicKeyOrHandle}/collaborators')
    if response.status_code != 200: print_error(response, "get_collaborators_by_public_key_or_handle")
    return [key for key in response.json()["collaborators"]], response.json()["publicKey"]

def get_releases_by_public_key_or_handle(publicKeyOrHandle):
    response = requests.get(f'{endpoint}/hubs/{publicKeyOrHandle}/releases')
    if response.status_code != 200: print_error(response, "get_releases_by_public_key_or_handle")
    return [Release(release) for release in response.json()["releases"]], response.json()["publicKey"]

def get_all_posts():
    response = requests.get(f'{endpoint}/posts')
    if response.status_code != 200: print_error(response, "get_all_posts")
    return [Post(post) for post in response.json()["posts"]], response.json()["total"]

def get_post_by_public_key(publicKey):
    response = requests.get(f'{endpoint}/posts/{publicKey}')
    if response.status_code != 200: print_error(response, "get_post_by_public_key")  
    return Post(response.json()["post"])

def get_all_releases():
    response = requests.get(f'{endpoint}/releases')
    if response.status_code != 200: print_error(response, "get_all_releases")
    return [Release(release) for release in response.json()["releases"]], response.json()["total"]

def get_release_by_public_key(publicKey):
    response = requests.get(f'{endpoint}/releases/{publicKey}')
    if response.status_code != 200: print_error(response, "get_release_by_public_key")  
    return Release(response.json()["release"])

def get_collectors_by_public_key(publicKey):
    response = requests.get(f'{endpoint}/releases/{publicKey}/collectors')
    if response.status_code != 200: print_error(response, "get_collectors_by_public_key") 
    return [collector for collector in response.json()["collectors"]]

def get_hubs_by_public_key(publicKey):
    response = requests.get(f'{endpoint}/releases/{publicKey}/hubs')
    if response.status_code != 200: print_error(response, "get_hubs_by_public_key") 
    return [Hub(hub) for hub in response.json()["hubs"]]

def get_exchanges_by_public_key(publicKey):
    response = requests.get(f'{endpoint}/releases/{publicKey}/exchanges')
    if response.status_code != 200: print_error(response, "get_exchanges_by_public_key") 
    return [Exchange(exchange) for exchange in response.json()["exchanges"]]

def search(query):
    # untested
    response = requests.post(f'{endpoint}/search', json=query)
    if response.status_code != 200: print_error(response, "search")
    return response

print(get_hub_by_public_key_or_handle("7Pc1WR8Rxt9UAgphNUA4jd8TXRFWuQhHyAG4jEhzbFkY").hub.public_key)
