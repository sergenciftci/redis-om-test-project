
from redis_om import Migrator, JsonModel, Field, EmbeddedJsonModel
from typing import List

class User(EmbeddedJsonModel):
    first_name: str = Field(index=True)
    last_name: str = Field(index=True)

class Workspace(JsonModel):
    title: str = Field(index=True)
    users: List[User] = Field(index=True)

Migrator().run()

jason_doe = User(first_name="Jason", last_name="Doe")
jason_doe.save()
john_bourne = User(first_name="John", last_name="Bourne")
john_bourne.save()
jason_bourne = User(first_name="Jason", last_name="Bourne")
jason_bourne.save()

first_workspace = Workspace(title="first workspace", users=[jason_doe, john_bourne])
first_workspace.save()
second_workspace = Workspace(title="second workspace", users=[jason_bourne])
second_workspace.save()

print(Workspace.find().all())
# [Workspace(pk='01GSCYRVVFQW4XRY7EG4YC7VDJ', title='first workspace', users=[User(pk='01GSCYRVVDQCF3RQYMM23E0KR2', first_name='Jason', last_name='Doe'), User(pk='01GSCYRVVE80BGT8B0HN7FEFQZ', first_name='John', last_name='Bourne')]), Workspace(pk='01GSCYRVVF1MAGWG0RWVVV74A2', title='second workspace', users=[User(pk='01GSCYRVVEYZ1NK0QJE5KEAX12', first_name='Jason', last_name='Bourne')])]
print(Workspace.find((Workspace.users.first_name == "Jason"), (Workspace.users.last_name == "Bourne")).all())
# [Workspace(pk='01GSCYRVVFQW4XRY7EG4YC7VDJ', title='first workspace', users=[User(pk='01GSCYRVVDQCF3RQYMM23E0KR2', first_name='Jason', last_name='Doe'), User(pk='01GSCYRVVE80BGT8B0HN7FEFQZ', first_name='John', last_name='Bourne')]), Workspace(pk='01GSCYRVVF1MAGWG0RWVVV74A2', title='second workspace', users=[User(pk='01GSCYRVVEYZ1NK0QJE5KEAX12', first_name='Jason', last_name='Bourne')])]