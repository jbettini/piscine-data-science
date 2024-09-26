def all_thing_is_obj(object: any) -> int:
    match object:
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

