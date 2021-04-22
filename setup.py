from setuptools import setup
from setuptools import find_packages

NAME = "two"
AUTHOR = "Ailln"
EMAIL = "kinggreenhall@gmail.com"
URL = "https://github.com/Ailln/two"
LICENSE = "MIT License"
DESCRIPTION = "😏随机一句「中二」的台词！"

if __name__ == "__main__":
    setup(
        name=NAME,
        version="0.1.3",
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
        package_data={
            "two": ["src/*.txt"]
        },
        zip_safe=True,
        classifiers=[
            "Programming Language :: Python :: 3",
            f"License :: OSI Approved :: {LICENSE}",
            "Operating System :: OS Independent",
        ]
    )
