def is_even(value):
    """Return True if *value* is even."""
    return (value % 2) == 0

def count_occurrences(target_list, predicate):
    """Return the number of times applying the callable *predicate* to a
    list element returns True."""
    return sum([1 for e in target_list if predicate(e)])



def surround_with(surrounding):
    """Return a function that takes a single argument and."""
    def surround_with_value(word):
        return '{}{}{}'.format(surrounding, word, surrounding)
    return surround_with_value

def transform_words(content, targets, transform):
    """Return a string based on *content* but with each occurrence
    of words in *targets* replaced with
    the result of applying *transform* to it."""
    result = ''
    for word in content.split():
        if word in targets:
            result += ' {}'.format(transform(word))
        else:
            result += ' {}'.format(word)
    return result

def currency(f):
    def wrapper(*args, **kwargs):
        return '$' + str(f(*args, **kwargs))

    return wrapper

class Product():

    def __init__(self,price):
        self.price = price

    def price_with_tax(self, tax_rate_percentage):
        """Return the price with *tax_rate_percentage* applied.
        *tax_rate_percentage* is the tax rate expressed as a float, like
        "7.0" for a 7% tax rate."""
        return self.price * (1 + (tax_rate_percentage * .01))

    @currency
    def price_with_tax_with_decorator(self, tax_rate_percentage):
        """Return the price with *tax_rate_percentage* applied.
        *tax_rate_percentage* is the tax rate expressed as a float, like
        "7.0" for a 7% tax rate."""
        return self.price * (1 + (tax_rate_percentage * .01))


if __name__ == '__main__':

    ## Function as argument
    my_predicate = is_even
    my_list = [2, 4, 6, 7, 9, 11]
    result = count_occurrences(my_list, my_predicate)
    print(result)

    ## Return function
    markdown_string = 'My name is Jeff Knupp and I like Python but I do not own a Python'
    markdown_string_italicized = transform_words(markdown_string, ['Python', 'Jeff'],
            surround_with('*'))
    print(markdown_string_italicized)


    ## Decorator example
    p = Product(3)
    print(p.price_with_tax(0.8))
    print(p.price_with_tax_with_decorator(0.8))