import JsonDiff

def basic():
    a = {'a':'b'}
    b = {'a':'b'}
    js = JsonDiff.JsonDiff(a, b)

    js.check(a, b)
    print js.tell_difference()
    # no difference

    a = {'a':'b'}
    b = {'a':'b', 'b':'a', 'c':'d'}
    js = JsonDiff.JsonDiff(a, b)

    js.check(a, b)
    js.save_diff(a, b)
    print js.tell_difference()
    # tell the difference

def t_list():
    # cant operate ...
    a = {'a':'b', 'b':'a', 'c':'d'}
    b = {'a':'b', 'b':'a', 'c':'d'}
    js = JsonDiff.JsonDiff(a, b)

    js.check(a, b)
    js.save_diff(a, b)
    print js.tell_difference()

#basic()
t_list()
