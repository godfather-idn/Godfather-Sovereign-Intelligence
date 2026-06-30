from core.router import AgentRouter
from core.agent_factory import AgentFactory


class GodfatherCoordinator:

    def __init__(self):
        self.router = AgentRouter()

    def process_request(self, user_prompt):

        agents_info = self.router.find_agents(user_prompt)

        if not agents_info:
            return {
                "success": False,
                "message": "No suitable agent found."
            }

        results = []
        selected_agents = []

        for agent_info in agents_info:

            agent = AgentFactory.create(agent_info["name"])

            if agent:

                selected_agents.append(agent_info["name"])

                results.append(
                    agent.handle_task(user_prompt)
                )

        if not results:
            return {
                "success": False,
                "message": "No agent implementations found."
            }

        from core.response_aggregator import ResponseAggregator

        combined_response = ResponseAggregator.combine(results)

        return {
            "success": True,
            "selected_agents": selected_agents,
            "response": combined_response
        }


if __name__ == "__main__":

    coordinator = GodfatherCoordinator()

    print("=" * 50)
    print("Godfather Sovereign Intelligence")
    print("Coordinator v1.0")
    print("Type 'exit' to quit.")
    print("=" * 50)

    while True:

        prompt = input("\nUser > ")

        if prompt.lower() == "exit":
            break

        result = coordinator.process_request(prompt)

        if result["success"]:
            print("\nCoordinator Decision")
            print("---------------------")

            for agent in result["selected_agents"]:
                print(f"- {agent}")

            print("\nAgent Response")
            print("---------------------")
            print(result["response"])

        else:
            print(result["message"])