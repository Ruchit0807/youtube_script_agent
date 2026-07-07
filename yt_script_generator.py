import os
from typing import TypedDict

#letys create state first

class pipelinestate(TypedDict):
    raw_input : str
    edited_text : str
    script_text : str
    final_output : str

from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)

def editor_node(state : pipelinestate) -> dict:
    """Stage 1: Cleans up grammer, removes typos, and refines the tone"""

    prompt = (
        "Your are expert copyeditor, Clean up the following raw text."
        "Fix my grammatical errors, spelling mistakes, and smooth out the transitional flow"
        "While keeping the core message intact. Return only the edited text. \n\n"
        f"Text:\n{state['raw_input']}"
    )

    response = llm.invoke(prompt)
    return {"edited_text" : response.content.strip()}

def scriptwriter_node(state : pipelinestate) -> dict:
    """Stage 2: Formats the clean text into an engaging video script style."""
    print("\n--- [Stage 2] Executing Scriptwriter node ---")

    prompt = (
        "You are a charismatic YouTube content creator, Take this edited edited text and transform"
        "it into highly engaging, punchy, conversational video script hook. Make it souds good"
        "Like a real person speaking passionately, Return only the script content. \n\n"
        f"Edited Text:\n{state['edited_text']}"
    )

    response = llm.invoke(prompt)
    return {"script_text": response.content.strip()}



def translator_node(state : pipelinestate) -> dict:
    """Stage 4: Translates the script into natural flowing Hinglish."""
    print("\n--- [Stage 3] Executing Hinglish transltor node ---")


    prompt = (
        "You are a charismatic YouTube content creator, Take this edited edited text and transform"
        "it into highly engaging, punchy, conversational video script hook. Make it souds good"
        "Like a real person speaking passionately, Return only the script content. \n\n"
        f"Script:\n{state['script_text']}"
    )

    response = llm.invoke(prompt)
    return {"final_output": response.content.strip()}

#now your state and nodes are ready and now it is time to create the graph.
#for creating the graph you have to conncect these nodes for that you have to need edges
#to use the edges

from langgraph.graph import StateGraph, START, END

#create the graph
graph = StateGraph(pipelinestate)

#adding nodes in our graph
graph.add_node("editor", editor_node)
graph.add_node("scriptwriter", scriptwriter_node)
graph.add_node("translator", translator_node)


#Add edges (sequential one after another)

graph.add_edge(START, "editor")
graph.add_edge('editor', "scriptwriter")
graph.add_edge('scriptwriter', "translator")
graph.add_edge('translator', END)


#compile the graph
app = graph.compile()

result = app.invoke({

    "raw_input" : "AI agents are the future of tech. they can think, plan, and act on their tasks"
})

#output 
print("your results are : --- \n\n")
print(result['final_output'])






