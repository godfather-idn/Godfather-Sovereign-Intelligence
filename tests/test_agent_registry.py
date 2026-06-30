from core.agent_registry import AgentRegistry

print("Registered Agents:")

for agent in AgentRegistry.list_agents():
    print("-", agent)

print("\nDebug:")

print(AgentRegistry.get("Godfather DeFi"))
print(AgentRegistry.get("Ritual Sentinel"))