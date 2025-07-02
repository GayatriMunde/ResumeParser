from setuptools import setup, find_packages

setup(
    name='resume-matcher',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'sentence-transformers>=2.5.1',
        'python-docx>=1.1.0',
        'scikit-learn>=1.3.0',
        'numpy>=1.23',
        'torch>=1.13.0'
    ],
    author='Gayatri Munde',
    author_email='gayatrimunde.ar@gmail.com',
    description='AI-powered resume and job description matcher with semantic scoring',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/GayatriMunde/ResumeParser',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
    ],
    python_requires='>=3.8'
)
