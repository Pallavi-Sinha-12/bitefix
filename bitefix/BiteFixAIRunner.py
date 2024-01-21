from bitefix.BiteFixAIAgents import BiteFixAIAgents
from bitefix.BiteFixAITasks import BiteFixAITasks
from bitefix.BiteFixAICrew import BiteFixAICrew
from typing import Any, Tuple


class BiteFixAIRunner:

    """
    This class is responsible for running the BiteFixAICrew.

    Attributes:
        function_code (str): The function code.
        arguments (Tuple[Any, ...]): The arguments passed to the function.
        error_message (str): The error message.
        llm (object): The LLM object.

    Methods:
        run: Initializes the Bite Fix AI Agents and Tasks involved in the error fixing process and passes them to the Bite Fix AI Crew to kickoff.
    """

    def __init__(
        self,
        function_code: str,
        arguments: Tuple[Any, ...],
        error_message: str,
        llm: object,
    ):
        self.function_code = function_code
        self.arguments = arguments
        self.error_message = error_message
        self.llm = llm

    def run(self) -> str:
        biteFixAIAgents = BiteFixAIAgents(
            function_code=self.function_code,
            arguments=self.arguments,
            error_message=self.error_message,
            llm=self.llm,
        )

        biteFixAITasks = BiteFixAITasks(
            function_code=self.function_code,
            arguments=self.arguments,
            error_message=self.error_message,
        )

        diagnosisAgent = biteFixAIAgents.DiagnosisAgent()
        ideaGeneratorAgent = biteFixAIAgents.IdeaGeneratorAgent()
        ideasEvaluatorAgent = biteFixAIAgents.IdeasEvaluatorAgent()
        codeDeveloperAgent = biteFixAIAgents.CodeDeveloperAgent()

        diagnosisTask = biteFixAITasks.DiagnosisTask(agent=diagnosisAgent)
        ideaGenerationTask = biteFixAITasks.IdeaGenerationTask(agent=ideaGeneratorAgent)
        ideasEvaluationTask = biteFixAITasks.IdeasEvaluationTask(
            agent=ideasEvaluatorAgent
        )
        codeDevelopmentTask = biteFixAITasks.CodeDevelopmentTask(
            agent=codeDeveloperAgent
        )

        biteFixAICrew = BiteFixAICrew(
            agent=[
                diagnosisAgent,
                ideaGeneratorAgent,
                ideasEvaluatorAgent,
                codeDeveloperAgent,
            ],
            tasks=[
                diagnosisTask,
                ideaGenerationTask,
                ideasEvaluationTask,
                codeDevelopmentTask,
            ],
        )

        result = biteFixAICrew.kickoff()
        return result
