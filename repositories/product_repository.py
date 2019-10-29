from models.product_model import Product

class ProductRepository():
    
    def get_product(self, productId):
        return Product.select() \
                      .where(Product.name == productId) \
                      .first()
    
    def get_products(self):
        return Product.select() \
                      .execute()

    def create_product(self, name, description, completionDate, version, managerId, image):
        if not image:
            image = "2.jpg"
        Product.create(name=name, description=description, completion_date=completionDate, image=image, version=version, manager_id=managerId)
    
    def search_product(self, productPattern):
        return Product.select() \
                      .where(Product.name.contains(productPattern)) \
                      .execute()

    def check_product(self, productId):
        return Product.select() \
                      .where(Product.name == productId) \
                      .exists()
