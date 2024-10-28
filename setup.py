import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="textsummarizer",
    version="0.0.2",
    author="Sourav Das",
    author_email="DlTjW@example.com",
    description="A small package for text summarization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/souravdas1999/Text-Summarizer",
    project_urls={
        "Bug Tracker": "https://github.com/souravdas1999/Text-Summarizer/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",    
    ],
    package_dir={"":"src"}, 
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",     
)