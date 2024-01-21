from crewai import Crew, Process, Agent, Task


class BiteFixAICrew:

    """
    This class represents a crew of Bite Fix AI agents involved in the decorated function code error fixing process.

    Attributes:
        agent (list[Agent]): List of AI Agents involved in the error fixing process.
        tasks (list[Task]): List of Tasks involved in the error fixing process.

    Methods:
        kickoff: Kicks off the crew. Returns the result of the crew in string format.
    """

    def __init__(self, agent: list[Agent], tasks: list[Task]):
        self.agent = agent
        self.tasks = tasks

    def kickoff(self) -> str:
        crew = Crew(
            agents=self.agent,
            tasks=self.tasks,
            verbose=True,
            process=Process.sequential,
        )
        result = crew.kickoff()
        return result
