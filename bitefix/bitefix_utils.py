import inspect
import os
from typing import Any, Callable
from langchain_openai import ChatOpenAI
from bitefix.BiteFixAIRunner import BiteFixAIRunner
from crewai.tasks.task_output import TaskOutput
from typing import List
from datetime import datetime


def resolve_with_openai(
    openai_api_key: str,
    function_description: str = None,
    model_name: str = "gpt-4",
    temperature: float = 0.7,
    export_dir: str = None,
    verbose: bool = True,
) -> Callable:
    """
    Bite Fix AI Decorator that provides error resolution on Runtime Errors using BiteFix AI Agents and OpenAI's Large Language Model.

    Args:
        openai_api_key (str): The API key for OpenAI.
        function_description (str, optional): Recommended to provide a description of the function to be resolved. It should not be less than 20 words and more than 50 words. Defaults to None.
        model_name (str, optional): The name of the model to use. Defaults to "gpt4".
        temperature (float, optional): The temperature for generating responses. Defaults to 0.7.
        export_dir (str, optional): The path to the directory to export the error resolution report. Defaults to None.
        verbose (bool, optional): Whether to print the output of the BiteFix AI process. Defaults to True.

    Returns:
        function: Decorator function that provides error resolution using BiteFix AI Agents and OpenAI's Large Language Model.
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
                print("Starting Bite Fix AI ...\n")
                code = inspect.getsource(func)

                os.environ["OPENAI_API_KEY"] = openai_api_key
                llm = ChatOpenAI(temperature=temperature, model_name=model_name)

                if function_description:
                    if (
                        len(function_description.split()) < 20
                        or len(function_description.split()) > 50
                    ):
                        raise ValueError(
                            "The function description should be within the word limit of 20-50 words."
                        )
                print("Running BiteFix AI ...\n")
                try:
                    biteFixAIRunner = BiteFixAIRunner(
                        function_code=code,
                        function_description=function_description,
                        arguments=args,
                        error_message=e,
                        llm=llm,
                    )
                    result = biteFixAIRunner.run()
                except Exception as ex:
                    print("Error occurred while running BiteFix AI - ", ex)
                    return None
                print("BiteFix AI completed.\n")
                if verbose:
                    print("BiteFix AI Error Resoltion Report: \n\n")
                    print(
                        "[PYTHON CODE DIAGNOSIS EXPERT] Error Diagnosis :\n\n",
                        result["tasks_outputs"][0].result().replace("```", ""),
                    )
                    print(
                        "\n\n[SENIOR PYTHON CODE EXPERT] Error resolution Ideas :\n\n",
                        result["tasks_outputs"][1].result().replace("```", ""),
                    )
                    print(
                        "\n\n[LEAD PYTHON CODE EXPERT] Best Resolution Idea Evaluation :\n\n",
                        result["tasks_outputs"][2].result().replace("```", ""),
                    )
                    print(
                        "\n\n[PYTHON CODE DEVELOPER] Resolution Idea Implemenation  :\n\n",
                        result["tasks_outputs"][3].result(),
                    )

                try:
                    if export_dir:
                        export_error_resolution_report(
                            result["tasks_outputs"], export_dir
                        )
                except Exception as exc:
                    print(
                        "Error occurred while exporting the error resolution report - ",
                        exc,
                    )

        return function_causing_error

    return resolve_with_openai_decorator


def resolve(
    llm: object,
    function_description: str = None,
    export_dir: str = None,
    verbose: bool = True,
) -> Callable:
    """
    Bite Fix AI Decorator that provides error resolution on Runtime Errors using BiteFiix AI Agents and the provided LLM.

    Args:
        llm (object): The language model object to use for error resolution.
        export_dir (str, optional): The directory to export Error Resoltion Report by BiteFix AI Agents and fixed code python file. Defaults to None.
        function_description (str, optional): Recommended to provide a description of the function to be resolved. Word limit: 20-50 words. Defaults to None.
        verbose (bool, optional): Whether to print the output of the BiteFix AI process. Defaults to True.

    Returns:
        function: Decorator function that provides error resolution using the BiteFix AI Agents and provided Large Language Model.
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
                if function_description:
                    if (
                        len(function_description.split()) < 20
                        or len(function_description.split()) > 50
                    ):
                        raise ValueError(
                            "The function description should be within the word limit of 30-50 words."
                        )

                print("Starting Bite Fix AI ...\n")

                try:
                    biteFixAIRunner = BiteFixAIRunner(
                        function_code=code,
                        function_description=function_description,
                        arguments=args,
                        error_message=e,
                        llm=llm,
                    )
                    result = biteFixAIRunner.run()
                except Exception as ex:
                    print("Error occurred while running BiteFix AI - ", ex)
                    return None

                print("BiteFix AI completed.\n")
                if verbose:
                    print("BiteFix AI Error Resoltion Report: \n\n")
                    print(
                        "[PYTHON CODE DIAGNOSIS EXPERT] Error Diagnosis :\n\n",
                        result["tasks_outputs"][0].result().replace("```", ""),
                    )
                    print(
                        "\n\n[SENIOR PYTHON CODE EXPERT] Error resolution Ideas :\n\n",
                        result["tasks_outputs"][1].result().replace("```", ""),
                    )
                    print(
                        "\n\n[LEAD PYTHON CODE EXPERT] Best Idea Evaluation :\n\n",
                        result["tasks_outputs"][2].result().replace("```", ""),
                    )
                    print(
                        "\n\n[PYTHON CODE DEVELOPER] Resolution Idea Implemenation :\n\n",
                        result["tasks_outputs"][3].result(),
                    )

                if export_dir:
                    try:
                        export_error_resolution_report(
                            result["tasks_outputs"], export_dir
                        )
                    except Exception as exc:
                        print(
                            "Error occurred while exporting the error resolution report - ",
                            exc,
                        )

        return function_causing_error

    return resolve_decorator


def export_error_resolution_report(output: List[TaskOutput], export_dir: str) -> None:
    """
    Export the error resolution report to a file in the specified directory.

    Args:
        output (List[TaskOutput]): The list of task outputs from the BiteFix AI process.
        export_dir (str): The Path to the directory to export the error resolution report.

    Returns:
        None
    """

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    report_file_name = f"BiteFixAIErrorResolutionReport_{timestamp}.md"
    report_file_path = os.path.join(export_dir, report_file_name)
    with open(report_file_path, "w") as file:
        file.write("# BiteFix AI Error Resolution Report\n\n")
        file.write("## Error Diagnosis Report by Python Code Diagnosis Expert\n\n")
        file.write(output[0].result().replace("```", ""))
        file.write("\n\n")
        file.write("## Error resolution ideas Report by Senior Python Code Expert\n\n")
        file.write(output[1].result().replace("```", ""))
        file.write("\n\n")
        file.write("## Best Idea Evaluation Report by Lead Python Code Expert\n\n")
        file.write(output[2].result().replace("```", ""))
        file.write("\n\n")
        file.write(
            "## Resolution Idea Implemenation Report by Python Code Developer\n\n"
        )
        file.write(output[3].result())
        file.write("\n\n")
    print(f"\nError Resolution Report has been saved to {report_file_path}")
