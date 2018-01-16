 "add a new post" form and the blog listings are on the same page.

 class Blog():
    id, title, and body

route = /blog (home page w/ all posts displayed)

 templates 1 one each for the / blog(main blog listings) 
 template 2 and / newpost(post new blog entry) views.

    Your templates should extend a base.html template 

base.html page NAVICATION LINKS:
        <nav>
        <a href="/base.html/">Main Blog Page</a> |
        <a href="/css/">Add a Blog Entry</a>
        </nav>

User input validation - if empty

Each blog post - Detail - Page ...clickable from the post

URL Route displays the ID in the URL

New blog post redirects to detail page of item vs main pg.
    Create a new DB record for the blog entry that was submitted and before redirecting,
    grab the id for the record.


CASE2 ___



