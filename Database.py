import Pencatatan
import json


def Convert(data):
    if isinstance(data, list):
        return {
            "__type__": "list",
            "data": {i: Convert(v) for i, v in enumerate(data)}
        }
    elif isinstance(data, dict):
        return {k: Convert(v) for k, v in data.items()}
    else:
        return data


def Revert(data):
    if isinstance(data, dict) and "__type__" in data:
        if data["__type__"] == "list":
            return [Revert(v) for k, v in sorted(data["data"].items())]
    elif isinstance(data, dict):
        return {k: Revert(v) for k, v in data.items()}
    else:
        return data


def Save(simpan):
    with open("data.json", "w") as f:
        json.dump(simpan, f)


def Open():
    with open("data.json", "r") as f:
        loaded = json.load(f)
    return loaded


def akses():
    data = Open()
    try:
        users = data["users"]
    except KeyError: users = []
    try:
        riwayat = data["riwayat"]
    except KeyError: riwayat = []
    try:
        hutang = data["hutang"]
    except KeyError: hutang = []
    try:
        riwhutang = data["rihu"]
    except KeyError: riwhutang = []
    return [users, riwayat, hutang, riwhutang]
