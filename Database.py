import Pencatatan
import json


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
        riwhutang = data["rh"]
    except KeyError: riwhutang = []
    return [users, riwayat, hutang, riwhutang]
