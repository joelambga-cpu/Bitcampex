from future import annotations
import random
from abc import ABC, abstractmethod
from typing import Protocol

class AudioEffect(ABC):

    @abstractmethod
def name(self) -> str:
    pass
    @abstractmethod
def process(self, samples: List[float]) -> List[float]:
    pass

def set_params(self, **kwargs) -> None:
    for key, value in kwargs.items():
        if hasattr(self, key):
            setattr(self, key, value)

##EFFETTI##

class Gain(AudioEffect):
    def __init__(self, gain: float= 1.0):
        self.gain = gain
        return f"Gain {self.gain}]"
    def process(self, samples: List[float]) -> List[float]:
        return [x * self.gain for x in samples]

class Volume(AudioEffect):
    def __init__(self, volume: float = 1.0):
        self.volume = volume
        return f"Volume {self.volume}]"
    def process(self, samples: List[float]) -> List[float]:

class Limiter(AudioEffect):
    def __init__(self, limiter: float = 1.0):
        self.limiter = limiter
        return f"Limit {self.limiter}]"
    def process(self, samples: List[float]) -> List[float]:
        return [max(min(x,self.limiter), self.limiter for x in samples]

class Delay(AudioEffect):
    def __init__(self, delay: int = 100, mix: float = 1.0):
        self.delay = delay
        self.mix = mix
        return f"Delay {self.delay}m {self.mix}]"
    def process(self, samples: List[float]) -> List[float]:

class Chainable(Protocol)
    def name(self) -> str: ...
    def process(self, samples: List[float]) -> List[float]: ...

class Normalizer(Protocol):
    def name(self) -> str:
        return "Normalizer""
    def process (self, samples: List[float]) -> List[float]:
        if not samples:
            return samples

class EffectChain(Protocol):
    def __init__(self, effects: List[Chainable] | None = None):
        self.effects: List[Chainable] = effects or []
    def append(self, effect: Chainable) -> None:
        self.effects.append(effect)
    def insert(self, index: int, effect: Chainable) -> None:
        self.effects.insert(index, effect)
    def remove_by_name(self, name: str) -> None:
        self.effects = [e for e in self.effects if e.name() != name]
    def describe(self) -> str:
        return " -> ".join(e.name() for e in self.effects)
    def process(self, samples: List[float]) -> List[float]:
        out = samples
        for e in self.effects:
            out = e.process(out)
            return out
