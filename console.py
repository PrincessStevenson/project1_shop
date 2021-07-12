
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

product1 = Product("Rampant Rabbit", "Toys", "The Rampant Rabbit is probably one of the most well-known 'pets'. With multiple speeds and methods of play, the Rampant Rabbit is the perfect all-rounder!", 5, 7.99, 19.99, manufacturer2, True)
product_repository.save(product1)
product2 = Product("Organic Eggs", "Toys", "Organic with a clean, smooth finish, these eggs boast numerous functions. Now wireless, eggs are great for amping up the antics in every day life as well as for spontaneous getaways. Small enough to not fill you up, but big enough to fill the hole.", 6, 6.12, 12.60, manufacturer2, True)
product_repository.save(product2)
product3 = Product("B-Plug", "Toys", "Standared sized b-plug for all levels of experience. Made from flexible-but-firm black rubber, dip your toes into the world of whole-body sensations. This plug also comes with a handy, little silver chain for ease of removal.", 2, 4.20, 9.99, manufacturer1, True)
product_repository.save(product3)
product4 = Product("Jewelled B-Plug", "Toys", "Delve into the heart of your pleasure with this heart-shaped, jewelled, metal b-plug. Metal can be cooled or heated according to preference. For use with water-based products. Perfectly paired with the Rampant Rabbit, Add a little sparkle and glamour to your life now!", 2, 10.50, 18.99, manufacturer1, True)
product_repository.save(product4)
product5 = Product("Maid Outfit", "Uniforms", "Tired of your normal clothes getting ripped? Sick of your normal clothes getting dirty while you're polishing that knob? Then this is the perfect outfit for you! Typically originating from France, the 'French Maid's Outfit' is now available in black and white, complete with tie-up apron!", 10, 12.75, 20.00, manufacturer4, True)
product_repository.save(product5)
product6 = Product("Gardening Outfit", "Uniforms", "Be at one with nature with our one-size-fit's all gardener's outfit. Suitable for both dry and wet weather, sleeveless for those hot times and poppers down both sides for speedy assitance with that pesky hose!", 7, 14.69, 24.99, manufacturer4, True)
product_repository.save(product6)
product7 = Product("%s", "%s", "%s", "%s", "%s", "%s", "%s", False)
product_repository.save(product7)
product8 = Product("%s", "%s", "%s", "%s", "%s", "%s", "%s", False)
product_repository.save(product8)


# Experience some life 'au naturel' with the new minimal-material design,

pdb.set_trace()