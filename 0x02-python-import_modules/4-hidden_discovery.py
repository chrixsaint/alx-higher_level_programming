#!/usr/bin/python3
if _name_ == "_main_":
    import hidden_4

    names = dir(hidden_4)
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)
