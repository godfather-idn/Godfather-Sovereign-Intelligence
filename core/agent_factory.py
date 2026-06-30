from core.agent_registry import AgentRegistry


class AgentFactory:

    @staticmethod
    def create(agent_name: str):
        
        agent_class = AgentRegistry.get(agent_name)
        
        if agent_class is None:
            return None

        return agent_class()