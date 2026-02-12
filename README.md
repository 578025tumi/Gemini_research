<h1>🤖 Multi-Agent Research & Reporting Team</h1>  
<h2>This project implements a Multi-Agent AI Team that functions as a virtual research department. It utilizes a "Straight Line" (Sequential) workflow where specialized AI agents perform high-level work—from live web searching to executive report synthesis—without human intervention.</h2>
<h3>🏢 The "Employee" Architecture</h3>  
<b>Unlike a standard chatbot, this system uses a Sequential Process where the output of one professional agent becomes the input for the next.
🕵️‍♂️ Agent 1: The Lead Researcher
Role: Senior Market Research Analyst
Responsibility: Browses the live web using the Tavily AI search engine.
Task: Extracts hard facts, dates, and sources on a specific topic.
Output: A structured research brief.
✍️ Agent 2: The Technical Writer
Role: Lead Technical Writer
Responsibility: Data synthesis and professional communication.
Task: Transforms the Researcher's brief into a boardroom-ready Markdown report.
Constraint: No internet access (prevents hallucination; ensures focus on researched facts).
🚀 Tech Stack
Framework: CrewAI (Orchestration)
Brain: OpenAI GPT-4o / Claude 3.5 Sonnet
Eyes: Tavily AI (Search API optimized for LLMs)
Language: Python 3.12
🛠️ Setup & Installation</b>
1. Clone the Repository
code
Bash
git clone https://github.com/YOUR_USERNAME/research-team-ai.git
cd research-team-ai
2. Install Dependencies
code
Bash
pip install -r requirements.txt
3. Environment Configuration
Create a .env file in the root directory and add your API keys:
code
Text
OPENAI_API_KEY=your_openai_key_here
TAVILY_API_KEY=your_tavily_key_here
(Note: The .env file is ignored by git to keep your keys secure.)
📈 Usage
To start the research project, run:
code
Bash
python research_team.py
What Happens:
Kickoff: You provide a topic (e.g., "The future of Solid State Batteries").
Research Phase: The Researcher Agent hits the web and logs its "thought process" in the terminal.
Handoff: Once the research is verified, it is passed to the Writer.
Deliverable: The team produces a file named final_report.md in your project folder.
