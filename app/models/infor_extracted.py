from pydantic import BaseModel, Field


class InforExtractedBase(BaseModel):
    skill: list[str] = Field(default_factory=list)
    education: list[str] = Field(default_factory=list)
    experience: list[str] = Field(default_factory=list)
    certificate: list[str] = Field(default_factory=list)


class InforExtractedResume(InforExtractedBase):
    project: list[str] = Field(default_factory=list)


class InforExtractedJD(InforExtractedBase):
    responsibilities: list[str] = Field(default_factory=list)