import subprocess as sp


def check_if_package_is_setup(package, version_command='-v'):
    try:
        sp.check_call([package, version_command])
        return True
    except:
        return False


def php_is_setup():
    return check_if_package_is_setup('php')


def composer_is_setup():
    return check_if_package_is_setup('composer', '--version')


def check_package(package):
    if hasattr(mapping, package):

        return getattr(mapping, package)()
    else:
        return False


mapping = {
    'composer': composer_is_setup,
    'php': php_is_setup
}
