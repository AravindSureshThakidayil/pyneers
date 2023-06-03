"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc
import time
docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"



class State(pc.State):
    problem=[[0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0.]]
    a01: int 
    """The app state."""
    def func(self):
        pass
    def start_timer(self):
        t=time.time()
        return t
    def set_problem(self):
        


        pass
                

    

def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.heading("Sudoku solver", font_size="50px"),
            pc.hstack(
        pc.text("Enter Your Problem",font_size="30px"),
        pc.button("Start",color="green"),
        pc.button("Submit",color="grey",on_click=State.func()),
       padding_top="5%"
    ),
    pc.hstack(
pc.input(id='00',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='01',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='02',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='03',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='04',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='05',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='06',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='07',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='08',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
),
pc.hstack(
pc.input(id='10',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='11',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='12',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='13',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='14',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='15',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='16',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='17',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='18',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
),
pc.hstack(
pc.input(id='20',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='21',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='22',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='23',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='24',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='25',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='26',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='27',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='28',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
),
pc.hstack(
pc.input(id='30',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='31',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='32',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='33',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='34',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='35',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='36',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='37',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='38',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
),
pc.hstack(
pc.input(id='40',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='41',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='42',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='43',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='44',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='45',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='46',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='47',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='48',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
),
pc.hstack(
pc.input(id='50',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='51',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='52',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='53',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='54',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='55',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='56',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='57',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='58',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
),
pc.hstack(
pc.input(id='60',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='61',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='62',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='63',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='64',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='65',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='66',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='67',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='68',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
),
pc.hstack(
pc.input(id='70',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='71',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='72',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='73',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='74',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='75',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='76',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='77',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='78',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
),
pc.hstack(
pc.input(id='80',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='81',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='82',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='83',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='84',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='85',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='86',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='87',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
pc.input(id='88',width='50px',height='50px',defaut_value=0,border="1px#808080 solid"),
)
    
,padding="2%"    
    ))

# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)

app.compile()