# setup.py

from setuptools import setup, find_packages

setup(
    name='package',
    version='0.1.0',
    description='Terminal AI command line interface',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Aditya',
    author_email='your@email.com',
    url='https://github.com/yourusername/yourproject',
    packages=find_packages(),
    install_requires=[
        'langchain_google_genai',
        'dotenv',
        'langchain_core'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.10',
)
