from agents.ritual_sentinel.agent import RitualSentinel

agent = RitualSentinel()

print(agent.get_info())

print(agent.handle_task("Analyze wallet security"))