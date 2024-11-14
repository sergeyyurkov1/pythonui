import sys

from ruamel.yaml import YAML

yaml = YAML(typ="rt", pure=True)
yaml.preserve_quotes = True
yaml.default_flow_style = False


def read_yaml(path: str = "settings.yaml") -> dict:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return yaml.load(f)

    except FileNotFoundError:
        write_yaml({})
        read_yaml()


def write_yaml(
    data: dict,
    path: str = "settings.yaml",
) -> None:
    try:
        with open(path, "w", encoding="utf-8") as f:
            yaml.dump(data, f)
    except Exception as e:
        print(str(e))
        sys.exit()
