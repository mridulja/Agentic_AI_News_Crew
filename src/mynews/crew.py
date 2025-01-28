from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, FileWriterTool
from dotenv import load_dotenv
import os
# Set up proper debug logging for litellm
os.environ['LITELLM_LOG'] = 'DEBUG'
import litellm

load_dotenv()

@CrewBase
class Mynews():
	"""Mynews crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'
	## Use the below code block to use OpenAI models, or define new LLM objects for other models similar to the below
	
	api_key = os.getenv('OPENAI_API_KEY')
	llm = LLM(
		model="gpt-4o-mini",
		api_key=api_key,
		temperature=0.7
	)

	## Use the below code block to use TOOL like Serper API for searching the Web 
	os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')
	search_tool = SerperDevTool()
	
	file_writer_tool = FileWriterTool()
	web_scraper_tool = ScrapeWebsiteTool()

	@agent
	def retrieve_news(self) -> Agent:
		return Agent(
			config=self.agents_config['retrieve_news'],
			tools=[self.search_tool],
			verbose=True
		)

	@agent
	def website_scraper(self) -> Agent:
		return Agent(
			config=self.agents_config['website_scraper'],
			tools = [self.web_scraper_tool],
			verbose=True
		)
	
	@agent
	def ai_news_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['ai_news_writer'],
			llm=self.llm,
			verbose=True
		)
	
	@agent
	def file_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['file_writer'],
			tools=[self.file_writer_tool],
			verbose=True
		)
	
	@task
	def retrieve_news_task(self) -> Task:
		return Task(
			config=self.tasks_config['retrieve_news_task'],
		)

	@task
	def website_scraper_task(self) -> Task:
		return Task(
			config=self.tasks_config['website_scraper_task']
		)

	@task
	def ai_news_writer_task(self) -> Task:
		return Task(
			config=self.tasks_config['ai_news_writer_task']
		)
	
	@task
	def file_writer_task(self) -> Task:
		return Task(
			config=self.tasks_config['file_writer_task']
		)
	@crew
	def crew(self) -> Crew:
		"""Creates the Mynews crew"""

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
