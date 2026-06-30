from agents.shared.base_agent import BaseAgent


class DummyAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            name="Dummy",
            specialization="Testing"
        )

    def handle_task(self, task):
        return f"Handled: {task}"


agent = DummyAgent()

print(agent.get_info())

print(agent.handle_task("Hello"))