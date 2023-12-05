import logging
import employer
logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(name)s :: %(levelname)s :: %(message)s')


def add(x, y):
    return x + y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


def sbt(x, y):
    return x - y


num1 = 20
num2 = 5
add_res = add(num1, num2)
logging.info("result {} + {} = {} ".format(num1, num2, add_res))
subt_res = sbt(num1, num2)
logging.info("result {} - {} = {} ".format(num1, num2, subt_res))

mul_res = mul(num1, num2)
logging.info("result {} * {} = {} ".format(num1, num2, mul_res))

div_res = div(num1, num2)
logging.info("result {} / {} = {} ".format(num1, num2, div_res))
