from __future__ import annotations

from dataclasses import dataclass
import random
import chess


@dataclass
class AgentConfig:
    seed: int = 0


class ChessAgent:
    name = "UnnamedAgent"

    def __init__(self, config: AgentConfig | None = None):
        self.config = config or AgentConfig()
        self.rng = random.Random(self.config.seed)

    def reset(self) -> None:
        """Reset any per-game state here if needed."""
        return None

    def select_move(self, board: chess.Board, time_budget: float) -> chess.Move:
        raise NotImplementedError
