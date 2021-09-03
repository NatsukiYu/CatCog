from setuptools import setup, find_packages

with open('requirements.txt', 'r') as fp:
    requirements = fp.read().splitlines()

setup(
    name='CatCog',
    version='1.0.0',
    license='MIT',
    description='Send a message when the cat walks on the keyboard.',
    author='@natsuki__yu',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=requirements,
)
