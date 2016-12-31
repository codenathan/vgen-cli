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


def laravel_is_setup():
    return check_if_package_is_setup('laravel', '--version')


def check_packages(packages):
    installed = {}

    for package in packages:
        answer = False
        if package in mapping:
            answer = mapping[package]()

        installed[package] = answer

    return installed


mapping = {
    'composer': composer_is_setup,
    'php': php_is_setup,
    'laravel': laravel_is_setup
}
