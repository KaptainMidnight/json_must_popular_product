import json


class Analyser():  # Create class for analyse data.json
    json_data = []

    def load_data(self, file_name):
        with open(file_name) as data:
            self.json_data = json.loads(data.read())

    def analyse(self, baskets):
        count_product = dict()
        for elements in baskets:
            for product in elements:
                product_in_counter = count_product.get(product["name"])
                if product_in_counter:
                    product_in_counter += product["count"]
                    count_product.update({product["name"]: product_in_counter})
                else:
                    count_product.update({product["name"]: product["count"]})

        sorted_count = sorted(count_product, key=count_product.get, reverse=True)
        for r in sorted_count:
            print(r, count_product[r])


analyser = Analyser()

analyser.load_data("data.json")
baskets = analyser.json_data["baskets"]
analyser.analyse(baskets)