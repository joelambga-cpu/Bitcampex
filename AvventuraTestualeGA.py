from __future__ import annotations
from typing import Dict, Optional, List


# ============================================================
# MEMENTO
# ============================================================

class GameMemento:
    def __init__(self, state: Dict):
        self._state = state

    def get_state(self) -> Dict:
        return self._state.copy()


# ============================================================
# ORIGINATOR (Game)
# ============================================================

class Game:
    def __init__(self):
        self.location: str = "Inizio"
        self.health: int = 100
        self.inventory: List[str] = []
        self.quest_progress: Dict[str, str] = {}

    def create_memento(self, full: bool = True) -> GameMemento:
        """Crea uno snapshot dello stato del gioco."""

        if full:
            state = {
                "location": self.location,
                "health": self.health,
                "inventory": list(self.inventory),
                "quest_progress": dict(self.quest_progress),
            }
        else:
            state = {
                "location": self.location,
                "quest_progress": dict(self.quest_progress)
            }

        return GameMemento(state)

    def restore(self, memento: GameMemento) -> None:
        """Ripristina solo i campi presenti nel memento."""
        state = memento.get_state()

        if "location" in state:
            self.location = state["location"]

        if "health" in state:
            self.health = state["health"]

        if "inventory" in state:
            self.inventory = list(state["inventory"])

        if "quest_progress" in state:
            self.quest_progress = dict(state["quest_progress"])

    def __str__(self):
        return (
            f"=== STATO ATTUALE ===\n"
            f"Location: {self.location}\n"
            f"Health: {self.health}\n"
            f"Inventory: {self.inventory}\n"
            f"Quest: {self.quest_progress}\n"
        )


# ============================================================
# CARETAKER
# ============================================================

class GameCaretaker:
    def __init__(self):
        self._branches: Dict[str, List[GameMemento]] = {}

    def save_memento(self, branch: str, memento: GameMemento):
        if branch not in self._branches:
            self._branches[branch] = []
        self._branches[branch].append(memento)

    def get_memento(self, branch: str, index: int = -1) -> Optional[GameMemento]:
        if branch not in self._branches:
            return None
        if not self._branches[branch]:
            return None
        return self._branches[branch][index]

    def pop_memento(self, branch: str) -> Optional[GameMemento]:
        if branch not in self._branches or not self._branches[branch]:
            return None
        return self._branches[branch].pop()

    def list_branches(self):
        return {b: len(v) for b, v in self._branches.items()}


# ============================================================
# MAIN DI TEST — FUNZIONA GARANTITO
# ============================================================

def main():
    game = Game()
    caretaker = GameCaretaker()

    print(game)

    # MODIFICA STATO
    game.location = "Foresta"
    game.health = 80
    game.inventory = ["Spada", "Pozione"]
    game.quest_progress = {"Tutorial": "completato", "Re": "in_corso"}

    print(">>> Salvataggio full su PercorsoBuono")
    caretaker.save_memento("PercorsoBuono", game.create_memento(full=True))

    # CAMBIA QUALCOSA
    game.location = "Villaggio"
    game.quest_progress["Re"] = "fallito"

    print(">>> Salvataggio parziale su PercorsoBuono")
    caretaker.save_memento("PercorsoBuono", game.create_memento(full=False))

    # ALTRO BRANCH
    game.location = "Castello Oscuro"
    game.health = 10
    game.inventory.append("Chiave Maledetta")

    print(">>> Salvataggio full su PercorsoMalvagio")
    caretaker.save_memento("PercorsoMalvagio", game.create_memento(full=True))

    print("\nBRANCHES:", caretaker.list_branches(), "\n")

    # RESTORE PARZIALE
    print(">>> Restore parziale dal PercorsoBuono")
    m1 = caretaker.get_memento("PercorsoBuono", -1)
    game.restore(m1)
    print(game)

    # RESTORE COMPLETO
    print(">>> Restore completo dal PercorsoMalvagio")
    m2 = caretaker.get_memento("PercorsoMalvagio", -1)
    game.restore(m2)
    print(game)

    # UNDO
    print(">>> Undo su PercorsoBuono")
    caretaker.pop_memento("PercorsoBuono")
    undo_m = caretaker.get_memento("PercorsoBuono", -1)
    game.restore(undo_m)
    print(game)


# ============================================================
# ENTRY POINT CORRETTO
# ============================================================

if __name__ == "__main__":
    main()
