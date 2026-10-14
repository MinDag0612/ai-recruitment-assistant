from enum import Enum


class LLMModel(str, Enum):
    GPT_41_MINI = "gpt-4.1-mini"
    GPT_41 = "gpt-4.1"
    GEMINI_FLASH = "gemini-3.8-flash"
    

class Prompt(str, Enum):
    PROMPT_EXTRACT_INFOR_JD = """
        Extract job description information.

        Rules:
        - Extract only information explicitly supported by the text.
        - Do not invent skills, education, experience,
          certificates, or responsibilities.
        - Preserve the meaning of the original text.
        - Return an empty list for a category with no
          information.
        - Separate distinct items into individual list elements.
        - Do not split a single concept into unrelated fragments.
    """

    PROMPT_EXTRACT_INFOR_RESUME = """
        Extract candidate information from the provided resume.

        Rules:
        - Extract only information explicitly supported by the text.
        - Do not invent skills, education, experience,
          certificates, or projects.
        - Preserve the meaning of the original text.
        - Return an empty list for a category with no
          information.
        - Separate distinct items into individual list elements.
        - Do not split a single concept into unrelated fragments.
        - Extract projects only when they are mentioned in the resume.
        - Do not confuse projects with work experience.
        - Do not confuse skills used in a project with certifications.
    """

    