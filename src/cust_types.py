from enum import StrEnum
from typing import Optional, List

from pydantic import BaseModel, EmailStr


class RoleType(StrEnum):
    Analysis = "Analysis"
    Development = "Development"
    Management = "Management"
    Testing = "Testing"
    Running = "Running"
    DevOps = "DevOps"


class TechnologyType(StrEnum):
    Cloud = "Cloud"
    Programming = "Programming"
    Database = "Database"
    DataEng = "DataEng"
    DevOps = "DevOps"
    Documentation = "Documentation"
    Testing = "Testing"


class LocaleType(StrEnum):
    NZ = "NZ"
    UK = "UK"


class TechnologyDetail(BaseModel):
    name: str
    libraries: Optional[List[str]]


class TechCategoryDetail(BaseModel):
    detail_type: TechnologyType
    technologies: List[TechnologyDetail]


class RoleDetail(BaseModel):
    action: str
    effect: str
    detail_type: RoleType


class ResumeEvent(BaseModel):
    position_title: str
    company_name: str
    industry: str
    start_date: int
    end_date: int
    role_details: List[RoleDetail]
    technologies: List[TechCategoryDetail]


class ResumeContactDetails(BaseModel):
    linkedin_uname: str
    linkedin_link: str
    email_addr: EmailStr
    citizenships: List[str]
    ph_num: str


class ResumeInfoSection(BaseModel):
    section_name: str
    section_events: List[ResumeEvent]


class ResumeBody(BaseModel):
    resume_name: str
    contact_section: ResumeContactDetails
    info_sections: List[ResumeInfoSection]
