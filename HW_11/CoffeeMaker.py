from IKitchenAppliance import IKitchenAppliance
from IBeveragePreparationEquipment import IBeveragePreparationEquipment


# Abstraction
# Inheritance
class CoffeeMaker(IKitchenAppliance, IBeveragePreparationEquipment):
    def __init__(self):
        self.__status = False
        self.__components = False
        self.__are_components_prepared = False
        self.__is_water_boiled = False
        self.__value = "Coffee"

    # Polymorphism
    def _start(self):
        self.__status = True
        print("The Coffee Maker is starting the process.")

    def mode_selection(self, value):
        self.__value = value
        print(f"Please place your cup on the brewing chamber and wait while the {self.__value} is being prepared.")
        return self._processing()

    def _components_check(self):
        if self.__status:
            self.__components = True
            print("Checking if all components are available.")

    def _components_preparation(self):
        if self.__components:
            self.__are_components_prepared = True
            self.__is_water_boiled = True
            print("The grains are grounding. The water is boiling.")

    def _serving(self):
        if self.__are_components_prepared and self.__is_water_boiled:
            print(f"Don't remove the cup, the {self.__value} is pouring.")

    def _stop(self):
        self.__status = False
        print("The Coffe Maker is finishing its work.")

    # Encapsulation
    def _processing(self):
        self._start()
        self._components_check()
        self._components_preparation()
        self._serving()
        self._stop()
        return f"Enjoy your {self.__value}!"

