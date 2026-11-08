import importlib


def resolve_import(dotted: str):
    mod, _, attr = dotted.rpartition(".")
    return getattr(importlib.import_module(mod), attr)
