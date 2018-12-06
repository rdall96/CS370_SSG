import setuptools

setuptools.setup(
    name="Flock_SSG",
    version="0.0.1",
    author="Derek Connelly, Ricky Dall‘Armellina, Dan Levy, Lukas Mallory",
    author_email="conneld@sunyit.edu",
    description="A static site generator",
    long_description="A simple website generation tool in Python should be able to gather information on how the website should look like from the user. This information includes, theme, colors, data/text to display. The user inputs one or more markdown files (file.md) to the website generator.The program then takes these files, indexes them and converts them to working HTML. A folder with the whole website/converted files is then created with the correct hierarchy.",
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
