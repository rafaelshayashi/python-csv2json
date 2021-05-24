from setuptools import setup, find_packages

setup(
    name='csv2json',
    version='0.1.0',
    scripts=['./bin/csv2json'],
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/rafaelshayashi/python-csv2json.git',
    license='MIT',
    author='Rafael Simionato Hayashi',
    author_email='rafaelshayashi@gmail.com',
    description='simple cli for testing porpuse'
)
