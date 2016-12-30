import unicodedata, re
import os,ctypes,platform
from vgen.services import hostfileupdate
from pwd import getpwnam


def slugify(string):
    slug = unicodedata.normalize("NFKD",unicode(string)).encode("ascii", "ignore")
    slug = re.sub(r"[^\w]+", " ", slug)
    slug = "-".join(slug.lower().strip().split())
    return slug


def make_directories(*paths):
    for path in paths:
            if not os.path.exists(path):
                os.makedirs(path)


def check_if_hostname_is_valid(domain):
    return hostfileupdate.isValidHostname(domain)


def check_if_running_as_administrator():
    if platform.system() == 'Windows':
        try:
            is_admin = os.getuid() == 0
        except AttributeError:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    else:
        is_admin = os.geteuid() == 0

    return is_admin

def change_directory_owner_recursively(path, owner):
    uid = getpwnam(owner).pw_uid
    gid = getpwnam(owner).pw_gid

    os.chown(path, uid, gid)
    for item in os.listdir(path):
        itempath = os.path.join(path, item)
        if os.path.isfile(itempath):
            os.chown(itempath, uid, gid)
        elif os.path.isdir(itempath):
            os.chown(itempath, uid, gid)
            change_directory_owner_recursively(itempath,owner)
