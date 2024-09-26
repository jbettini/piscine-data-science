def all_thing_is_obj(object: any) -> int:
    match object:
        case int(object):
            print(f"Int : {type(object)}")
        case float(object):
            print(f"Float : {type(object)}")
        case complex():
            print(f"Complex : {type(object)}")
        case frozenset(object):
            print(f"FrozenSet : {type(object)}")
        case bool(object):
            print(f"Bool : {type(object)}")
        case bytes(object):
            print(f"Bytes : {type(object)}")
        case bytearray(object):
            print(f"ByteArray : {type(object)}")
        case memoryview():
            print(f"MemoryView : {type(object)}")
        case None:
            print(f"None : {type(object)}")
        case list(object):
            print(f"List : {type(object)}")
        case tuple(object):
            print(f"Tuple : {type(object)}")
        case dict(object):
            print(f"Dict : {type(object)}")
        case set(object):
            print(f"Set : {type(object)}")
        case str(object):
            if object == "Brian":
                print(f"Brian is in the kitchen : {type(object)}")
            else:
                print(f"Str : {type(object)}")
        case _:
            print(f"Type not found")
    return 42

ft_int = 21
ft_float = 3.14
ft_complex = 1 + 2j
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_dict = {"Hello": "titi!"}
ft_set = {"Hello", "tutu!"}
ft_frozenset = frozenset({"Hello", "tutu!"})
ft_bool = True
ft_bytes = b'abc'
ft_bytearray = bytearray(b'abc')
ft_memoryview = memoryview(b'abc')
ft_none = None
ft_str = "Bonjour"

all_thing_is_obj(ft_int)
all_thing_is_obj(ft_float)
all_thing_is_obj(ft_complex)
all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_dict)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_frozenset)
all_thing_is_obj(ft_bool)
all_thing_is_obj(ft_bytes)
all_thing_is_obj(ft_bytearray)
all_thing_is_obj(ft_memoryview)
all_thing_is_obj(ft_none)
all_thing_is_obj(ft_str)
all_thing_is_obj("Brian")

print(all_thing_is_obj(10))