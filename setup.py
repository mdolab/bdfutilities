from setuptools import setup
import re

__version__ = re.findall(r"""__version__ = ["']+([0-9\.]*)["']+""", open("bdfutilities/__init__.py").read())[0]

setup(
    name="bdfutilities",
    version=__version__,
    description="bdfUtilities is a package to create, modify, and use BDF meshes.",
    keywords="BDF",
    author="",
    author_email="",
    url="https://github.com/eirikurj/bdfutilities",
    license="Apache 2.0",
    packages=["bdfutilities"],
    package_data={"bdfutilities": ["*.so"]},
    install_requires=["numpy>=1.16", "scipy", "pyNastran"],
    extras_require={
        "testing": ["mdolab-baseclasses>=1.3", "testflo", "parameterized"],
    },
    classifiers=["Operating System :: Linux", "Programming Language :: Python, Fortran"],
    entry_points={"console_scripts": ["bdf_utils = bdfutilities.bdf_utils:main"]},
)
