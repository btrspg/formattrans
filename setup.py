from setuptools import setup

scripts=['ft.py']

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
    description=description
)
