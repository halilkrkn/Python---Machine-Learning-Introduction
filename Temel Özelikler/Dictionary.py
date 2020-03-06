

sozluk = {

        "book": "kitap",
        "table":"masa"

}

sozluk2 = dict(kitap = "book", masa="table")
print(sozluk2)

sozluk["book"] = "kitap 1"
sozluk["pencil"] = "kalem"
#del(sozluk["book"])
print(sozluk)