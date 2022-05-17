import pandas as p

worlds = p.read_csv("lol_worlds_2021_play_in.csv")

allPositionsName = list(dict.fromkeys(worlds["Position"]))
allChampionsName = list(dict.fromkeys(worlds["Champion"]))
allTeamsName = list(dict.fromkeys(worlds["Team"]))
allPlayersName = list(dict.fromkeys(worlds["Player"]))

class Dataset:
  datasetType = "Dataset"
  
  winrate = 0
  kda = 0
  creepScore = 0
  wardInteractions = 0

  otherWinrate = 0
  otherCreepScore = 0
  otherKda = 0
  otherWardInteractions = 0

  def __init__(self, name, position="", versus="", datasetType="Champion") -> None:
    self.datasetType = datasetType
    self.name = name
    self.position = position
    self.versus = versus
    self.loadDataset()
    self.setWinRate()
    self.setKillDeathAssistAverage()
    self.setOtherKillDeathAssistAverage()
    self.setOtherWinRate()
    self.setCreepScore()
    self.setWardInteraction()

  def loadDataset(self) -> None:
    self.initialDataset = worlds[worlds[self.datasetType] == self.name]
    if(self.position != ""):
      datasetPosition = worlds[worlds["Position"] == self.position]
      self.dataset = datasetPosition[datasetPosition[self.datasetType] == self.name]
      if(self.versus != ""):
        self.otherDataset = datasetPosition[datasetPosition[self.datasetType] == self.versus]
      else:
        self.otherDataset = datasetPosition[datasetPosition[self.datasetType] != self.name]
    else:
      self.dataset = worlds[worlds[self.datasetType] == self.name]
      if(self.versus != ""):
        self.otherDataset = worlds[worlds[self.datasetType] == self.versus]
      else:
        self.otherDataset = worlds[worlds[self.datasetType] != self.name]
    self.nbGames = len(self.dataset)
    self.otherNbGames = len(self.otherDataset)

  def setWinRate(self) -> None:
    winGames = len(self.dataset[self.dataset["Result"] == "W"])
    if(self.nbGames != 0):
      self.winrate = winGames / self.nbGames

  def setKillDeathAssistAverage(self) -> None:
    kill = self.dataset[["Kills"]].mean()
    death = self.dataset[["Deaths"]].mean()
    assist = self.dataset[["Assists"]].mean()
    if(self.nbGames != 0):
      self.kda = (float(kill) + float(assist)) / float(death)

  def setOtherKillDeathAssistAverage(self) -> None:
    kill = self.otherDataset[["Kills"]].mean()
    death = self.otherDataset[["Deaths"]].mean()
    assist = self.otherDataset[["Assists"]].mean()
    if(self.otherNbGames != 0):
      self.otherKda = (float(kill) + float(assist)) / float(death)

  def setOtherWinRate(self) -> None:
    winGames = len(self.otherDataset[self.otherDataset["Result"] == "W"])
    if(self.otherNbGames != 0):
      self.otherWinrate = winGames / self.otherNbGames

  def setCreepScore(self) -> None:
    if(self.nbGames != 0):
      self.creepScore = float(self.dataset[["Creep Score"]].mean())
    if(self.otherNbGames != 0):
      self.otherCreepScore = float(self.otherDataset[["Creep Score"]].mean())

  def setWardInteraction(self) -> None:
    if(self.nbGames != 0):
      self.wardInteractions = float(self.dataset[["Ward Interactions"]].mean())
    if(self.otherNbGames != 0):
      self.otherWardInteractions = float(self.otherDataset[["Ward Interactions"]].mean())
  

  def getFrequenceOfDataset(self, needles):
    freq = {}
    for item in self.initialDataset[needles]:
      if (item in freq):
        freq[item] += 1
      else:
        freq[item] = 1
    return freq

  def printAttributes(self):
    versus = "Others"
    if(self.versus != ""):
      versus = self.versus

    print("\n\n",self.datasetType)
    
    print("\n" + self.name + " { // games => ", self.nbGames)
    print("  kda:               ", self.kda)
    print("  creep score:       ", self.creepScore)
    print("  ward interaction:  ", self.wardInteractions)
    print("  winrate:           ", self.winrate)
    print("}")
    
    print("\n ", versus ," { // games => ", self.otherNbGames)
    print("  kda:               ", self.otherKda)
    print("  creep score:       ", self.otherCreepScore)
    print("  ward interaction:  ", self.otherWardInteractions)
    print("  winrate:           ", self.otherWinrate)
    print("}")
