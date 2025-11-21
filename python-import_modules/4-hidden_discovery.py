#!/usr/bin/python3
if __name__ == "__main__":
    import marshal
    import types

    # Load the compiled module
    with open("/tmp/hidden_4.pyc", "rb") as f:
        f.read(16)  # skip the header (magic + timestamp)
        code = marshal.load(f)

    # Collect all names
    names = [name for name in code.co_names if not name.startswith("__")]

    # Print each name in alpha order
    for name in sorted(names):
        print(name)
