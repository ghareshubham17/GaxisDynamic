from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in gaxisdynamic/__init__.py
from gaxisdynamic import __version__ as version

setup(
	name="gaxisdynamic",
	version=version,
	description="sss",
	author="shubham",
	author_email="aa",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
