import inspect
import os
from typing import Any, Callable
from langchain_openai import ChatOpenAI
from bitefix.BiteFixAIRunner import BiteFixAIRunner


def resolve_with_openai(
    openai_api_key: str, model_name: str = "gpt-4", temperature: float = 0.7
) -> Callable:
    """
    Bite Fix AI Decorator that resolves errors in a function using OpenAI model.

    Args:
        openai_api_key (str): The API key for OpenAI.
        model_name (str, optional): The name of the model to use. Defaults to "gpt4".
        temperature (float, optional): The temperature for generating responses. Defaults to 0.7.

    Returns:
        function: Decorator function that resolves errors using Bite Fix AI.
    """

    def resolve_with_openai_decorator(func) -> Callable:
        def function_causing_error(*args, **kwargs) -> Any:
            """
            Function that executes the decorated function and handles errors.

            Args:
                *args: Positional arguments for the decorated function.
                **kwargs: Keyword arguments for the decorated function.

            Returns:
                Any: The result of the decorated function.
            """
            try:
                result = func(*args, **kwargs)
                print("Successfully executed the function.")
                return result
            except Exception as e:
                print("Error occurred while executing the function. - ", e)
                code = inspect.getsource(func)

                os.environ["OPENAI_API_KEY"] = openai_api_key
                llm = ChatOpenAI(temperature=temperature, model_name=model_name)

                print("Starting Bite Fix AI ...")

                biteFixAIRunner = BiteFixAIRunner(
                    function_code=code, arguments=args, error_message=e, llm=llm
                )
                result = biteFixAIRunner.run()

                print("*****************************")
                print("Bite Fix AI completed. Here is the result - ", result)
                print("You can try the suggested fix now. Happy coding!")

        return function_causing_error

    return resolve_with_openai_decorator


def resolve(llm: object) -> Callable:
    """
    Bite Fix AI Decorator that resolves errors in a function using a provided language model.

    Args:
        llm (object): The language model object to use for error resolution.

    Returns:
        function: Decorator function that resolves errors using the provided language model.
    """

    def resolve_decorator(func) -> Callable:
        def function_causing_error(*args, **kwargs) -> Any:
            """
            Function that executes the decorated function and handles errors.

            Args:
                *args: Positional arguments for the decorated function.
                **kwargs: Keyword arguments for the decorated function.

            Returns:
                Any: The result of the decorated function.

            Raises:
                Exception: If an error occurs while executing the decorated function.
            """
            try:
                result = func(*args, **kwargs)
                print("Successfully executed the function.")
                return result
            except Exception as e:
                print("Error occurred while executing the function. - ", e)
                code = inspect.getsource(func)
                print("Starting Bite Fix AI ...")

                biteFixAIRunner = BiteFixAIRunner(
                    function_code=code, arguments=args, error_message=e, llm=llm
                )
                result = biteFixAIRunner.run()

                print("*****************************")
                print("Bite Fix AI completed. Here is the result - ", result)
                print("You can try the suggested fix now. Happy coding!")

        return function_causing_error

    return resolve_decorator
