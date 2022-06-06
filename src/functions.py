import matplotlib.pyplot as plt
import numpy as np
from collections import Counter, OrderedDict

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
  fig, ax = plt.subplots(figsize=(5,3))
  ax.bar(x_pos, height, color=colors)

  # Create names on the x-axis
  plt.xticks(x_pos, bars)
  plt.xlabel(datasetType)
  labels = getLabels(dataTypeNeed)
  plt.ylabel(labels[1])
  plt.title(labels[0] + datasetType)

  return fig

def printBar(items, datasetType="Champion"):
  fig = plt.figure(figsize=(6, 3), dpi=200)
  x = Counter(items)
  itemsSorted = OrderedDict(x.most_common(5))

  ax = fig.add_axes([0,0,1,1])
  
  ax.bar(itemsSorted.keys(), itemsSorted.values(), color="blue")

  title = "team having played the most this champion"
  if(datasetType == "Team"):
    title = "the most played champions by this team"
  if(datasetType == "Player"):
    title = "most played champions by this player"
  plt.title(title)

  plt.yticks(np.arange(0, max(itemsSorted.values()) + 1, 1))
  return fig

