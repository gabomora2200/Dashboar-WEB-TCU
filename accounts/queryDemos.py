from models import *

# (1)Devuelve todos los clientes de la tabla de clientes.
customers = Customer.objects.all()

# (2)Devuelve el primer cliente de la tabla de clientes
firstCustomer = Customer.objects.first()

# (3)Devuelve el último cliente de la tabla de clientes
lastCustomer = Customer.objects.last()

# (4)Devuelve un unico cliente que busca por nombre
customerByName = Customer.objects.get(name='Peter Piper')

# (5)Devuelve un cliente por identificacion
customerById = Customer.objects.get(id=4)

# (6)Devuelve las ordenes que existan asociadas a un cliente
firstCustomer.order_set.all()

# (7)Returns orders customer name: (Query parent model values)
order = Order.objects.first()
parentName = order.customer.name

# (8)Devuelve todos los productos dentro de la categoria Out door
products = Product.objects.filter(category="Out Door")

# (9) Ordena los productos por identificador
leastToGreatest = Product.objects.all().order_by('id')
greatestToLeast = Product.objects.all().order_by('-id')


# (10)Devuelve todos los productos con la categoria de deportes
productsFiltered = Product.objects.filter(tags__name="Sports")

'''
(11)Bonus
Q: If the customer has more than 1 ball, how would you reflect it in the database?
A: Because there are many different products and this value changes constantly you would most 
likly not want to store the value in the database but rather just make this a function we can run
each time we load the customers profile
'''

# Returns the total count for number of time a "Ball" was ordered by the first customer
ballOrders = firstCustomer.order_set.filter(product__name="Ball").count()

# Returns total count for each product orderd
allOrders = {}

for order in firstCustomer.order_set.all():
    if order.product.name in allOrders:
        allOrders[order.product.name] += 1
    else:
        allOrders[order.product.name] = 1

# Returns: allOrders: {'Ball': 2, 'BBQ Grill': 1}


# RELATED SET EXAMPLE
class ParentModel(models.Model):
    name = models.CharField(max_length=200, null=True)


class ChildModel(models.Model):
    parent = models.ForeignKey(Customer)
    name = models.CharField(max_length=200, null=True)


parent = ParentModel.objects.first()
# Returns all child models related to parent
parent.childmodel_set.all()
