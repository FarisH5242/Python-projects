import os
from package import ParentClass

@nonsenseDecorator
def doesNothing():
    passclass

ExampleClass(ParentClass):
    @staticmethod
    def example(inputStr):
        a = list(inputStr)
        a.reverse()
        return''.join(a)
        
    def __init__(slef,mixin='Hello'):
        self.mixin = mixin
