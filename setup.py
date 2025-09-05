import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_desc = f.read()
    
__version__ ="0.0.1"

REPO_NAME = "Text-Summarizer-Project"
USER_NAME = "Mouna"
SRC_REPO = "textsummarizer"
Email = "msrisai.p@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version= __version__,
    author=USER_NAME,
    author_email=Email,
    description="A small Python package for NLP App",
    long_description_content="text/markdown",
    url = f"https://github.com/{USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker" : f"https://github.com/{USER_NAME}/{REPO_NAME}/issues",
    },
package_dir={"":"src"},
packages=setuptools.find_packages(where="src")
)