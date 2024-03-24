from typing import List, Tuple

from src.content_loader import main as content_load
from src.cust_types import (ResumeBody, ResumeEvent, ResumeInfoSection,
                            TechCategoryDetail)
from src.definitions import JINENV



def main() -> str:
    # Gotta Load Up That Content
    resume_body: ResumeBody = content_load()

    # Extract Templates
    section_template = JINENV.get_template("./templates/resume_section.tex")
    body_template = JINENV.get_template("./templates/resume_body.tex")

    # Render Experience Section

    resume_experience_section: ResumeInfoSection = list(
        filter(lambda x: x.section_name == "Experience", resume_body.info_sections)
    )[0]
    experience_section_rendered_text = section_template.render(
        **dict(resume_experience_section)
    )

    resume_rendered_text = body_template.render(
        resume_name=resume_body.resume_name,
        contact_section=resume_body.contact_section,
        resume_sections=[experience_section_rendered_text],
    )
    return resume_rendered_text


if __name__ == "__main__":
    main()
