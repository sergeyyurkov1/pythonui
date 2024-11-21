import inspect
import os
import pathlib
import sys

from ruamel.yaml import YAML

yaml = YAML(typ="rt", pure=True)
yaml.preserve_quotes = True
yaml.default_flow_style = False

PATH = pathlib.Path(__file__).parent


class NamespaceMixin:
    @property
    def namespace(self):
        return str(pathlib.Path(inspect.getfile(self.__class__)).parent).rsplit(
            maxsplit=1, sep=os.sep
        )[1]


def log_to_txt(text: str) -> None:
    with open(PATH / "log.txt", "a") as f:
        f.write(text + "\n")


def read_yaml(path: str = PATH / "settings.yaml") -> dict:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return yaml.load(f)
    except FileNotFoundError:
        return {}


def write_yaml(
    data: dict,
    path: str = PATH / "settings.yaml",
) -> None:
    try:
        with open(path, "w", encoding="utf-8") as f:
            yaml.dump(data, f)
    except Exception as e:
        print(str(e))
        sys.exit()


class NamespaceAlreadyExistsException(Exception): ...


def register_namespace(namespace: str) -> None:
    settings = read_yaml()
    print(settings)
    if settings.get(namespace, None) is None:
        settings[namespace] = {}
        write_yaml(settings)
    # else:
    #     raise NamespaceAlreadyExistsException(
    #         "Namespace already exists. Please rename your plugin."
    #     )


class SettingsMixin(NamespaceMixin):
    def write_settings(
        self, key: str, value: str, namespace: str | None = None
    ) -> None:
        if namespace is None:
            namespace = self.namespace

        settings = read_yaml()

        try:
            settings[namespace][key] = value
        except KeyError:
            print("Setting not found. Please check namespace or key.")
        else:
            write_yaml(settings)

    def read_settings(self, key: str, namespace: str | None = None) -> any:
        if namespace is None:
            namespace = self.namespace

        settings = read_yaml()

        try:
            value = settings.get(namespace).get(key)
        except AttributeError:
            print("Setting not found. Please check namespace or key.")
        else:
            return value

    def search_key(self, key) -> any:
        return _search_key(read_yaml(), key)


def _search_key(dictionary, key):
    if key in dictionary:
        return dictionary[key]
    for value in dictionary.values():
        if isinstance(value, dict):
            if _search_key(value, key):
                return value[key]
    return False
