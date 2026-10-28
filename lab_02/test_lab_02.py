import lab_02

def test_add():
    lab_02.list.clear()

    lab_02.addNewElement("Bob", "111", "bob@gmail.com", "KB-251")

    assert len(lab_02.list) == 1
    assert lab_02.list[0]["name"] == "Bob"

def test_delete():
    lab_02.list.clear()

    lab_02.addNewElement("Bob", "111", "bob@gmail.com", "KB-251")
    result = lab_02.deleteElement("Bob")

    assert result == True
    assert len(lab_02.list) == 0

def test_update():
    lab_02.list.clear()

    lab_02.addNewElement("Bob", "111", "bob@gmail.com", "KB-251")
    result = lab_02.updateElement(
        "Bob", "Anna", "222", "anna@gmail.com", "KB-252"
    )

    assert result == True
    assert len(lab_02.list) == 1
    assert lab_02.list[0]["name"] == "Anna"

def test_save_load(tmp_path):
    lab_02.list.clear()

    lab_02.addNewElement("Bob", "111", "bob@gmail.com", "KB-251")

    fileName = tmp_path / "test.csv"
    lab_02.saveList(fileName)

    lab_02.list.clear()
    lab_02.loadList(fileName)

    assert len(lab_02.list) == 1
    assert lab_02.list[0]["name"] == "Bob"