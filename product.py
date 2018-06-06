class Product:
    def __init__(self,price,item_name,weight,brand):
        self.price=price
        self.item_name=item_name
        self.weight=weight
        self.brand=brand
        self.status="for sale"
        self.condition="new"
    def sell(self):
        self.status="sold"
        return self
    def add_tax(self, tax):
        return self.price*(1+tax)
    def returnItem(self, reason_for_return):
        self.reason_for_return=reason_for_return
        if self.reason_for_return=="defective":
            self.conditon="defective"
            self.price=0;
            return self
        elif self.reason_for_return=="like_new":
            self.condition="like_new"
            self.status="forsale"
            return self
        elif self.reason_for_return=="opened":
            self.condition="used"
            self.status="for sale"
            self.price*=.8
            return self
    def display_info(self):
        print ("Brand:", self.brand, "Product:", self.item_name, "Status:", self.status, "Consition", self.condition)
        return self
FlippyFlops=Product(120,"My Flippy Floppies",2,"olukai")
FlippyFlops.display_info()


