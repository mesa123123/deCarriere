from enum import StrEnum

from pydantic import BaseModel, EmailStr

DETAIL_TYPE = StrEnum(
    "detailType",
    ["Analysis", "Development", "Management", "Testing", "Running", "DevOps"],
)

TECHNOLOGY_TYPE = StrEnum(
    "technologType",
    ["Cloud", "Programming", "Database", "DataEng", "DevOps", "Management"],
)


class TechnologyDetail(BaseModel):
    name: str
    tech_type: TECHNOLOGY_TYPE
    libraries: list[str]


class RoleDetail(BaseModel):
    action: str
    effect: str
    detail_type: DETAIL_TYPE


class ResumeEvent(BaseModel):
    position_title: str
    company_name: str
    industry: str
    start_date: int
    end_date: int
    role_details: list[RoleDetail]
    technologies: list[TechnologyDetail]


class ResumeContactDetails(BaseModel):
    linkedin_uname: str
    linkedin_link: str
    email_addr: EmailStr
    citizenships: list[str]
    ph_num: str


class ResumeInfoSection(BaseModel):
    section_name: str
    section_events: list[ResumeEvent]


class ResumeBody(BaseModel):
    resume_name: str
    contact_section: ResumeContactDetails
    info_sections: list[ResumeInfoSection]
