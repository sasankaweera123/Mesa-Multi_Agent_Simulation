from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

from model import GameModel
from mesa.visualization.modules import CanvasGrid


def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "r": 0.5}
    if agent.power > 0:
        portrayal["Color"] = "red"
        portrayal["Layer"] = 0
    else:
        portrayal["Color"] = "blue"
        portrayal["Layer"] = 1
        portrayal["r"] = 0.2
    return portrayal


grid = CanvasGrid(agent_portrayal, 50, 50, 500, 500)
server = ModularServer(GameModel, [grid], "Game Model", {"height": 50, "width": 50, "num_agents": 30})
server.port = 8521  # The default
server.launch()
