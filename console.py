
import pdb
from models.manufacturer import Manufacturer
from models.product import Product
import repositories.manufacturer_repository as manufacturer_repository
import repositories.product_repository as product_repository

product_repository.delete_all()
manufacturer_repository.delete_all()


manufacturer1 = Manufacturer("Anne Winters", "Scotland")
manufacturer_repository.save(manufacturer1)
manufacturer2 = Manufacturer("LoveLemon", "England")
manufacturer_repository.save(manufacturer2)
manufacturer3 = Manufacturer("Chinese Whispers", "China")
manufacturer_repository.save(manufacturer3)
manufacturer4 = Manufacturer("Agent Arrested", "France")
manufacturer_repository.save(manufacturer4)

manufacturer_repository.select_all()

product1 = Product("Rampant Rabbit", "Toys", "The Rampant Rabbit is probably one of the most well-known 'pets'. With multiple speeds and methods of play, the Rampant Rabbit is the perfect all-rounder!", 5, 7.99, 19.99, manufacturer2, "https://media.istockphoto.com/photos/cute-standing-chocolate-lionhead-bunny-rabbit-picture-id162055704?k=6&m=162055704&s=612x612&w=0&h=Utfs7da1DE0Tq5ZNg46KwdIfI6s1SZRzEKqx-2SPlJc=")
product_repository.save(product1)
product2 = Product("Organic Eggs", "Toys", "Organic with a clean, smooth finish, these eggs boast numerous functions. Now wireless, eggs are great for amping up the antics in every day life as well as for spontaneous getaways. Small enough to not fill you up, but big enough to fill the hole.", 6, 6.12, 12.60, manufacturer2, "https://images.squarespace-cdn.com/content/v1/565d3a0ce4b07ad504d2981c/1448953645982-657R2SSJLL4K6HJLE986/eggs.jpg?format=2500w")
product_repository.save(product2)
product3 = Product("B-Plug", "Toys", "Standared sized b-plug for all levels of experience. Made from flexible-but-firm black rubber, dip your toes into the world of whole-body sensations. This plug also comes with a handy, little silver chain for ease of removal.", 2, 4.20, 9.99, manufacturer1, "https://lh3.googleusercontent.com/spp/AARfHkwlkAqcJZEe4NNNqQdu3xJJkqNj9OmJSqdsUZPXtCYF6QEFZ0GTeDprbe20xqhpI85eBYXgBuGHPUYcTsXwvv8yvrJx744-jUpupvd2xSRvE49KBKyFkIWoIYgot5EQIdEqDAciPus-VjsMt0ySjARJMtSq5D_0A-aEigIL4-N4JObDEkWry1_QQ-BUklpS67g2h_eyWg=s512-rw-pd-pc0x00ffffff")
product_repository.save(product3)
product4 = Product("Jewelled B-Plug", "Toys", "Feel like Royalty with this jewelled, silicone b-plug. Perfectly paired with the Oragnic Egg, Add a little sparkle and glamour to your life now! Available in 3 pastel colours, suitable to use with water-based liquids.", 2, 10.50, 18.99, manufacturer1, "https://image.dhgate.com/0x0s/f2-albu-g9-M00-1E-61-rBVaWF7rKC2AR_UjAAHkIIi2vCI159.jpg/bathroom-drain-hair-catcher-bath-stopper.jpg")
product_repository.save(product4)
product5 = Product("Maid Outfit", "Uniforms", "Tired of your normal clothes getting ripped? Sick of your normal clothes getting dirty while you're polishing that knob? Then this is the perfect outfit for you! Typically originating from France, the 'French Maid's Outfit' is now available in a variety of colours including the classic black and white, complete with tie-up apron!", 10, 12.75, 20.00, manufacturer4, "https://canary.contestimg.wish.com/api/webimage/5be28fdf267bba3158a87d08-large.jpg?cache_buster=ed1771bc0145c460dc659cb9f1a675a7")
product_repository.save(product5)
product6 = Product("Gardening Outfit", "Uniforms", "Be at one with nature with our one-size-fit's all gardener's outfit. Suitable for both dry and wet weather, sleeveless for those hot times and poppers down both sides for speedy assitance with that pesky hose! Colours include Raunchy Red and BDSM Blue", 7, 14.69, 24.99, manufacturer4, "https://cdn.engelbert-strauss.co.uk/assets/wf/images/DetailPageGallery/product/5.Release.3320381/Bib_brace_e_s_classic_-9262-2-634995483861442860.jpg")
product_repository.save(product6)
product7 = Product("Flower Power Plug", "Toys", "Revive your inner hippie with these funky, multi-coloured b-plugs! Not just a pretty faucet, this plug is both pretty and practical adopting the flower handle design for ease of removal. Made from high-grade silicone, it is soft, flexible and not easy to damage. They can be used for a long time and the handy flower handle makes them easy to use and clean. These plugs are suitable to use with a range of different liquids and its unique spiral design seals securely saving you from having to worry about leakage. Available in 4 different colours to suit all varieties of soakers", 8, 7.99, 11.25, manufacturer3, "https://images-na.ssl-images-amazon.com/images/I/71gdyyUTiWL._AC_SX679_.jpg")
product_repository.save(product7)
product8 = Product("Firefighter Outfit", "Uniforms", "Fight Fire with Fire in this Smokin' New 2 piece! Too Hot to Handle? Don't worry, we've got you covered - literally! Velcro straps along the sides and along the seams for when you need quick access to that fire extinguisher.", 11, 17.32, 24.69, manufacturer4, "https://ae01.alicdn.com/kf/Hba0ce892e7814c35bcb76533867108a1r/New-Factory-sale-FireMan-Uniform.png_50x50.png_.webp")
product_repository.save(product8)


# Experience some life 'au naturel' with the new minimal-material design,
