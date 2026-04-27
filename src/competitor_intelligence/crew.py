from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from competitor_intelligence.tools import (
    search_tool,
    scrape_tool,
    file_writer_tool,
    file_read_tool,
    sentiment_scrape_tool,
)

@CrewBase
class CompetitorIntelligence():
    """CompetitorIntelligence crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

    agents_config = "config/agents.yaml"
    tasks_config  = "config/tasks.yaml"

    # ── Agents ────────────────────────────────────────────────────────────────

    @agent
    def web_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["web_researcher"],
            tools=[search_tool],          # removed scrape_tool — too large for local model
            llm="ollama/mistral-nemo:12b",
            max_rpm=25,
            verbose=True,
            max_iter=3,
        )

    @agent
    def sentiment_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["sentiment_analyst"],
            tools=[search_tool, sentiment_scrape_tool],
            llm="ollama/mistral-nemo:12b",
            max_rpm=25,
            verbose=True,
            max_iter=3,
        )

    @agent
    def competitor_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["competitor_analyst"],
            llm="ollama/mistral-nemo:12b",
            max_rpm=25,
            verbose=True,
            max_iter=3,
        )

    @agent
    def strategy_generator(self) -> Agent:
        return Agent(
            config=self.agents_config["strategy_generator"],
            llm="ollama/mistral-nemo:12b",
            max_rpm=25,
            verbose=True,
            max_iter=3,
        )

    @agent
    def report_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["report_writer"],
            tools=[file_writer_tool],     # use imported, not self.file_write_tool
            llm="ollama/mistral-nemo:12b",
            max_rpm=25,
            verbose=True,
            max_iter=3,
        )


    # ── Tasks ─────────────────────────────────────────────────────────────────

    @task
    def research_task(self) -> Task:
        return Task(config=self.tasks_config["research_task"])

    @task
    def sentiment_task(self) -> Task:
        return Task(config=self.tasks_config["sentiment_task"])

    @task
    def analysis_task(self) -> Task:
        return Task(config=self.tasks_config["analysis_task"])

    @task
    def strategy_task(self) -> Task:
        return Task(config=self.tasks_config["strategy_task"])

    @task
    def report_task(self) -> Task:
        return Task(config=self.tasks_config["report_task"])

    # ── Crew ──────────────────────────────────────────────────────────────────

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            max_rpm=25,
            embedder={
                "provider": "ollama",
                "config": {
                    "model": "nomic-embed-text",
                    "base_url": "http://localhost:11434",
                }
            }
        )