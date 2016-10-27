import sys
sys.path.insert(0, '../')
from frameworks.comprehensions import factorial
from frameworks.comprehensions import digit_sum

print(digit_sum(factorial(100)))