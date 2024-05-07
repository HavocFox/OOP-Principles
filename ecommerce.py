class Product:
    def __init__(self, productid, name, price):
        self.productid = productid
        self.name = name
        self.price = price

    def display_info(self):
        print("Product info: ")
        print(f"    Product ID: {self.productid}\n    Product Name: {self.name}\n    Product Price: ${self.price}\n")

class Book(Product):
    def __init__(self, product_id, name, price, author, pubdate):
        super().__init__(product_id, name, price)
        self.author = author
        self.pubdate = pubdate

    def display_info(self):
        print("Book info: ")
        print(f"    Book Product ID: {self.productid}\n    Book Name: {self.name}\n    Book Price: ${self.price}\n   Book Author: {self.author}\n   Date Published: {self.pubdate}")

# Example usage
my_product = Product("456", "Headphones", 50.00)
my_book = Book("123", "Python Essentials", 29.99, "J. Doe", "10/20/2019")
my_product.display_info()
my_book.display_info()