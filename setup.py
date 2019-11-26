from setuptools import setup
from setuptools import find_packages

from two import version

NAME = "two"
AUTHOR = "Ailln"
EMAIL = "kinggreenhall@gmail.com"
URL = "https://github.com/Ailln/two"
LICENSE = "MIT License"
DESCRIPTION = "two."

if __name__ == "__main__":
    setup(
        name=NAME,
        version=version.VERSION,
        author=AUTHOR,
        author_email=EMAIL,
        url=URL,
        license=LICENSE,
        description=DESCRIPTION,
        packages=find_packages(),
        include_package_data=True,
        install_requires=open("./requirements.txt", "r").read().splitlines(),
        long_description=open("./README.md", "r").read(),
        long_description_content_type='text/markdown',
        entry_points={
            "console_scripts": [
                "two=two.shell:run"
            ]
        },
        package_data={
            "two": ["src/*.txt"]
        },
        zip_safe=True,
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ]
    )
