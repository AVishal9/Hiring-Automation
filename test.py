# @erp.feature 4me4nledo8

def calculate_discount(price, rate):
    """
    Calculates the final price after discount.
    """
    if rate > 1.0:
        return price
    return price * (1 - rate)
