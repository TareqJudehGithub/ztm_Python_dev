"""
MRO - Method Resolution Order
 - MRO is a rule that Python follows to determine when you run a method which
   method to run.
 - class_name.mro() or class_name.__mor__()
"""
class A:
    num = 10


class B(A):
    pass

class C(A):
    num = 1

class D(B, C):
    pass