from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="TredingViewData",
    version="0.1",
    packages=["TredingViewData"],
    license="MIT License",
    author="@RavalMeet",
    author_email="ravalmeett@gmail.com",
    description="TradingView Historical Data Downloader Tool",
    long_description_content_type="text/markdown",
    long_description=long_description,
    install_requires=[
        "setuptools",
        "pandas",
        "websocket-client",
        "requests"
    ],
)
