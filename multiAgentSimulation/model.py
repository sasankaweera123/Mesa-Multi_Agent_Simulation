from mesa import Model
from agent import GameAgent
from mesa.space import MultiGrid
from mesa.time import RandomActivation


class GameModel(Model):
    def __init__(self, height, width, num_agents):
        self.n_agents = num_agents
        self.grid = MultiGrid(height, width, True)
        self.schedule = RandomActivation(self)
        self.running = True

        for i in range(self.n_agents):
            a = GameAgent(i, self)
            self.schedule.add(a)

            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

    def step(self):
        self.schedule.step()
