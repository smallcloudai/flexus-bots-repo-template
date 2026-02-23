from setuptools import setup, find_packages


setup(
    name="flexus_my_bots",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "": ["*.json", "*.md", "*.webp", "*.png"],
    },
    install_requires=[
        "flexus-client-kit @ git+https://github.com/smallcloudai/flexus-client-kit.git",
    ],
    author="Flexus Team",
    author_email="",
    long_description_content_type="text/markdown",
    url="https://github.com/smallcloudai/flexus-bots-repo-template",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
