"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    def __init__(self, first_name, last_name, email, password):
        """ Instantiates a customer instance, includes instance attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        """Convenience method to show information about customer in console."""

        return "<Customer: {first_name} {last_name}, {email}, {password}>".format(
            first_name=self.first_name, last_name=self.last_name,
            email=self.email, password=self.password)


def get_customers(customers_file):
    """ Populate dictionary with customer data from file """
    customers_dict = {}
    customers_file = open(customers_file, "r")

    for customer in customers_file:
        customer = customer.rstrip().split("|")
        customer_obj = Customer(customer[0], customer[1], customer[2], customer[3])
        customers_dict[customer_obj.email] = customer_obj

    return customers_dict


def get_by_email(email):
    """ Returns customer info when given email for a customer """

    return customers_dict[email]


customers_dict = get_customers("customers.txt")
