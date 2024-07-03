from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in sales_management/__init__.py
from sales_management import __version__ as version

setup(
	name="sales_management",
	version=version,
	description="Sales Management System",
	author="Muhammad Essam",
	author_email="mohamed.essam68.me@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
