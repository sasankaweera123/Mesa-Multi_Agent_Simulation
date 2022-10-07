from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter

from model import GameModel
from mesa.visualization.modules import CanvasGrid, ChartModule

NUMBER_OF_CELLS = 20

SIZE_OF_CANVAS_IN_PIXELS_X = 500
SIZE_OF_CANVAS_IN_PIXELS_Y = 500


simulation_prams = {
    "number_of_agents": UserSettableParameter("slider",
                                              "Number of agents",
                                              50,  # default value
                                              5,  # min value
                                              100,  # max value
                                              1,  # step
                                              description="Choose how many agents to include in the model"),
    "width": NUMBER_OF_CELLS,
    "height": NUMBER_OF_CELLS

}


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


grid = CanvasGrid(agent_portrayal, NUMBER_OF_CELLS, NUMBER_OF_CELLS, SIZE_OF_CANVAS_IN_PIXELS_X, SIZE_OF_CANVAS_IN_PIXELS_Y)
AgentChart = ChartModule([
    {"Label": "High Power Agents", "Color": "red"},
    {"Label": "Low Power Agents", "Color": "green"},
    {"Label": "Died Agents", "Color": "blue"},
],
    canvas_height=150, data_collector_name="AgentDataCollector")

server = ModularServer(GameModel, [grid,AgentChart], "Game Model", simulation_prams)
server.port = 8521  # The default
server.launch()
