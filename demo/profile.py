from OdooLocust import OdooLocust
from SellerTaskSet import SellerTaskSet

class Seller(OdooLocust.OdooLocust):
    host = "127.0.0.1"
    database = "dev"
    user = "admin"
    password = "admin"
    min_wait = 100
    max_wait = 1000
    weight = 3

    tasks = [ SellerTaskSet ]
