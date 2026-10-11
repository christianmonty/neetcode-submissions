import math

class AreaCalc:
    # TODO: Implement calculate method
    '''
    def calculate(self, length, width=None):
        if width is None: # must just be radius
            return round(length * length * math.pi, 2)
        else:
            return length * width
    '''

    def calculate(self, *args):
        if len(args) == 1:
            return round(args[0] * args[0] * math.pi, 2)
        else:
            return args[0] * args[1]
            
            
    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
