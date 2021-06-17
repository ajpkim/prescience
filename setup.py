from setuptools import setup

setup(
    name="prescience",
    version='0.0.1',
    url="https://github.com/ajpkim/prescience",
    author="Alex Kim",
    author_email="alexjpkim@protonmail.com",
    description='Track and improve predictions',
    # py_modules=["prescience"],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Langauge :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)"
    ],
    entry_points = {
        'console_scripts': [
            'prescience = main:main'
        ]
    },
)
