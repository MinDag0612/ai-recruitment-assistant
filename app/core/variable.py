from enum import Enum


class LLMModel(str, Enum):
    GPT_41_MINI = "gpt-4.1-mini"
    GPT_41 = "gpt-4.1"
    GEMINI_FLASH = "gemini-3.8-flash"
    OLLAMA_MODEL = "qwen2.5:3b"


from enum import Enum


class Prompt(str, Enum):
    SYSTEM_RULE = """
      You are an information extraction system.

      General rules:
      - Extract all relevant information explicitly stated in the document.
      - Assign each item to the most appropriate field based on its meaning.
      - Do not omit information merely because it appears outside a
        section with a matching heading.
      - Do not invent information or infer unstated facts.
      - Preserve the original meaning and important details.
      - Put each distinct item in a separate list element.
      - Do not split a single concept into unrelated fragments.
      - Use an empty list only when the document contains no relevant
        information for that field.
      - Return only data that conforms to the provided JSON schema.
    """

    PROMPT_EXTRACT_INFOR_JD = """
      Extract information from the job description.

      Field definitions:
      - skill: Skills and competencies required or preferred by the
        employer, including technical, practical, professional, and
        interpersonal skills.
      - education: Required or preferred educational qualifications,
        degrees, fields of study, and academic requirements.
      - experience: Required experience levels, years of experience,
        previous work background, and relevant professional experience.
      - certificate: Professional certificates, licenses, and formal
        qualifications required or preferred by the employer.
      - responsibilities: Duties, tasks, and expected work activities
        the candidate is required to perform.

      Extraction rules:
      - Extract requirements from all sections, including job
        requirements, qualifications, preferred qualifications,
        responsibilities, and job descriptions.
      - Extract each explicitly stated skill separately when possible.
      - Keep required qualifications distinct from preferred ones
        when the source makes that distinction clear.
      - Do not treat the employer's requirements as qualifications
        already possessed by a candidate.
    """

    PROMPT_EXTRACT_INFOR_RESUME = """
      Extract information from the candidate's resume.

      Field definitions:
      - skill: Skills and competencies explicitly demonstrated or
        listed by the candidate, including technical, practical,
        professional, and interpersonal skills.
      - education: Educational background, including degrees, fields
        of study, institutions, and academic qualifications.
      - experience: Employment history, including positions, employers,
        dates, duties, achievements, and relevant work experience.
      - certificate: Professional certificates, licenses, and formal
        qualifications explicitly obtained by the candidate.
      - project: Projects or substantial work explicitly mentioned,
        including project names, purposes, activities, technologies
        or methods used, outcomes, and the candidate's contributions
        when stated.

      Extraction rules:
      - Extract skills from every section, including skills lists,
        work experience, education, and project descriptions.
      - Extract education information even when it appears in a short
        sentence rather than a dedicated education section.
      - Preserve relevant details about each position, project,
        qualification, and achievement.
      - Do not confuse projects with employment history.
      - Do not treat skills or tools used in a project as certificates.
      - Do not assume that a candidate possesses a skill solely
        because it is commonly associated with a job title.
    """
