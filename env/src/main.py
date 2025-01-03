from phi.agent import Agent 

from phi.agent import Agent
from phi.model.groq import Groq
import os

API_KEY = os.getenv("GROQ_API_KEY")

print("Tell me the topic of the essay you want to write")
topic = input()
print("Tell me the length of the essay you want to write in words")
length = input()


query_essay=("Write an essay on the topic '"+topic+"' in "+length+" words")

essay_writting_agent = Agent(
    # Add functions or Toolkits
    name = "Essay Writting Agent",
    role = "Provide essay writting services",
    model=Groq(id="llama-3.1-8b-instant"),

    
    instructions=["Give the essay in {length} words for given {topic} with this format 1.Introduction 2.Body 3.Conclusion"],
    # Show tool calls in the Agent response
    show_tool_calls=True
)


essay_writting_agent.print_response(query)





poem_writting_agent = Agent(
    name = "Poem Writting Agent",
    role = "Provide poem writting services",
    model=Groq(id="llama-3.1-8b-instant"),
    instructions=["Generate a poem of 15-20 lines","Follow rhyme scheme ABAB CDCD EFEF GG"], 
)
#poem_writting_agent.print_response("Write a poem on the topic 'Nature'")


agent_team=Agent(
    team=[essay_writting_agent,poem_writting_agent],
    


)