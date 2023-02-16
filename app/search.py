
from redis_om import Migrator, JsonModel, Field
from typing import List

class User(JsonModel):
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
# [Workspace(pk='01GSCYNT0366QJ4MAKW049GKFP', title='first workspace', users=[User(pk='01GSCYNT012PQPV8Y5N7S6J0B3', first_name='Jason', last_name='Doe'), User(pk='01GSCYNT022ZP2AAKZCVEQ6SZP', first_name='John', last_name='Bourne')]), Workspace(pk='01GSCYNT03B8Y67RW9VK5FGQWV', title='second workspace', users=[User(pk='01GSCYNT02PE0P2XT4K2A3XCDV', first_name='Jason', last_name='Bourne')])]
print(Workspace.find((Workspace.users.first_name == "Jason"), (Workspace.users.last_name == "Bourne")).all())
# [Workspace(pk='01GSCYNT0366QJ4MAKW049GKFP', title='first workspace', users=[User(pk='01GSCYNT012PQPV8Y5N7S6J0B3', first_name='Jason', last_name='Doe'), User(pk='01GSCYNT022ZP2AAKZCVEQ6SZP', first_name='John', last_name='Bourne')]), Workspace(pk='01GSCYNT03B8Y67RW9VK5FGQWV', title='second workspace', users=[User(pk='01GSCYNT02PE0P2XT4K2A3XCDV', first_name='Jason', last_name='Bourne')])]
users = User.find((User.first_name == "Jason") & (User.last_name == "Bourne")).all()
print(users)
# []
user_pks = [u.pk for u in users]
for user in users:
    print(Workspace.find(Workspace.users.pk == user.pk).all())