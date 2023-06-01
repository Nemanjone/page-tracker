from setuptools import setup, find_packages

setup(
    name='page-tracker',
    version='1.0.0',
    author='Nemanja Balaban',
    author_email='nemanjabalaban111@gmail.com',
    description='A short description of your package',
    # packages=['/home/nemanjab/page-tracker/'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask",
        "redis",
    ],
)
