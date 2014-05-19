try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requires = ['requests>=2.1.0']

setup(
    name='mapmyfitness',
    version='0.1.1',
    description='A python wrapper for the MapMyFitness API',
    author='Jason Sanford',
    author_email='jasonsanford@gmail.com',
    url='https://github.com/JasonSanford/mapmyfitness-python',
    packages= ['mapmyfitness', 'mapmyfitness.api', 'mapmyfitness.objects', 'mapmyfitness.validators',],
    install_requires=requires,
    license='Apache License',
)