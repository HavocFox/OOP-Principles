class BudgetCategory:
    def __init__(self, catname, catbud):
        self.__catname = catname
        self.__catbud = catbud
        self.__expense = 0

    def get_category_name(self):
        return self.__catname

    def get_allocated_budget(self):
        return self.__catbud

    def set_allocated_budget(self, new_catbud):
        if new_catbud >= 0:
            self.__catbud = new_catbud
        else:
            print("Error: Budget should be a positive number.")

    def get_expense(self):
        return self.__expense

    def add_expense(self, amount):
        if amount >= 0:
            self.__expense += amount
            print("An expense equal to the amount of $", amount, "has been added to the category", self.__catname, ".")
        else:
            print("Please enter a positive number. You can't add a negative one.")

    def display_budget_details(self):
        print("Category:", self.__catname)
        print("Allocated Budget:", self.__catbud)
        print("Total Expenses:", self.__expense)


# Example usage (retained)
food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_budget_details()
