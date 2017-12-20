Preoccupied by a single leaf, you won't see the tree

# items to fix:
1) blog section items:
    - limit the number of blog posts per page, have the newest on front, oldest in back. Make the max 5?
    - rotate backgrounds on each blog index page
    - Figure out how to add images for the blog posts where it replaces the image on the index
    - Fix the styling on *all* blog pages
    - Combining two filters on a template for the post_list.html on the line with class="post_text"
    
2) index:
    - hamburger menu on front page
    - Link the 'HAuto' on the title to the index

3) vehicle:
    - work on setting up your models
    - think about the different ways you could get to the part the person is looking for
    - in the parts model there should be a related parts field (different mfg relation)
    - in the parts model there should be related parts eg: coolant temp sensor - both coolant system and electrical
    
4) stacking HTML files
    - You can add onto all of the HTML files, the blog templates folder shows this. 
    - either each of the apps have a 'main' file OR there is one purely main file.
    - I am leaning towards each app having a 'main', Layouts can vastly differ when more apps get added on
        I don't want to be held to a specific base look.
    
5) document
    - Start making documentation, before the site gets unmanageable.



####Monday 12/11/2017
Worked on index2.html - I didn't like what was going on with index.html so I started from scratch

Left off making 3 images for the top part. 

Items to look into:
- finish up the front page look

For Tuesday: 
Finish front page for now,
Work on the car detail page
work on the blog page



Random Ideas:
- footer quote: random Zen footer quote
- rotating theme header with different livery color schemes.

#### Tuesday 12/12/2017
Updated to index3.html - had to fix bugs with the css, 
the only way to accomplish that was to copy/pasta
also new: layout3.css

Brown paper drawing - that's the template.
starting on vehiclechoice.html now
started on vc1.css now

###### index page has 3 sections - vehicle choice section, 
###### site navigation section, and a blog section
###### I think the site navigation section is a placeholder.

#### Wednesday 12/13/2017
Laid out vehiclechoice.html and styled it
I need a hblog.html page next - but before that, 
I will be going through django girls tutorial for blogs.
I got to a point where you deploy a blog to a website. I might try this on a different day. Right now, I carry on.
Create an HTML for the hardblog. Can copy/pasta from other templates already made. 
ENDO OF DDAYYEY

#### Thursday 12/14/2017
There is a really slick way of creating a base template and inserting other html inside.
Good example is the base.html and post_list.html within the hardblog. 
added a lot of functionality to the blog (draft, edit, publish, delete)
Now to a point where I will be adding security to the site. 

#### Friday 12/15/2017
Added a users to the site
Edited the index3.html and layout3.css in templates outside of the django project - ready to be placed
######Next step: 
- adding commenting to the blog pages
- start moving over the index layout and linking the blog into the main index 
- *Make sure your links aren't broken! you broke the login links to demo*
- Might be a good idea to start up a separate project to try and make the vehicle choices

#### Monday 12/18/2017
Added commenting with admin approve/deny on the comments.
Started a table that I am thinking of using with my models. Need to refine it so I have a clear understanding of all 
    parts of the model.

### Tuesday 12/19/2017