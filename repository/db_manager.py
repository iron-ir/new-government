def paginate(objs, page=1, page_size=10):
    len_objs = len(objs)
    paginate_objects = []

    start = (page - 1) * page_size
    stop = start + page_size

    if start > len_objs:
        return None
    if stop > len_objs:
        stop = len_objs

    for i in range(start, stop):
        paginate_objects.append(objs[i])

    return paginate_objects
