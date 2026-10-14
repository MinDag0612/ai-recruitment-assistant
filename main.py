from app.features.processor.gemini_model import GEMINIModel
from app.models.infor_extracted import (
    InforExtractedJD,
    InforExtractedResume,
)


def test_extract_jd():
    model = GEMINIModel()

    parsed_text = """
    Backend Engineer Intern

    Requirements:
    - Proficient in Python.
    - Familiar with FastAPI and REST APIs.
    - Basic knowledge of PostgreSQL and Docker.
    - Currently pursuing a degree in Computer Science or Software Engineering.
    - No prior work experience required.

    Responsibilities:
    - Develop and maintain backend APIs.
    - Write unit tests.
    - Collaborate with the AI engineering team.
    """

    result = model.extract(
        parsed_text=parsed_text,
        is_resume=False,
    )

    print("\nJD extraction result:")
    print(result.model_dump_json(indent=2))

    assert isinstance(result, InforExtractedJD)
    assert isinstance(result.skill, list)
    assert isinstance(result.education, list)
    assert isinstance(result.experience, list)
    assert isinstance(result.certificate, list)
    assert isinstance(result.responsibilities, list)

    assert any("Python" in item for item in result.skill)
    assert len(result.responsibilities) > 0


def test_extract_resume():
    model = GEMINIModel()

    parsed_text = """
    EDUCATION
    Bachelor of Software Engineering, Ton Duc Thang University.
    Expected graduation: 2027.

    SKILLS
    Python, FastAPI, PostgreSQL, Docker, Git.

    PROJECTS
    AI Recruitment Assistant:
    - Developed REST APIs using FastAPI.
    - Implemented JWT authentication.
    - Used PostgreSQL for data persistence.

    EXPERIENCE
    No formal work experience listed.

    CERTIFICATIONS
    AWS Certified Cloud Practitioner.
    """

    result = model.extract(
        parsed_text=parsed_text,
        is_resume=True,
    )

    print("\nResume extraction result:")
    print(result.model_dump_json(indent=2))

    assert isinstance(result, InforExtractedResume)
    assert isinstance(result.skill, list)
    assert isinstance(result.education, list)
    assert isinstance(result.experience, list)
    assert isinstance(result.certificate, list)
    assert isinstance(result.project, list)

    assert any("FastAPI" in item for item in result.skill)
    assert len(result.project) > 0


if __name__ == "__main__":
    test_extract_jd()
    test_extract_resume()
    print("\nAll extraction tests passed.")
