from pydantic import BaseModel


class ResumeContactDetails(BaseModel):
    pass

class ResumeInfoSection(BaseModel):
    pass

class ResumeBody(BaseModel):
    resume_name: str
    contact_section: ResumeContactDetails
    info_sections: list[ResumeInfoSection]

