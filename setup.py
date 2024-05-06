from setuptools import setup


def readme():
    with open("README.md", "r", encoding="utf-8") as rdm_f:
        return rdm_f.read()


setup(
    name="CreateRandomADOFAI",
    version="0.0.0.1",
    author="Ger",
    author_email="gerutrogame@gmail.com",
    description="Adodai)",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Gerutro/CreateRandomADOFAI",
    license="MIT License, see LICENCE file",
    packages=["CreateRandomADOFAI"],
    classifiers=[
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'],
    keywords="extra exception lib library ",
    project_urls={
        "Documentation": "https://github.com/Gerutro"
    },
    python_requires=">=3.9",
)
