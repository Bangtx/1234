def is_exists(data, list_data):
    try:
        index = list_data.index(data)
        return True
    except:
        return False


def get_category_mom(list_category):
    result = list()
    for i in list_category:
        if i.id_mom == -1:
            result.append(i)
    return result


def get_category_child_of_mom(list_category_mom, list_category):
    result = dict()
    for i in list_category_mom:
        result[i.id] = list()

    for i in list_category:
        if i.id_mom != -1:
            result[i.id_mom].append(i)

    return result
