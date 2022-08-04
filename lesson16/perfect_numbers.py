def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    result = 0
    for i in range(1, number):
        if number % i == 0:
            result += i
    if result == number:
        return "perfect"
    if result > number:
        return "abundant"
    return "deficient"
