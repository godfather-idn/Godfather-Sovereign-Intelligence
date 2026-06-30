from agents.godfather_defi.agent import GodfatherDeFi
from agents.ritual_sentinel.agent import RitualSentinel


class AgentRegistry:

    _agents = {
        "Godfather DeFi": GodfatherDeFi,
        "Ritual Sentinel": RitualSentinel,
    }

    @classmethod
    def get(cls, agent_name):
        return cls._agents.get(agent_name)

    @classmethod
    def register(cls, agent_name, agent_class):
        cls._agents[agent_name] = agent_class

    @classmethod
    def list_agents(cls):
        return list(cls._agents.keys())