from distutils.core import setup

setup(
    name='EbsAnalyzer',
    packages=['EbsAnylzer'],
    version='0.1',
    license='MIT',
    description='Analyze ebook usage data for evidence based selection models',
    author='Eike T. Spielberg',
    author_email='Eike.Spielberg@uni-due.de',
    url='https://github.com/ETspielberg/EbsAnalyzer',  # Provide either the link to your github or to your website
    download_url='https://github.com/user/reponame/archive/v_01.tar.gz',
    keywords=['Analysis', 'E-Books', 'Evidence Based Selection'],  # Keywords that define your package best
    install_requires=[
        'numpy',
        'statistics',
        'math',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  # Again, pick a license
        'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
