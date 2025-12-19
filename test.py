# @erp.feature FEAT-TEST-001

def calculate_discount(price, rate):
    """
    Calculates the final price after discount.
    """
    if rate > 1.0:
        return price
    return price * (1 - rate)
