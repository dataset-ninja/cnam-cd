from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "CNAM-CD"
PROJECT_NAME_FULL: str = "CNAM-CD: A Multi-Class Change Detection Dataset"
HIDE_DATASET = False  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.Apache_2_0(source_url="https://github.com/Silvestezhou/CNAM-CD/blob/main/LICENSE")
APPLICATIONS: List[Union[Industry, Domain, Research]] = [
    Domain.Geospatial(),
    Industry.UrbanPlanning(),
]
CATEGORY: Category = Category.Aerial(extra=[Category.Environmental(), Category.Satellite()])

CV_TASKS: List[CVTask] = [
    CVTask.InstanceSegmentation(),
    CVTask.SemanticSegmentation(),
    CVTask.ObjectDetection(),
]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.InstanceSegmentation()]

RELEASE_DATE: Optional[str] = "2023-05-03"  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = None

HOMEPAGE_URL: str = "https://github.com/Silvestezhou/CNAM-CD"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 2700316
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/cnam-cd"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[
    Union[str, dict]
] = "https://drive.google.com/file/d/1w6tDfE-F4o3Q4KGh1jzzIRpIlIUIXXrx/view?usp=sharing"
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = {
    "background": [230, 25, 75],
    "bare ground": [60, 180, 75],
    "impervious surface": [255, 225, 25],
    "vegetation": [0, 130, 200],
    "other": [245, 130, 48],
    "water bodies": [145, 30, 180],
}
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

# If you have more than the one paper, put the most relatable link as the first element of the list
PAPER: Optional[Union[str, List[str]]] = "https://www.mdpi.com/2072-4292/15/9/2464"
BLOGPOST: Optional[Union[str, List[str]]] = None
CITATION_URL: Optional[str] = None
AUTHORS: Optional[List[str]] = [
    "Zhou, Yanpeng",
    "Wang, Jinjie",
    "Ding, Jianli",
    "Liu, Bohua",
    "Weng, Nan",
    "Xiao, Hongzhi",
]
AUTHORS_CONTACTS: Optional[List[str]] = ["zyp@stu.xju.edu.cn"]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = "Xinjiang University, China"
ORGANIZATION_URL: Optional[Union[str, List[str]]] = "https://www.xju.edu.cn/"

# Set '__PRETEXT__' or '__POSTTEXT__' as a key with value:str to add custom text. e.g. SLYTAGSPLIT = {'__POSTTEXT__':'some text}
SLYTAGSPLIT: Optional[Dict[str, Union[List[str], str]]] = {
    "__PRETEXT__": "Alternatively, the dataset could be split into 2512 groups set by ***img_id***. Every group has 2 images: ***A*** (before) and ***B*** (after). Ground truth masks assigned to ***B***"
}
TAGS: Optional[List[str]] = ['multi-view']



SECTION_EXPLORE_CUSTOM_DATASETS: Optional[List[str]] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "project_name_full": PROJECT_NAME_FULL or PROJECT_NAME,
        "hide_dataset": HIDE_DATASET,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["blog"] = BLOGPOST
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["authors_contacts"] = AUTHORS_CONTACTS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    settings["explore_datasets"] = SECTION_EXPLORE_CUSTOM_DATASETS

    return settings
