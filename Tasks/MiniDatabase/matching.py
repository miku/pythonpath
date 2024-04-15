db = []

def insert(db, record):
    db.append(record)

def select(db, query):
    result = []
    for record in db:
        matching = 0
        for k, v in query.items():
            if record.get(k) == v:
                matching += 1
        if matching == len(query):
            result.append(record)
    return result
            
                


db = []

insert(db, {"a": 1})
insert(db, {"a": 2})

print(select(db, {"a": 1})) # [{'a': 1}]

db = []

insert(db, {"a": 1, "b": 2})
insert(db, {"a": 2, "b": 2})
insert(db, {"a": 2, "b": 2, "c": 3})

print(select(db, {"a": 2, "b": 2})) # [{'a': 2, 'b': 2}, {'a': 2, 'b': 2, 'c': 3}]
