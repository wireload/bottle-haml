from setuptools import setup

dependencies = [
    'bottle',
    'pyhaml'
]

setup(
    name="bottle-haml",
    packages=["bottlehaml",],
    install_requires=dependencies,
    version="0.1.4",
    author="Zachary Jones",
    author_email="me@zacharytamas.com",
    license="BSD",
    url="https://github.com/wireload/bottle-haml",
    long_description=open('README.md').read(),
    package_data = {
        '': ['*.md', '*.txt']
    },
    include_package_data=True
)