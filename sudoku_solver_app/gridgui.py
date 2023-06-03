import pynecone as pc
class TextareaState(pc.State):
    text: str = "Hello World!"

listx = []

for i in range(9):
    listn = []
    for j in range(9):
        listn.append(pc.text_area(id = f"{j}{i}"))
    listx.append(listn)
    
    tuplex1 = tuple(listn[0])
    tuplex2 = tuple(listn[1])
    tuplex3 = tuple(listn[2])
    tuplex4 = tuple(listn[3])
    tuplex5 = tuple(listn[4])
    tuplex6 = tuple(listn[5])
    tuplex7 = tuple(listn[6])
    tuplex8 = tuple(listn[7])
    tuplex9 = tuple(listn[8])

def table():
    return pc.vstack(
        *listn)