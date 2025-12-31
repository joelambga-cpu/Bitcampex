from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Dict, List, Tuple, TypeVar, Generic

T = TypeVar("T")


# ------------------ Esercizi 1–2 ------------------
class RangeRestart:
    """Aggregatore riavviabile che produce a, a+1, ..., b-1."""

    def __init__(self, a: int, b: int) -> None:
        if b < a:
            raise ValueError("b must be >= a")
        self._a = a
        self._b = b

    def __iter__(self) -> "RangeRestartIterator":
        """Ritorna ogni volta un nuovo iteratore indipendente."""
        return RangeRestartIterator(self._a, self._b)


class RangeRestartIterator:
    """Iteratore su [a, b) che avanza di 1 e termina con StopIteration."""

    def __init__(self, a: int, b: int) -> None:
        self._cur = a
        self._stop = b

    def __iter__(self) -> "RangeRestartIterator":
        return self

    def __next__(self) -> int:
        if self._cur >= self._stop:
            raise StopIteration
        val = self._cur
        self._cur += 1
        return val


# ------------------ Esercizio 3 ------------------
class SequenceView:
    """Vista su una stringa con __iter__ (avanti) e __reversed__ (indietro)."""

    def __init__(self, seq: str):
        self._seq = seq

    def __iter__(self) -> "Forward":
        """Nuovo iteratore in avanti sui caratteri."""
        return Forward(self)

    def __reversed__(self) -> "Backward":
        """Nuovo iteratore all'indietro sui caratteri."""
        return Backward(self)


class Forward:
    """Iteratore in avanti su SequenceView."""

    def __init__(self, view: SequenceView) -> None:
        self._seq = view._seq
        self._i = 0

    def __iter__(self) -> "Forward":
        return self

    def __next__(self) -> str:
        if self._i >= len(self._seq):
            raise StopIteration
        ch = self._seq[self._i]
        self._i += 1
        return ch


class Backward:
    """Iteratore all'indietro su SequenceView."""

    def __init__(self, view: SequenceView) -> None:
        self._seq = view._seq
        self._i = len(self._seq) - 1

    def __iter__(self) -> "Backward":
        return self

    def __next__(self) -> str:
        if self._i < 0:
            raise StopIteration
        ch = self._seq[self._i]
        self._i -= 1
        return ch


# ------------------ Esercizio 4 ------------------
class Bag:
    """Multiset semplice di stringhe con iteratore fail-fast su modifica."""

    def __init__(self) -> None:
        self._counts: Dict[str, int] = {}
        self._modcount: int = 0

    def add(self, s: str) -> None:
        """Aggiunge una occorrenza e aggiorna il contatore di versione."""
        self._counts[s] = self._counts.get(s, 0) + 1
        self._modcount += 1

    def remove_one(self, s: str) -> None:
        """Rimuove una occorrenza; KeyError se assente. Aggiorna versione."""
        if s not in self._counts:
            raise KeyError(s)
        if self._counts[s] == 1:
            del self._counts[s]
        else:
            self._counts[s] -= 1
        self._modcount += 1

    def __len__(self) -> int:
        return sum(self._counts.values())

    @property
    def modcount(self) -> int:
        """Contatore di versione interno usato per il fail-fast."""
        return self._modcount

    def __iter__(self) -> "BagIterator":
        """Ritorna un iteratore che verifica le modifiche ad ogni __next__."""
        return BagIterator(self)


class BagIterator:
    """Iteratore fail-fast su Bag, basato su snapshot (item, count) iniziale."""

    def __init__(self, bag: Bag) -> None:
        self._bag = bag
        self._snapshot: List[Tuple[str, int]] = list(bag._counts.items())
        self._outer_i = 0
        self._inner_left = self._snapshot[0][1] if self._snapshot else 0
        self._version = bag.modcount

    def _check_mod(self) -> None:
        if self._bag.modcount != self._version:
            raise RuntimeError("modified during iteration")

    def __iter__(self) -> "BagIterator":
        return self

    def __next__(self) -> str:
        self._check_mod()
        if self._outer_i >= len(self._snapshot):
            raise StopIteration

        item, count = self._snapshot[self._outer_i]
        if self._inner_left <= 0:
            self._outer_i += 1
            if self._outer_i >= len(self._snapshot):
                raise StopIteration
            item, count = self._snapshot[self._outer_i]
            self._inner_left = count

        self._inner_left -= 1
        return item


