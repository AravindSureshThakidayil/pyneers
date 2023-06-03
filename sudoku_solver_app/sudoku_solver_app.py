"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc
import time
docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"



class State(pc.State):
    """The app state."""
    def func(self):
        pass
    def start_timer(self):
        t=time.time()
        return t
    

# listx = []
# for i in range(9):
#         listn = []
#         for j in range(9):
#             listn.append(pc.text_area(id = f"{i}{j}"))
#         listx.append(listn)
    
        # tuplex1 = tuple(listn[0])
        # tuplex2 = tuple(listn[1])
        # tuplex3 = tuple(listn[2])
        # tuplex4 = tuple(listn[3])
        # tuplex5 = tuple(listn[4])
        # tuplex6 = tuple(listn[5])
        # tuplex7 = tuple(listn[6])
        # tuplex8 = tuple(listn[7])
        # tuplex9 = tuple(listn[8])

def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.heading("Sudoku solver", font_size="50px"),
            pc.hstack(
        pc.text("Enter Your Problem",font_size="30px"),
        pc.button("Start",color="green"),
        pc.button("Submit",color="grey",on_click=State.func()),


        padding_top="5%")
    )
    )

# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)

app.compile()