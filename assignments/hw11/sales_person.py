"""

"""


class SalsePerson:

    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name_change):
        self.name = name_change

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        self.sales_total = 0
        for sale in self.sales:
            sales_total = self.sales_total + sale
        return self.sales_total

    def get_sales(self):
        return self.sales_total

    def met_quota(self, quota):
        if self.sales_total >= quota:
            return True
        else:
            return False

    def compare_to(self, other):
        if other > self.sales_total:
            return -1
        elif self.sales_total > other:
            return 1
        else:
            return 0

    def __str__(self):
        return self.employee_id, "-", self.name, ":", self.sales_total



