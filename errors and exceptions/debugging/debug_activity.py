
import pdb

from test_trigger import Trigger, Circle

Trigger.trigger_error()

circle1 = Circle(5)

print(circle1)

pdb.set_trace()

area = circle1.area()
print(area)

diameter = circle1.diameter()