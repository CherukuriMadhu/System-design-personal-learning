"""6. Builder Pattern ⭐⭐⭐
Definition

The Builder Pattern separates the construction of a complex object from its representation.

It is useful when an object has:

many parameters
optional parameters
complex construction steps
Problem

Imagine:

User(
    name,
    age,
    email,
    phone,
    address,
    gender,
    ...
)

Constructor becomes difficult to understand.

Builder makes it cleaner.

Code
class User:

    def __init__(self, name, age=None, email=None, phone=None):
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone

    def __str__(self):
        return (
            f"User(name={self.name}, "
            f"age={self.age}, "
            f"email={self.email}, "
            f"phone={self.phone})"
        )


class UserBuilder:

    def __init__(self, name):
        self.name = name
        self.age = None
        self.email = None
        self.phone = None

    def set_age(self, age):
        self.age = age
        return self

    def set_email(self, email):
        self.email = email
        return self

    def set_phone(self, phone):
        self.phone = phone
        return self

    def build(self):
        return User(
            self.name,
            self.age,
            self.email,
            self.phone
        )

Usage:

user = (
    UserBuilder("Madhu")
    .set_age(22)
    .set_email("madhu@example.com")
    .set_phone("9999999999")
    .build()
)

print(user)
Why return self?

This:

builder.set_age(22)
builder.set_email("...")

becomes:

builder.set_age(22).set_email("...").build()

This is called method chaining.

When to use?

Use Builder when:

An object has many optional properties or complicated construction steps.

Common LLD examples
Pizza
Computer
Car
User
HTTP Request
SQL Query
House



"""