# ------------------ Esercizio 5 ------------------
class RoundRobin(Generic[T]):
    """Aggregatore che alterna elementi da iterabili (anche di lunghezze diverse)."""

    def __init__(self, *iterables: Iterable[T]) -> None:
        self._iterables = iterables

    def __iter__(self) -> "RoundRobinIterator[T]":
        """Ritorna un nuovo iteratore round-robin indipendente."""
        return RoundRobinIterator(self._iterables)


class RoundRobinIterator(Iterator[T], Generic[T]):
    """Iteratore che alterna elementi tra più iterabili, saltando quelli esauriti."""

    def __init__(self, iterables: Tuple[Iterable[T], ...]) -> None:
        self._iters: List[Iterator[T]] = [iter(it) for it in iterables]
        self._idx: int = 0

    def __iter__(self) -> "RoundRobinIterator[T]":
        return self

    def __next__(self) -> T:
        if not self._iters:
            raise StopIteration

        while True:
            try:
                value = next(self._iters[self._idx])
                self._idx = (self._idx + 1) % len(self._iters)
                return value
            except StopIteration:
                del self._iters[self._idx]
                if not self._iters:
                    raise StopIteration
                if self._idx >= len(self._iters):
                    self._idx = 0


# ------------------ Esercizio 6 (bonus) ------------------
class Windowed:
    """Aggregatore che emette finestre sovrapposte (substring) di lunghezza k."""

    def __init__(self, seq: str, k: int) -> None:
        if k <= 0:
            raise ValueError("k must be > 0")
        self._seq = seq
        self._k = k

    def __iter__(self) -> "WindowedIterator":
        """Nuovo iteratore che usa soli indici (nessuna list globale)."""
        return WindowedIterator(self._seq, self._k)


class WindowedIterator:
    """Iteratore che produce finestre di lunghezza fissa spostate di 1."""

    def __init__(self, seq: str, k: int) -> None:
        self._seq = seq
        self._k = k
        self._i = 0
        self._limit = max(0, len(seq) - k + 1)

    def __iter__(self) -> "WindowedIterator":
        return self

    def __next__(self) -> str:
        if self._i >= self._limit:
            raise StopIteration
        start = self._i
        end = start + self._k
        self._i += 1
        return self._seq[start:end]


# ------------------ Test minimi ------------------
def _run_tests() -> None:
    # Esercizio 1–2: RangeRestart e due iteratori indipendenti
    r = RangeRestart(2, 5)
    assert list(iter(r)) == [2, 3, 4]
    it1 = iter(r); it2 = iter(r)
    assert next(it1) == 2
    assert next(it1) == 3
    assert next(it2) == 2
    assert list(it1) == [4]
    try:
        next(it1)
        assert False, "Expected StopIteration"
    except StopIteration:
        pass

    r2 = RangeRestart(0, 4)
    a, b = iter(r2), iter(r2)
    # avanzamento a scacchiera per dimostrare indipendenza
    assert next(a) == 0
    assert next(b) == 0
    assert next(a) == 1
    assert next(b) == 1
    assert list(a) == [2, 3]
    assert list(b) == [2, 3]

    # Esercizio 3: SequenceView
    sv = SequenceView("ABCD")
    assert "".join(iter(sv)) == "ABCD"
    assert "".join(reversed(sv)) == "DCBA"

    # Esercizio 4: Bag fail-fast
    bag = Bag()
    bag.add("apple"); bag.add("banana"); bag.add("apple")
    it = iter(bag)
    assert next(it) in {"apple", "banana"}
    bag.add("cherry")
    try:
        next(it)
        assert False, "Expected RuntimeError on modification"
    except RuntimeError as e:
        assert str(e) == "modified during iteration"

    # Esercizio 5: RoundRobin
    rr = RoundRobin([1, 2], (10, 20, 30), "ab")
    assert list(iter(rr)) == [1, 10, "a", 2, 20, "b", 30]

    # Esercizio 6: Windowed
    w = Windowed("ABCDE", 3)
    assert list(iter(w)) == ["ABC", "BCD", "CDE"]
    assert list(Windowed("AB", 3)) == []

    print("All tests passed ✅")


if __name__ == "__main__":
    _run_tests()
