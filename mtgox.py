import json
import urllib.request
import logging

def get_trades():
    page = urllib.request.urlopen(
        "http://mtgox.com/code/data/getTrades.php").read()
    return json.loads(str(page, "utf-8"))

def get_depth():
    page = urllib.request.urlopen(
        "http://mtgox.com/code/data/getDepth.php").read()
    return json.loads(str(page, "utf-8"))

def ticker():
    page = urllib.request.urlopen(
        "http://mtgox.com/code/data/ticker.php").read()
    return json.loads(str(page, "utf-8"))

class MtGoxUser:
    def __init__(self, username, password):
        self.params = {"name": username, "pass": password}
        
    
    def get_balance(self):
        url = "https://mtgox.com/code/getFunds.php"
        page = urllib.request.urlopen(url, 
            bytes(urllib.parse.urlencode(self.params), "utf-8")).read()
        return json.loads(str(page, "utf-8"))
    
    def get_orders(self):
        url = "https://mtgox.com/code/getOrders.php"
        page = urllib.request.urlopen(url, 
            bytes(urllib.parse.urlencode(self.params), "utf-8")).read()
        return json.loads(str(page, "utf-8"))
    
    def buy(self, amount, price):
        url = "https://mtgox.com/code/buyBTC.php"
        params = self.params + {"amount": amount, "price": price}
        page = urllib.request.urlopen(url, 
            bytes(urllib.parse.urlencode(params), "utf-8")).read()
        return json.loads(str(page, "utf-8"))

    def sell(self, amount, price):
        url = "https://mtgox.com/code/sellBTC.php"
        params = self.params + {"amount": amount, "price": price}
        page = urllib.request.urlopen(url, 
            bytes(urllib.parse.urlencode(params), "utf-8")).read()
        return json.loads(str(page, "utf-8"))
    
    def cancel(self, oid, order_type):
        url = "https://mtgox.com/code/cancelOrder.php"
        params = self.params + {"oid": oid, "type": order_type}
        page = urllib.request.urlopen(url, 
            bytes(urllib.parse.urlencode(params), "utf-8")).read()
        return json.loads(str(page, "utf-8"))
    
    def withdraw(self, btca, amount):
        url = "https://mtgox.com/code/withdraw.php"
        params = self.params + \
            {"group1": "BTC", "btca": btca, "amount": amount}
        page = urllib.request.urlopen(url, 
            bytes(urllib.parse.urlencode(params), "utf-8")).read()
        page = urllib.request.urlopen(url).read()
        return json.loads(str(page, "utf-8"))

