from agents.godfather_defi.agent import GodfatherDeFi

agent = GodfatherDeFi()

print(agent.get_info())

result = agent.handle_task("Analyze staking opportunities on Ritual")

print(result)