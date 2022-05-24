import matplotlib.pyplot as plt
import numpy as np

def getLabels(typeData="kda"):
  # title, x label, y label
  if(typeData == "kda"):
    return ["Kda Moyen/", "Kda"]
  elif(typeData == "creep"):
    return ["Creep Moyen/", "Creep score"]
  elif(typeData == "gold"):
    return ["Gold Moyen/", "Gold score"]
  else:
    return ["Vision Interaction Moyen/", "Vision interaction"]

def printBarPlot(height, bars, datasetType="Champion", dataTypeNeed="kda"):
  # create a dataset
  # height = [3, 12]
  # bars = ('A', 'B')
  x_pos = np.arange(len(bars))

  colors = ['blue', 'red']

  # Create bars with different colors
  fig, ax = plt.subplots()
  ax.bar(x_pos, height, color=colors)

  # Create names on the x-axis
  plt.xticks(x_pos, bars)
  plt.xlabel(datasetType)
  labels = getLabels(dataTypeNeed)
  plt.ylabel(labels[1])
  plt.title(labels[0] + datasetType)

  return fig