import streamlit as st
import matplotlib.pyplot as plt
from Dataset import Dataset, allPlayersName, allChampionsName, allPositionsName, allTeamsName

POSITIONS = allPositionsName
CHAMPIONS = allChampionsName
TEAMS = allTeamsName
PLAYERS = allPlayersName
TYPE = {
  "Champion": CHAMPIONS,
  "Team": TEAMS,
  "Player": PLAYERS,
}

st.set_page_config(
  page_title="Dashboard League of Legends",
  page_icon="🧊",
  layout="wide",
  initial_sidebar_state="expanded",
)

st.title("Dashboard Worlds 2021")


def initializeDataset():
  st.session_state.dataset = Dataset(
    name=st.session_state.selected,
    datasetType=st.session_state.type,
    position=st.session_state.position,
    versus=st.session_state.versus
  )

if not "initialized" in st.session_state:
  st.session_state.type = list(TYPE.keys())[0]
  st.session_state.selected = CHAMPIONS[0]
  st.session_state.versus = ""
  st.session_state.position = ""
  st.session_state.initialized = True
  initializeDataset()

def onChangeType():
  st.session_state.type = st.session_state.optionType
  st.session_state.selected = TYPE[st.session_state.type][0]
  st.session_state.versus = ""
  initializeDataset()

def onChangePosition():
  st.session_state.position = ""
  if(st.session_state.optionPosition != "All"):
    st.session_state.position = st.session_state.optionPosition
  initializeDataset()

def onChangeSelected():
  st.session_state.selected = st.session_state.optionSelected
  initializeDataset()

def onChangeVersus():
  st.session_state.versus = ""
  if st.session_state.optionVersus != "All":
    st.session_state.versus = st.session_state.optionVersus
  initializeDataset()

colType, colPosition = st.columns([1,1])
with colType:
  optionType = st.selectbox('Select champion, team or player?', TYPE.keys(), key="optionType", on_change=onChangeType)
with colPosition:
  optionPosition = st.selectbox('Select the position', ['All'] + POSITIONS, key="optionPosition", on_change=onChangePosition)

# Col
col1, col2, col3 = st.columns([1, 7, 1])

nbGamesCol, winCol = st.columns([1,1])
with nbGamesCol:
  st.header("N°Games")
with winCol:
  st.header("Win")
with col1:
  optionMe = st.radio(optionType, TYPE[optionType], key="optionSelected", on_change=onChangeSelected)

with col2:
  st.text("Type : " + st.session_state.dataset.datasetType)
  st.text("Position : " + (st.session_state.dataset.position if st.session_state.dataset.position != "" else "All"))
  st.text("\n----------------\n\nSelected : " +st.session_state.dataset.name)
  st.text("Kda : " + str(st.session_state.dataset.kda))
  st.text("nb games : " + str(st.session_state.dataset.nbGames))
  st.text("Winrate : " + str(st.session_state.dataset.winrate))

  st.text("\n----------------\n\nVersus : " + (st.session_state.dataset.versus if st.session_state.dataset.versus != "" else "All"))
  st.text("kda : " + str(st.session_state.dataset.otherKda))
  st.text("nb games : " + str(st.session_state.dataset.otherNbGames))
  st.text("winrate : " + str(st.session_state.dataset.otherWinrate))


  # with nbGamesCol:
  #   nbGamesLeft, nbGamesRight = st.columns([1,1])
    # st.header("N°Games")
  #   with nbGamesLeft:
  #     st.header("5")
  #   with nbGamesRight:
  #     st.header("10")
  
  # with winCol:
  #   winLeft, winRight = st.columns([1,1])
    # st.header("Winrate")
  #   with winLeft:
  #     st.header("40%")
  #   with winRight:
  #     st.header("60%")

  # st.header("A dog")
  # st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
  optionVersus = st.radio(optionType, ["All"] + TYPE[optionType], key="optionVersus", on_change=onChangeVersus)



# with st.sidebar:
#   for x in ["vert", "rouge", "bleu", "yellow"]:
#     if st.button(x):
#       setTitle(x)
#       if x == "bleu":
#         titleEl.empty()

