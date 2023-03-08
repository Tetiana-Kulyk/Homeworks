from abc import ABC, abstractmethod


class IKitchenAppliance(ABC):

    @abstractmethod
    def _start(self): ...

    @abstractmethod
    def mode_selection(self, value): ...

    @abstractmethod
    def _processing(self): ...

    @abstractmethod
    def _stop(self): ...
