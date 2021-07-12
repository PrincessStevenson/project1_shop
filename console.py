import pdb
from models.manufacturer import Manufacturer
from models.product import Product
import repositories.manufacturer_repository as manufacturer_repository
import repositories.product_repository as product_repository

manufacturer_repository.delete_all()
product_repository.delete_all()

manufacturer1 = Manufacturer("Anne Winters", "Scotland")
manufacturer_repository.save(manufacturer1)
manufacturer2 = Manufacturer("LoveLemon", "England")
manufacturer_repository.save(manufacturer2)
manufacturer3 = Manufacturer("Chinese Whispers", "China")
manufacturer_repository.save(manufacturer3)
manufacturer4 = Manufacturer("Agent Arrested", "France")
manufacturer_repository.save(manufacturer4)

manufacturer_repository.select_all()

product1 = Product