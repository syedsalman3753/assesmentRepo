data = {

    "employees": [

        {"id": 1, "name": "Alice", "dept": "Data"},

        {"id": 2, "name": "Bob", "dept": "IT"},

        {"id": 3, "name": "Charlie", "dept": "Data"},

    ]

}

for e in data['employees']:
    if e['dept'] == "Data":
        print(e['name'])