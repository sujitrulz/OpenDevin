from dataclasses import dataclass

from opendevin.schema import ObservationType

from .base import Observation


@dataclass
class UserMessageObservation(Observation):
    """
    This data class represents a message sent by the user.
    """

    role: str = 'user'
    observation: str = ObservationType.MESSAGE

    @property
    def message(self) -> str:
        return ''


@dataclass
class AgentMessageObservation(Observation):
    """
    This data class represents a message sent by the agent.
    """

    role: str = 'assistant'
    observation: str = ObservationType.MESSAGE

    @property
    def message(self) -> str:
        return ''
