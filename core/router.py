import json
from pathlib import Path


class AgentRouter:
    def __init__(self, registry_path="core/registry.json"):
        registry_file = Path(registry_path)

        with open(registry_file, "r", encoding="utf-8") as f:
            self.registry = json.load(f)

    def find_agent(self, user_prompt: str):
        prompt = user_prompt.lower()

        best_agent = None
        highest_score = 0

        for agent in self.registry["agents"]:
            score = 0

            for keyword in agent["specialization"]:
                if keyword.lower() in prompt:
                    score += 1

            if score > highest_score:
                highest_score = score
                best_agent = agent

        return best_agent
    
    def find_agents(self, user_prompt: str):

        prompt = user_prompt.lower()

        matched_agents = []

        for agent in self.registry["agents"]:

            score = 0

            for keyword in agent["specialization"]:

                if keyword.lower() in prompt:
                    score += 1

            if score > 0:
                matched_agents.append({
                    "score": score,
                    "agent": agent
                })

        matched_agents.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return [item["agent"] for item in matched_agents]

if __name__ == "__main__":

    router = AgentRouter()

    while True:

        prompt = input("\nUser > ")

        if prompt.lower() == "exit":
            break

        agent = router.find_agent(prompt)

        if agent:
            print(f"\nSelected Agent : {agent['name']}")
            print(f"Harness        : {agent['harness']}")
            print(f"Keywords       : {agent['specialization']}")
        else:
            print("\nNo suitable agent found.")