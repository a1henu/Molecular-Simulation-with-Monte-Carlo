from abc import ABC, abstractmethod
from typing import Tuple

class BaseSystem(ABC):
    @abstractmethod
    def calc_energy(self) -> float:...

    @abstractmethod
    def trial_move(self) -> Tuple[float, float]:...

    @abstractmethod
    def accept_move(self) -> None:...

    @abstractmethod
    def reject_move(self) -> None:...
