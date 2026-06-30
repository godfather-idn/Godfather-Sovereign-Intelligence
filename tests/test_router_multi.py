from core.router import AgentRouter

router = AgentRouter()

agents = router.find_agents(
    "Research Ritual ecosystem and analyze staking security"
)

print("Matched Agents:\n")

for agent in agents:
    print(agent["name"])