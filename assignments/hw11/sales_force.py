"""

"""

class SalesForce:


    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        sales_people_data = open(file_name, "r")
        self.sales_people = self.sales_people.append(sales_people_data.readlines())

    def quota_report(self, quota):
        list = []
        smaller_list = []
        for i in self.sales_people:
            split_list = i.split(", ")
            smaller_list.append(split_list[0])
            smaller_list.append(split_list[1])
            smaller_list.append(split_list[2])
            total_sales = 0
            for sale in range(split_list[2]):
                total_sales = total_sales + j
            if total_sales >= quota:
                smaller_list.append(True)
            else:
                smaller_list.append(False)
            list.append(smaller_list)
            smaller_list = []

    def top_seller(self):
        names = []
        max_checker = 0
        for name in self.sales_people:
            list_split = name.split(", ")
            total_sales = 0
            for sale in range(list_split[2]):
                total_sales = total_sales + sale
            if total_sales > max_checker:
                max_checker = total_sales
                names = [name]
            elif total_sales == max_checker:
                names = names.append(name)
            else:
                None
            return names

    def individual_sales(self, employee_id):
            for id in self.sales_people:
                if id == employee_id:
                    return name
                else:
                    return None

    def get_sales_frequencies(self):
        sales_frequency = {}
        for name in self.sales_people:
            sales = name.get


