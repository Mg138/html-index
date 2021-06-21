from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name='html_index',
    version='0.1',
    author='Madeline Sparkle',
    author_email='muguang138@gmail.com',
    license='MIT License',
    description='HTML file indexing generator.',
    long_description='A python script that generates index.html files for file indexing.',
    long_description_content_type="text",
    url='https://github.com/Mg138/html_index',
    py_modules=['html_index'],
    packages=find_packages(),
    install_requires=[requirements],
    python_requires='>=3.8',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points='''
        [console_scripts]
        index=html_index:main
    '''
)
