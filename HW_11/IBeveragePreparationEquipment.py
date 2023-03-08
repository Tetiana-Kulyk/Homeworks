from abc import ABC, abstractmethod


class IBeveragePreparationEquipment(ABC):
    @abstractmethod
    def _components_check(self): ...

    @abstractmethod
    def _components_preparation(self): ...

    @abstractmethod
    def _serving(self): ...
