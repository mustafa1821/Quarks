"""
Backtrader PRO - Advanced Backtesting Program
Setup script for package installation
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="backtrader-pro",
    version="1.0.0",
    author="Backtrader PRO Team",
    author_email="your.email@example.com",
    description="Professional-grade backtesting program for trading strategies",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/backtrader-pro",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Financial and Insurance Industry",
        "Topic :: Office/Business :: Financial :: Investment",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        "backtrader>=1.9.78",
        "yfinance>=0.2.0",
        "pandas>=1.3.0",
        "numpy>=1.19.0",
        "matplotlib>=3.3.0",
    ],
    entry_points={
        "console_scripts": [
            "backtrader-pro=backtest_program_pro:main",
        ],
    },
)
