import json


class Analyser():  # Create class for analyse data.json
    json_data = []  # Create list for json data

    def load_data(self, file_name):  # Function for load data json
        with open(file_name) as data:  # Open file data.json
            self.json_data = json.loads(data.read())  # Read data.json

    def analyse(self, baskets):  # Analysis json data
        count_product = dict()  # Count product in data.json
        for elements in baskets:  # Plunk element in dat.json
            for product in elements:  # Plunk product in data.json
                product_in_counter = count_product.get(product["name"])  # Search product counter in data.json with key name 
                if product_in_counter:
                    product_in_counter += product["count"]  # Increases variable product_in_counter
                    count_product.update({product["name"]: product_in_counter})  # Update dictionary count_product
                else:
                    count_product.update({product["name"]: product["count"]})  # Update dictionary count_product
        '''Count rating product'''
        sorted_count = sorted(count_product, key=count_product.get, reverse=True)  # Sorting product ascending
        for r in sorted_count:  # Cycl for plunk sorted dictionary
            print(r, count_product[r])


analyser = Analyser()  # Initialize class Analyser
'''Load data.json'''
analyser.load_data("data.json")
baskets = analyser.json_data["baskets"]
analyser.analyse(baskets)
