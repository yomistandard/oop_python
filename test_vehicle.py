from poly import Vehicle

car = Vehicle("car","drive")
ship = Vehicle("ship","sail")
plane = Vehicle("plane","fly")
Vehicle.type = ""
Vehicle.movement = ""
print(car.move())
print(plane.move())
print(ship.move())

