from mesa import Model
from agent import GameAgent
from mesa.space import MultiGrid
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector


class GameModel(Model):
    def __init__(self, height, width, number_of_agents):
        self.n_agents = number_of_agents
        self.grid = MultiGrid(height, width, True)
        self.schedule = RandomActivation(self)
        self.running = True

        self.AgentDataCollector = DataCollector(
            {
                "High Power Agents": GameModel.get_high_power_agents,
                "Low Power Agents": GameModel.get_low_power_agents,
                "Died Agents": GameModel.get_died_agents,
            }
        )

        # Agent Creation
        for i in range(self.n_agents):
            a = GameAgent(i, self)
            self.schedule.add(a)

            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))
        # for i in range()

    def step(self):
        self.schedule.step()
        self.AgentDataCollector.collect(self)

    @staticmethod
    def get_high_power_agents(model) -> list[int]:
        return [1 for agent in model.schedule.agents if agent.power > 5]

    @staticmethod
    def get_low_power_agents(model) -> list[int]:
        return [1 for agent in model.schedule.agents if agent.power > 0 & agent.power < 5]

    @staticmethod
    def get_died_agents(model) -> list[int]:
        return [1 for agent in model.schedule.agents if agent.power == 0]
