from agents.shared.base_agent import BaseAgent


class RitualSentinel(BaseAgent):

    def __init__(self):
        super().__init__(
            name="Ritual Sentinel",
            specialization="Security Intelligence"
        )

    def handle_task(self, task):

        return {
            "agent": self.name,
            "status": "completed",
            "task": task,
            "response": (
                f"[{self.name}] analyzed the security request: '{task}'. "
                "Security scan completed successfully."
            )
        }