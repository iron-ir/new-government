from uuid import uuid4


def image_upload_to(instance, file_name):
    _uuid = uuid4()
    _uuid2 = uuid4()
    ext = file_name.split('.')[-1]
    return "images/{}/{}.{}".format(str(_uuid), str(_uuid2), ext)


def file_upload_to(instance, file_name):
    _uuid = uuid4()
    _uuid2 = uuid4()
    ext = file_name.split('.')[-1]
    return "files/{}/{}.{}".format(str(_uuid), str(_uuid2), ext)
