from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

from model import GameModel
from mesa.visualization.modules import CanvasGrid


def agent_portrayal(agent):
    portrayal = {"Filled": "true",
                 }
    if agent.power > 5:
        portrayal["Shape"] = "circle"
        portrayal["Color"] = "green"
        portrayal["Layer"] = 0
        portrayal["r"] = 0.5
    elif agent.power > 0:
        portrayal["Shape"] = "circle"
        portrayal["Color"] = "red"
        portrayal["Layer"] = 1
        portrayal["r"] = 0.5
    else:
        portrayal["Shape"] = "rect"
        portrayal["Color"] = "blue"
        portrayal["Layer"] = 1
        portrayal["w"] = 1
        portrayal["h"] = 1
    return portrayal


grid = CanvasGrid(agent_portrayal, 20, 20, 500, 500)
server = ModularServer(GameModel, [grid], "Game Model", {"height": 20, "width": 20, "num_agents": 100})
server.port = 8521  # The default
server.launch()
