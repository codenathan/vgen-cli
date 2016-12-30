import unicodedata, re
import os


def slugify(string):
    slug = unicodedata.normalize("NFKD",unicode(string)).encode("ascii", "ignore")
    slug = re.sub(r"[^\w]+", " ", slug)
    slug = "-".join(slug.lower().strip().split())
    return slug


def mkdir(*paths):
    for path in paths:
            if not os.path.exists(path):
                os.makedirs(path)
