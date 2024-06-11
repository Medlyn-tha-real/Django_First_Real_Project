from django import template
from num2words import num2words
register = template.Library()

def first_five_upper(value):
    result = value[:5].upper()
    return result

def specified_n_upper(value, n):
    result = value[:n].upper()
    return result

def length_limit(value, limit):
    if len(value) > limit:
        return value[0:limit] + '.....'
    else:
        return value
    
def rating(value):
    if(float(value) >=4):
        return value + "[Excellent]"
    elif (float(value) >=3):
        return value + "[Very Good]"
    elif (float(value) >=1.5):
        return value + "[Average]"
    else:
        return value + "[Poor]"

def convert_number_to_words(value):
    return num2words(value)
    


register.filter('first_five_upper', first_five_upper)
register.filter('specified_upper', specified_n_upper)
register.filter('length_limit', length_limit)
register.filter('rating', rating)
register.filter('convert_number_to_words', convert_number_to_words)


















