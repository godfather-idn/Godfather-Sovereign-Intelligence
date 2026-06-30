from abc import ABC, abstractmethod
from datetime import datetime


class BaseAgent(ABC):
    """
    Base class for all Sovereign AI Agents.
    """

    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization
        self.status = "Active"
        self.created_at = datetime.utcnow()

    @abstractmethod
    def handle_task(self, task):
        """
        Every agent must implement this method.
        """
        pass

    def get_info(self):
        return {
            "name": self.name,
            "specialization": self.specialization,
            "status": self.status,
            "created_at": self.created_at.isoformat()
        }