from crewai import Crew, Process, Agent, Task


class BiteFixAICrew:

    """
    This class represents a crew of Bite Fix AI agents involved in the decorated function code error fixing process.

    Attributes:
        agent (list[Agent]): List of AI Agents involved in the error fixing process.
        tasks (list[Task]): List of Tasks involved in the error fixing process.

    Methods:
        kickoff: Kicks off the crew. Returns the result of the agents.
    """

    def __init__(self, agent: list[Agent], tasks: list[Task]):
        self.agent = agent
        self.tasks = tasks

    def kickoff(self) -> dict:
        crew = Crew(
            agents=self.agent,
            tasks=self.tasks,
            verbose=False,
            process=Process.sequential,
            full_output=True,
        )
        result = crew.kickoff()
        return result
