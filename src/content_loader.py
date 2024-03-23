"""󰘧 main() -> ResumeBody"""

import os
from os.path import join
from typing import List, Union

import yaml

from src.cust_types import (LocaleType, ResumeBody, ResumeContactDetails,
                            ResumeEvent, ResumeInfoSection, RoleDetail,
                            TechCategoryDetail, TechnologyDetail)
from src.definitions import DATA_PATH, LOCALE, RESUME_NAME


# Section: Loaders
# ----------
# Load Experience Details
def load_event_info(
    data_dir: str = DATA_PATH, events_dir: str = "Events"
) -> List[dict]:
    file_paths = [
        f"{data_dir}{events_dir}/{file}"
        for file in os.listdir(f"{data_dir}{events_dir}")
    ]
    return [yaml.safe_load(open(file_path, "r")) for file_path in file_paths]


# Load Contact Details
def load_contact_details(
    data_dir: str = DATA_PATH, contact_file: str = "contacts.yml"
) -> dict:
    return yaml.safe_load(open(join(data_dir, contact_file), "r"))


# ----------


# Section: Parsers
# ----------
def parse_tech_detail(tech_dict: Union[dict[str, List[str]], str]) -> TechnologyDetail:
    if isinstance(tech_dict, str):
        return TechnologyDetail(name=tech_dict, libraries=None)
    tech_tuple = list(tech_dict.items())
    if len(tech_tuple) > 1:
        raise ValueError("You parsed the tech detail with more than one technology")
    return TechnologyDetail(name=tech_tuple[0][0], libraries=tech_tuple[0][1])


def parse_tech_category(categories: List[dict]) -> List[TechCategoryDetail]:
    return [
        TechCategoryDetail(
            detail_type=key,
            technologies=[parse_tech_detail(technology) for technology in value],
        )
        for techcategory in categories
        for key, value in techcategory.items()
    ]


def parse_roles(role_points: List[dict]) -> List[RoleDetail]:
    return [
        RoleDetail(
            action=point["action"],
            effect=point["affect"],
            detail_type=point["category"].title(),
        )
        for point in role_points
    ]


def parse_events(events: List[dict]) -> List[ResumeEvent]:
    def process_event(event: dict) -> ResumeEvent:
        event["role_details"] = parse_roles(event["role_details"])
        event["technologies"] = parse_tech_category(event["technologies"])
        return ResumeEvent(**event)

    return [process_event(event) for event in events]


def parse_contacts(contact_dict: dict, locale: LocaleType) -> ResumeContactDetails:
    ph_num = (
        contact_dict["ph_num"]["NZ"]
        if locale == LocaleType.NZ
        else contact_dict["ph_num"]["UK"]
    )
    del contact_dict["ph_num"]
    return ResumeContactDetails(ph_num=ph_num, **contact_dict)


def parse_info_section(section: str, events: List[ResumeEvent]):
    return ResumeInfoSection(section_name=section, section_events=events)


def parse_body(
    resume_name: str,
    contact_section: ResumeContactDetails,
    info_sections: List[ResumeInfoSection],
):
    return ResumeBody(
        resume_name=resume_name,
        contact_section=contact_section,
        info_sections=info_sections,
    )


# ----------


# Main Logic
# ----------
def main(resume_name: str = RESUME_NAME, locale: LocaleType = LOCALE) -> ResumeBody:
    return parse_body(
        contact_section=parse_contacts(load_contact_details(), locale),
        info_sections=[
            parse_info_section("Experience", parse_events(load_event_info()))
        ],
        resume_name=resume_name,
    )


if __name__ == "__main__":
    main()
# ----------
