from car_module.car_components.engine.engine_interface import Engine

class CapuletEngine(Engine):
    def __init__(self, current_mileage :int, last_service_mileage:int ):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self) ->bool:
        return self.current_mileage - self.last_service_mileage > 30000
