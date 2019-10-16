from models.product_model import Product

class ProductRepository():
    
    def get_product(self, productId):
        return Product.select() \
                      .where(Product.name == productId) \
                      .first()
    
    def get_products(self):
        return Product.select() \
                      .execute()

    def create_product(self, name, description, image="default", completionDate, version, managerId):
        Product.create(name=name, description=description, image=image, version=version, manager_id=managerId)
