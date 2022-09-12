from mesa import Agent


class GameAgent(Agent):

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.power = 1

    def step(self) -> None:
        # print("Hi, I am agent " + str(self.unique_id) + ".")
        self.move()
        if self.power > 0:
            self.power_struggle()

        if self.power <= 0:
            self.model.schedule.remove(self)

    def move(self) -> None:
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def power_struggle(self):
        cellmate = self.model.grid.get_cell_list_contents([self.pos])
        if len(cellmate) > 1:
            other = self.random.choice(cellmate)
            other.power -= 1
            self.power += 1
