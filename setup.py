from setuptools import setup

scripts=['ft.py']

entry_points = { 'console_scripts': ['fc2o=fmttrans.pipelines:fc2o'] }

with open('readme.md','r') as f:
    description=f.read()
setup(
    name='formattrans',
    version='0.1.0dev',
    packages=['fmttrans'],
    scripts=scripts,
    url='https://github.com/btrspg/formattrans.git',
    license='',
    author='CHEN, Yuelong',
    author_email='yuelong.chen.btr@gmail.com',
    description=description,
    entry_points=entry_points
)
