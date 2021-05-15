from importlib.resources import read_binary, read_text
import json

STRINGS_DAT = read_binary("unitypack", "strings.dat")
UNITY_CLASSES = json.loads(read_text("unitypack", "classes.json"))


def UnityClass(i):
	return UNITY_CLASSES.get(str(i), "<Unknown #%i>" % (i))
