import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="clock_timer",
    version="0.1.0",
    author="Cyberbolt",
    author_email="735245473@qq.com",
    description="clock_timer 是 Python 下的时间库，用于时间字符串处理，可在 Web 开发、数据分析 等领域使用。该库 80% 基于 datetime ，使用该库，您能更人性化地处理时间字符串，而无需每次查询 datetime 繁琐的接口。",
    long_description=long_description,
    long_description_content_type="text/markdown",    
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'python-dateutil>=2.8.2',
        'six>=1.16.0'
    ]    
)