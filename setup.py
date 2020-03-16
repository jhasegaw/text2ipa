import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="text2ipa",
    version="0.0.1",
    author="Mark Hasegawa-Johnson",
    author_email="jhasegaw@illinois.edu",
    description="Convert text to IPA, in any language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jhasegaw/text2ipa",
    packages=setuptools.find_packages(),
    scripts=['t2ipa'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

