from CreateRandomADOFAI.adofai_exceptions import EaseException

with open('../src/eases.txt') as f:
    eases_all = [line.rstrip() for line in f]


def eases_find(ease_find: str):
    """

    :param ease_find: ease for find. Can be 'In', 'Out', 'In-Out' or name of ease, for example: 'Sine', 'In-Out Sine'
    :return:
    """
    if ease_find == "In":
        ease_find_inout = "In-Out"
    else:
        ease_find_inout = "In"
    result = [ease for ease in eases_all if ease.startswith(ease_find) and not ease.startswith(ease_find_inout)]
    if result:
        pass
    else:
        raise EaseException("Invalid type. Use 'In', 'Out', 'In-Out' or name of ease. See all eases in file "
                            "'../src/eases.txt'")

    return result
