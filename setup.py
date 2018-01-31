from setuptools import setup, find_packages

setup(
    name='cocasync',
    version='0.0.2',
    description='An async Python API wrapper for the COC API',
    long_description="async python wrapper for the COC API. Also, we don't yet have a good description so this empty page will have to do.",
    url='https://github.com/cree-py/cocasync',
    author='Umbresp',
    author_email='creepy.org3301@gmail.com',
    license='MIT',
    keywords=['coc clash-of-clans clash clans cocasync api-wrapper async'],
    packages=find_packages(),
    install_requires=['aiohttp', 'python-box']
)
