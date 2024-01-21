# BiteFix 🛠️

![Last commit](https://img.shields.io/github/last-commit/Pallavi-Sinha-12/bitefix?color=green&label=Last%20commit)
![Repo size](https://img.shields.io/github/repo-size/Pallavi-Sinha-12/bitefix?color=orange&label=Repo%20size)
[![Stars](https://img.shields.io/github/stars/Pallavi-Sinha-12/bitefix?color=yellow&label=Stars)](https://github.com/Pallavi-Sinha-12/Expense-Tracker-Chatbot/stargazers)
[![Forks](https://img.shields.io/github/forks/Pallavi-Sinha-12/bitefix?color=orange&label=Forks)](https://github.com/Pallavi-Sinha-12/bitefix/forks)


BiteFix is an advanced and efficient tool designed to revolutionize the error-fixing process using the capabilities of Large Language Models (LLM). It is a Python library that offers a range of decorators to help you debug your code and fix errors in a matter of seconds.

## Table of Contents 📋

- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Examples](#examples)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Feedback](#feedback)
- [Contact](#contact)
- [License](#license)
- [References](#references)

## Introduction 🌟

By offering decorators, BiteFix empowers you to enhance the error-handling experience in your functions. When a decorated function encounters an error, the decorator orchestrates a team of AI Agents, each specializing in a unique aspect of error resolution. Here's a brief overview of the AI Agents:

🕵️ **Python code Diagnosis Expert**: Swiftly analyzes the code to pinpoint the root cause of the error.

👨‍💻 **Senior Python Developer**: Provides insightful ideas on how to rectify the issue within the decorated function's code.

👩‍💼 **Lead Python Developer**: Meticulously evaluates ideas, selecting the most effective one for implementation.

👨‍💻 **Python Code Developer**: Skillfully rewrites the code to bring the chosen idea to life, ultimately fixing the error.

BiteFix simplifies the error-fixing journey by seamlessly combining the expertise of these AI Agents, ensuring a smoother and more efficient debugging process for your Python code.


## Technologies Used 🔧

- [![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
- [![langchain](https://img.shields.io/badge/langchain-0.1.1-yellow)](https://api.python.langchain.com/en/latest/langchain_api_reference.html#)
- [![crewai](https://img.shields.io/badge/crewai-0.1.2-green)](https://github.com/joaomdmoura/crewAI.git)
- [![gpt-4](https://img.shields.io/badge/gpt-4-orange)](https://openai.com/)

## Getting Started 🚀

- Install BiteFix using `pip install bitefix`
- Explore the powerful decorators to streamline your error-fixing process!
- Check out the [examples](#examples) to understand how BiteFix works.

Happy Coding! 🚀

## Examples 💻

Let's take a look at some examples to understand how BiteFix works. Bitefix offers two decorators: `@resolve` and `@resolve_with_openai`.

### Example 1 : Using Open AI Models

Let's say you have a function that is supposed to return longest length of subsequence in a given list. We can use `@resolve_with_openai` decorator with our function to help us resolve the error if the function fails while execution.

```python

from bitefix import resolve_with_openai

@resolve_with_openai(openai_api_key="YOUR_OPENAI_KEY")
def length_of_lis(nums):
    if not nums:
        return 0

    dp = [1] * len(nums)

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = dp[i + 1]

    return max(dp)

```

In the above example, we have just added Open AI API key as a parameter to the decorator. You can also add the name of the particular Open AI LLM you want to use and the temperature. By default, it uses OpenAI's gpt-4 model with temperature 0.7.
Now after writing the function, let's try to execute it with a list of numbers.

```python

input_list = [10, 9, 2, 5, 3, 7, 101, 18]
result = length_of_lis(input_list)
print(result)

```

Here is the recorded output of the function execution - [bitefix_decorator_example](https://drive.google.com/file/d/1JKeKCbhwSRkx4MfrVtz1oAtW_n4Up1rN/view?usp=sharing)


We can see how this decorator provided us step by step debugging of the function in case of failure by using crew of Python AI coders. It also provided us with the solution to the error.

### Example 2 : Using Open Source Models

If we want to use some other Large Language Model instead of OpenAI, we can use `@resolve` decorator with our function to help us resolve the error if the function fails while execution. This helps us to use any custom trained model as well for error resolution.

For this example, let's use Openhermes model from Ollama. You can download Ollama from [here](https://ollama.ai/). Ollama allows you to run open-source large language models, such as Openhermes, Llama 2, locally. 

After downloading Ollama, install it. Then run the following command to pull the Openhermes model.

```bash
ollama pull openhermes
```

Now, we can use the model with the decorator `@resolve` as follows.

```python

from bitefix import resolve
from langchain_community.llms import Ollama

llm = Ollama("openhermes")

@resolve(llm)
def length_of_lis(nums):
    if not nums:
        return 0

    dp = [1] * len(nums)

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = dp[i + 1]

    return max(dp)

```

Similarly, we can use any other Large Language Model with the decorator.

## Project Structure 📁

The project structure of Bitefix is as follows:

- `bitefix` : This folder contains the source code of the Bitefix library.
- `bitefix/__init__.py` : This file is used to make the `bitefix` folder a Python module.
- `bitefix/bitefix_utils.py` : This file contains the decorators exposed by the Bitefix library.
- `bitefix/BiteFixAIRunner` : This file contains the class that orchestrates the AI Agents to resolve the error.
- `bitefix/BiteFixAICrew` : This file contains the class that represents the crew of Bitefix AI Agents.
- `bitefix/BiteFixAIAgents` : This file contains the classes that represent the individual Bitefix AI Agents.
- `bitefix/BiteFixAITasks` : This file contains the classes that represent the individual tasks performed by the Bitefix AI Agents.
- `requirements.txt` - This file specifies the Python dependencies required to run the project.
- `setup.py` - This file is used to package the project for distribution.
- `LICENSE` - This file contains the license information for the project.
- `README.md` - This file contains the documentation for the project.

## Contributing 🤝

Contributions are always welcome!

If you find any issue or have suggestions for improvements, please submit them as Github issues or pull requests.

Here is the steps you can follow to contribute to this project:

1. Fork the project on Github.
2. Clone the forked project to your local machine.
3. Create a virtual environment using `python -m venv venv`.
4. Activate the virtual environment using `venv\Scripts\activate` on Windows or `source venv/bin/activate` on Mac/Linux
5. Install the dependencies using `pip install -r requirements.txt`.
6. Make the required changes.
7. Format the code using `black .`.
8. Create a pull request.


## Feedback 📣

If you liked the project support it by giving a star :star:

Feel free to send me feedback at pallavisinha95829@gmail.com. Let me know if you have any suggestions on how to make this project better.


## 🔗 Contact 📞
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/pallavi-sinha-09540917b/)[![GitHub](https://img.shields.io/badge/GitHub-555555?style=for-the-badge&logo=github&logoColor=white&)](https://github.com/Pallavi-Sinha-12)

## License 📝

This project is licensed under the terms of the [MIT license](https://choosealicense.com/licenses/mit/)

## References 📚

- crewAI: Cutting-edge framework for orchestrating role-playing, autonomous AI agents. https://github.com/joaomdmoura/crewAI

- langchain: Python library for interacting with the Langchain API. https://api.python.langchain.com/en/latest/langchain_api_reference.html#

- OpenAI: OpenAI is an artificial intelligence research laboratory consisting of the for-profit corporation OpenAI LP and its parent company, the non-profit OpenAI Inc. https://openai.com/

- Ollama: Ollama allows you to run open-source large language models, such as Openhermes, Llama 2, locally. https://ollama.ai/