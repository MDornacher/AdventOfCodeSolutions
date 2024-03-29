from setuptools import setup

setup(
    name="AdventOfCodeSolutions",
    version="0.1",
    packages=["aocs"],
    author="mdornacher",
    author_email="manuel.dornacher@gmail.com",
    description="My personal solutions for the advent of code challenges",
    install_requires=[
        "advent-of-code-data",
        "numpy",
        "scipy",
        "matplotlib",
        "treelib",
        "tqdm",
    ],
    extras_requires=["black"],
    tests_require=["pytest"],
)
