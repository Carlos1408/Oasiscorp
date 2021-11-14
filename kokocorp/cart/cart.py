from .models.order import Order
from .models.order_detail import Order_detail
from catalogue.models.product import Product

class Cart():

    def __init__(self, request):
        self.session = request.session
        try:
            self.cart = self.session['cart']
        except:
            self.cart = dict()

        try:
            self.total = self.session['total']
        except:
            self.total = 0

    def __str__(self):
        table = list()
        for product in self.cart.values():
            row = f"{product['name']}\tx{product['quantity']}\t{product['unit_price']}$\t{product['subtotal']}$"
            table.append(row)
        table.append(f"Total: {self.total}$")
        return '\n'.join(table)
    
    def addProduct(self, product, quantity=1):
        try:
            cart_prod = self.cart[str(product.id)]
            cart_prod['quantity'] += quantity
            cart_prod['subtotal'] += quantity * product.unit_price
        except:
            cart_prod = {
                    'name' : product.name,
                    'unit_price' : product.unit_price,
                    'supplier' : product.supplier.name,
                    'image_url' : product.image.url,
                    'quantity' : quantity,
                    'subtotal' : quantity * product.unit_price
                    }
        self.cart[str(product.id)] = cart_prod
        self.total += product.unit_price * quantity
        self.saveCart()

    def subtractProduct(self, product, quantity=1):
        cart_prod = self.cart[product.id]
        if quantity >= cart_prod['quantity']:
            self.removeProduct(product.id)
        else:
            cart_prod['quantity'] -= quantity
            cart_prod['subtotal'] -= quantity * product.price
            self.total -= quantity * product.price
        self.saveCart()

    def confirmOrder(self, request):
        user = request.user
        order = Order.objects.create(
                user = user,
                cost = self.total
                )
        for product_id, cart_prod in self.cart.items():
            product = Product.objects.get(id = int(product_id))
            order_d = Order_detail.objects.create(
                    product = product,
                    order = order,
                    amount = cart_prod['quantity'],
                    cost = cart_prod['subtotal']
                    )
            product.stock -= cart_prod['quantity']
            product.save()
        self.clearCart()


    def removeProduct(self, product_id):
        self.total -= self.cart[product_id]['subtotal']
        del self.cart[product_id]
        self.saveCart()

    def saveCart(self):
        self.session['cart'] = self.cart
        self.session['total'] = self.total
        self.session.modified = True

    def clearCart(self):
        self.cart = {}
        self.total = 0
        self.saveCart()
