from setuptools import setup

setup(
    name="projectgoombastomp",
    version="1.0.4",
    packages=["projectgoombastomp"],
    include_package_data=True,
    install_requires=["fpdf2"],
    entry_points={
        'console_scripts': [
            'goomba=projectgoombastomp.cli:main',
        ],
    },
    author="Lonnie",
    description="Command-line tool to merge folder structure and contents into Markdown/PDF/ZIP with UTF-8 support",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
