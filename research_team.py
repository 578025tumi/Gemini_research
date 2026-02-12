import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import TavilySearchTool

load_dotenv() # This looks for the .env file automatically

# Initialize the search tool
search_tool = TavilySearchTool()

# 1. Define the Researcher Agent
researcher = Agent(
    role='Senior Market Research Analyst',
    goal='Find the most recent and relevant data on {topic}',
    backstory="""You are an expert at navigating the live web. Your 
    specialty is finding news, whitepapers, and technical specs that 
    are less than 6 months old. You provide raw, data-heavy notes.""",
    tools=[search_tool],
    verbose=True, # This lets you see the agent "thinking" in the console
    allow_delegation=False
)

# 2. Define the Research Task
research_task = Task(
    description="""1. Search for the latest 3 breakthroughs in {topic}.
    2. Identify the key companies or researchers involved.
    3. Format the findings into a clear list of facts with source URLs.""",
    expected_output="A bulleted list of research findings and sources.",
    agent=researcher
)

# 1. Define the Writer Agent
writer = Agent(
    role='Lead Technical Writer',
    goal='Synthesize the research into a professional report.',
    backstory="""You are a world-class technical editor. You take 
    raw research data and transform it into a narrative that is 
    easy for executives to read. You excel at structure and clarity.""",
    verbose=True,
    allow_delegation=False
)

# 2. Define the Writing Task
writing_task = Task(
    description="""Review the research findings provided. 
    1. Organize the info into a 3-part report (Summary, Findings, Outlook).
    2. Ensure all technical terms are explained.
    3. Make sure the tone is professional and ready for a client.""",
    expected_output="A polished, 3-section report in Markdown format.",
    agent=writer,
    output_file="final_report.md"  # This is the "Employee's deliverable"
)

# 3. Assemble the Crew
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    process=Process.sequential, # This enforces the "Straight Line"
    verbose=True
)

# 4. The Kickoff (Starting the workday)
print("### Starting the Research Project ###")
result = crew.kickoff(inputs={'topic': 'The current state of Humanoid Robotics in 2024'})

print("\n\n########################")
print("## FINAL REPORT PREPARED BY AI TEAM ##")
print("########################\n")
print(result)