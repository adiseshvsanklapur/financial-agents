from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools

from dotenv import load_dotenv

load_dotenv()

web_search_agent = Agent(
    name = "The Web Agent",
    description = "This is the agent that will scour through the web and then find content regarding a particular topic",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools = [DuckDuckGo()],
    instructions = "Search the web to find up-to-date, relevant, and accurate content for the user's query. Summarize your findings clearly and concisely. Always include clickable source links for verification, and prefer authoritative or primary sources when possible.",
    show_tool_calls = True,
    markdown = True,
    debug_mode = True
)

finance_agent = Agent(
    name = "The Finance Agent",
    description = "Your task is to find all the financial information",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools = [YFinanceTools(stock_price = True, analyst_recommendations = True, company_info = True, company_news = True)],
    instructions = "Use clear and structured tables to present all financial data. Include key metrics such as stock price, changes over time, analyst sentiment, and any recent financial news. Ensure the data is up-to-date and easy to compare at a glance.",
    show_tool_calls = True,
    markdown = True,
    debug_mode = True
)

agent_team = Agent(
    team = [web_search_agent, finance_agent],
    model = Groq(id="llama-3.3-70b-versatile"),
    instructions = [
        "Coordinate between the web and finance agents to provide a comprehensive answer.",
        "Use structured tables to present quantitative data such as stock prices or analyst ratings.",
        "Summarize written content clearly and highlight the most critical insights.",
        "Always include source links for external content to ensure transparency and traceability."
    ],
    show_tool_calls = True,
    markdown = True,
    debug_mode = False
)

agent_team.print_response("Summarize analyst recommendations for NVDA", stream = True)