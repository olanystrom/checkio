from collections import abc

def flatten(dictionary):
    result = dict()
    if not isinstance(dictionary,abc.Mapping):
        return {dictionary: ""}
    for level in dictionary.keys():
        thiskey, thislevel = nextlevel(level,dictionary[level])
        print(thislevel)
        result.update(thislevel)
    return result

def nextlevel(name, dictionary):
    if not (isinstance(dictionary, abc.Mapping)):
        return (name, {name: dictionary})
    if(len(dictionary) == 0):
        return (name, {name: ""})
    for level in dictionary.keys():
        newname = f"{name}/{level}"
        ret = (newname, {newname: dictionary[level]})
        if isinstance(dictionary[level], abc.Mapping):
            return nextlevel(newname,dictionary[level])
        else:
            print(ret)
            return ret





if __name__ == '__main__':
    # test_input = {"key": {"deeper": {"more": {"enough": "value"}}}}
    # print(' Input: {}'.format(test_input))
    # print('Output: {}'.format(flatten(test_input)))

    # #These "asserts" using only for self-checking and not necessary for auto-testing
    # assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    # assert flatten(
    #     {"key": {"deeper": {"more": {"enough": "value"}}}}
    # ) == {"key/deeper/more/enough": "value"}, "Nested"
    # assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({"name": {
                        "first": "One",
                        "last": "Drone"},
                    "job": "scout",
                    "recent": {},
                    "additional": {
                        "place": {
                            "zone": "1",
                            "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}
    print('You all set. Click "Check" now!')