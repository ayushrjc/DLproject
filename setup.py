from setuptools import find_packages, setup

def get_requierements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for re in requirements]

        if HYPEN_E_DIT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setip(

    name = "Xray",
    version = "0.0.1",
    author = "Ayush Raj Choudhary",
    author_email = "ayushrajchoudhary@gmail.com",
    install_requires=get_requirements(),
    package=find_packages()

)