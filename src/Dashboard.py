import streamlit as st
from Dataset import Dataset, allPlayersName, allChampionsName, allPositionsName, allTeamsName
from functions import printBarPlot

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
st.set_option('deprecation.showPyplotGlobalUse', False)


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

colChampLeft, colChampRight = st.columns([1,1])
with colChampLeft:
  optionMe = st.selectbox(optionType, TYPE[optionType], key="optionSelected", on_change=onChangeSelected)
with colChampRight:
  optionPosition = st.selectbox(optionType+" versus", ["All"] + TYPE[optionType], key="optionVersus", on_change=onChangeVersus)


col1, col2, col3, col4 = st.columns([1, 1, 2, 2])
with col1:
  st.markdown('<h2 style="text-align: center;">N°Games</h2>', unsafe_allow_html=True)
  st.markdown('<h4 style="color: #007FFF;text-align: center;">'+ str(st.session_state.dataset.nbGames) +'</h4>', unsafe_allow_html=True)
  st.markdown('<h4 style="color: #FF003F;text-align: center;">'+ str(st.session_state.dataset.otherNbGames) +'</h4>', unsafe_allow_html=True)

with col2:
  st.markdown('<h2 style="text-align: center;">Winrate</h2>', unsafe_allow_html=True)
  st.markdown('<h4 style="color: #007FFF;text-align: center;">'+ str(int(st.session_state.dataset.winrate * 100)) +'%</h4>', unsafe_allow_html=True)
  st.markdown('<h4 style="color: #FF003F;text-align: center;">'+ str(int(st.session_state.dataset.otherWinrate * 100)) +'%</h4>', unsafe_allow_html=True)

with col3:
  st.markdown('<h2 style="text-align: center;">Kda</h2>', unsafe_allow_html=True)
  st.pyplot(printBarPlot([st.session_state.dataset.kda, st.session_state.dataset.otherKda], [st.session_state.dataset.name, "others" if st.session_state.dataset.versus == "" else st.session_state.dataset.versus], st.session_state.dataset.datasetType, "kda"))

with col4:
  st.markdown('<h2 style="text-align: center;">Gold</h2>', unsafe_allow_html=True)
  st.pyplot(printBarPlot([st.session_state.dataset.golds, st.session_state.dataset.otherGolds], [st.session_state.dataset.name, "others" if st.session_state.dataset.versus == "" else st.session_state.dataset.versus], st.session_state.dataset.datasetType, "gold"))

col5, col6, col7 = st.columns([2, 1, 1])
with col6:  
  st.markdown('<h2 style="text-align: center;">Creep Score</h2>', unsafe_allow_html=True)
  st.pyplot(printBarPlot([st.session_state.dataset.creepScore, st.session_state.dataset.otherCreepScore], [st.session_state.dataset.name, "others" if st.session_state.dataset.versus == "" else st.session_state.dataset.versus], st.session_state.dataset.datasetType, "creep"))

with col7:
  st.markdown('<h2 style="text-align: center;">Ward Interactions</h2>', unsafe_allow_html=True)
  st.pyplot(printBarPlot([st.session_state.dataset.wardInteractions, st.session_state.dataset.otherWardInteractions], [st.session_state.dataset.name, "others" if st.session_state.dataset.versus == "" else st.session_state.dataset.versus], st.session_state.dataset.datasetType, "vision"))


# st.text("Type : " + st.session_state.dataset.datasetType)
# st.text("Position : " + (st.session_state.dataset.position if st.session_state.dataset.position != "" else "All"))
# st.text("\n----------------\n\nSelected : " +st.session_state.dataset.name)
# st.text("Kda : " + str(st.session_state.dataset.kda))
# st.text("Winrate : " + str(st.session_state.dataset.winrate))

# st.text("\n----------------\n\nVersus : " + (st.session_state.dataset.versus if st.session_state.dataset.versus != "" else "All"))
# st.text("kda : " + str(st.session_state.dataset.otherKda))
# st.text("nb games : " + str(st.session_state.dataset.otherNbGames))
# st.text("winrate : " + str(st.session_state.dataset.otherWinrate))
