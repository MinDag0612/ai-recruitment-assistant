
from pydantic import BaseModel, Field


class InforExtractedBase(BaseModel):
    skill: list[str] = Field(
        default_factory=list,
        description=(
            "Skills and competencies explicitly mentioned in the text, "
            "including technical skills, practical abilities, "
            "professional skills, and interpersonal skills. "
            "Extract relevant items from any section of the text."
        ),
    )

    education: list[str] = Field(
        default_factory=list,
        description=(
            "Educational background and qualifications explicitly "
            "mentioned, including degrees, fields of study, schools, "
            "academic achievements, and educational requirements."
        ),
    )

    experience: list[str] = Field(
        default_factory=list,
        description=(
            "Professional or work experience explicitly mentioned, "
            "including positions, organizations, duration, duties, "
            "achievements, and relevant previous work."
        ),
    )

    certificate: list[str] = Field(
        default_factory=list,
        description=(
            "Professional certificates, licenses, and other formal "
            "qualifications explicitly mentioned in the text. "
            "Do not include ordinary skills or work experience."
        ),
    )


class InforExtractedResume(InforExtractedBase):
    project: list[str] = Field(
        default_factory=list,
        description=(
            "Projects or substantial pieces of work explicitly "
            "mentioned in the resume, including their names, goals, "
            "activities, outcomes, and the candidate's contributions "
            "when stated."
        ),
    )


class InforExtractedJD(InforExtractedBase):
    responsibilities: list[str] = Field(
        default_factory=list,
        description=(
            "Duties, tasks, and expected work activities explicitly "
            "stated in the job description."
        ),
    )
