from crewai import Agent, Task
from typing import Any, Tuple


class BiteFixAITasks:

    """
    This class is responsible for creating the tasks for the BiteFixAI task.
    The tasks are the steps involved in the process of fixing the error in the decorated python function.

    Attributes:
        function_code (str): The function code.
        arguments (Tuple[Any, ...]): The arguments passed to the function.
        error_message (str): The error message.

    Methods:
        DiagnosisTask: Returns a task responsible for diagnosing the error.
        IdeaGenerationTask: Returns a task responsible for generating ideas to fix the error.
        IdeasEvaluationTask: Returns a task responsible for evaluating and choosing the best idea to fix the error.
        CodeDevelopmentTask: Returns a task responsible for writing the code to fix the error.
    """

    def __init__(
        self, function_code: str, arguments: Tuple[Any, ...], error_message: str
    ):
        self.function_code = function_code
        self.arguments = arguments
        self.error_message = error_message

    def DiagnosisTask(self, agent: Agent) -> Task:
        return Task(
            description=f"""Go through the function code, arguments passed and the error message and explain why the error occured. 
            Explain why the function failed for the arguments passed. Explain it in normal human language. 
            The function code is given to you here - {self.function_code}. 
            The arguments passed are given to you here - {self.arguments}. 
            The error message is given to you here - {self.error_message}.""",
            agent=agent,
        )

    def IdeaGenerationTask(self, agent: Agent) -> Task:
        return Task(
            description=f"""Generate ideas on how to fix the error in normal human language. 
            You also think of best practices and efficiency while suggesting the ideas. 
            Consider the given function code, arguments passed and the error message while generating the ideas. 
            The function code is given to you here - {self.function_code}. 
            The arguments passed are given to you here - {self.arguments}. 
            The error message is given to you here - {self.error_message}. """,
            agent=agent,
        )

    def IdeasEvaluationTask(self, agent: Agent) -> Task:
        return Task(
            description=f"""Evaluate the error fix ideas and choose the best idea to fix the error.
            Also explain your decision to fix the error in normal human language. 
            Also think of best practices and efficiency while evaluating the ideas. 
            Take a look on function code, arguments passed and error message as well if needed. 
            The function code is given to you here - {self.function_code}. 
            The arguments passed are given to you here - {self.arguments}. 
            The error message is given to you here - {self.error_message}.""",
            agent=agent,
        )

    def CodeDevelopmentTask(self, agent: Agent) -> Task:
        return Task(
            description=f"""Rewrite the function code to fix the error based on the idea chosen. 
            Also explain the implementation details in normal human language. 
            The function code is given to you here - {self.function_code}. 
            The arguments passed are given to you here - {self.arguments}. 
            The error message is given to you here - {self.error_message}. """,
            agent=agent,
        )
