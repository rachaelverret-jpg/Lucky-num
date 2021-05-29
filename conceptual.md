### Conceptual Exercise

Answer the following questions below:

- What is RESTful routing?
Route that provides mapping from HTTP verbs (get, post, put, delete, patch) to controller CRUD actions (create, read, update, delete).

- What is a resource?

Data files that accompany a program's executable code

- When building a JSON API why do you not include routes to render a form that when submitted creates a new user?



- What does idempotent mean? Which HTTP verbs are idempotent?

An identical request can be made once or several times in a row with the same effect while leaving the server in the same state. ... Implemented correctly, the GET , HEAD , PUT , and DELETE methods are idempotent

- What is the difference between PUT and PATCH?

PUT method uses the request URI to supply a modified version of the requested resource which replaces the original version of the resource, whereas the PATCH method supplies a set of instructions to modify the resource.


- What is one way encryption?

Hashing

- What is the purpose of a `salt` when hashing a password?

They create unique passwords even in the instance of two users choosing the same passwords.

- What is the purpose of the Bcrypt module?

Allows us to build a password security platform that scales with computation power and always hashes every password with a salt.

- What is the difference between authorization and authentication?

Authentication confirms that users are who they say they are. Authorization gives those users permission to access a resource.
