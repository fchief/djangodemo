Readme
---------------------------------------------------------

Python: 3.6
Django Version: 1.10

This is a basic django CRUD web app for demo purpose.
Main URL: your machine host with designated port number. Usually localhost:8000

Home Page
---------------------------------------------------------
Purpose: List all posts created by the user.
Function: The R (retrieve) of CRUD
URL: localhost:8000

Create Post Page
---------------------------------------------------------
Purpose: Create new post. 
Function: The C (create) of CRUD
URL: localhost:8000/post

Update/Retrieve Post Page
---------------------------------------------------------
Purpose: Update or retrieve an existing post. 
Function: The R and U (update) of CRUD
URL: localhost:8000/post/id, id is substituted by a post id. Everytime a new post is created, id is incremented automatically through a model primary key and is attached to the new post as part of the identiy.

Delete Post Page
---------------------------------------------------------
Purpose: Delete existing post. 
Function: The D(delete) of CRUD
URL: localhost:8000/post/id/delete