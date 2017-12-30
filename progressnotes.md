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
    - youtube links somewhere with the parts detail
    - tools detail somewhere with the parts detail
    - 
    
4) stacking HTML files
    - You can add onto all of the HTML files, the blog templates folder shows this. 
    - either each of the apps have a 'main' file OR there is one purely main file.
    - I am leaning towards each app having a 'main', Layouts can vastly differ when more apps get added on
        I don't want to be held to a specific base look.
    
5) document
    - Start making documentation, before the site gets unmanageable.
    
6) Future
    - Realizing in the database a few things:
        - There should be a clarification note for the part
            - Cooling has a radiator caps have a pressure rating + link to explain ratings
            - Cooling has a thermostat temperature rating + link to explain ratings
        - Companion image for the part
        - Marking items as Original Equipment or an OE Supplier
        - Marking items as General Aftermarket Replacement
        - Marking items as Racing Equipment
        - Marking Racing Equipment installation items that would require modification
            - ranking system 1-5 for modification 
            - explanation on rankings:
                - 1 = minor modification
                - 5 = major modification
        - Duplication of parts can become very easy when entering in database
            - How can this be prevented in the future?
            - Can there be an easy way to sort parts in the admin panel based on an attribute?
        - A part can be linked to multiple systems, having an option to add additional systems attributes to a part would help.
        - Having an alternate part numbers field (could be outdated part numbers, or cross reference from other manufacturers)  
        - When a part number matches another have a field where all of those are indicated (hardware, hose clamps, bulbs)   
        - An explanation field for manufacturers who do not have part numbers
            - could be boutique parts
            - or if there is no part number given
        - For items like hardware:
            - Bolts & Nuts: thread pitch, specifications, rating, ect ect
            - Hose clamps: Inner diameter or sizing for the specific hose, strength, material
            - O-rings: specify the type of O-ring, inner and outer diameter, application, rating, material    


Over break:

1) make drawings of cars (less than 1-minute per drawing)
2) make drawings of systems (less than 1-minute per drawing)
3) make drawings of cooling systems parts (less than 1-minute per drawing)
4) convert drawings to SVG and host in imgur
5) Finish up the selection tree to choose a specific system then those parts. (AJAX - in the HTML sheet choicebar.)**ACK! WHAT AM I DOING WRGON!**
6) Pagentation for the blog postings
7) Create a app for the media section
8) Work on styling the pages that need it - even if it isn't final styling, make it easier to visualize
9) Fill in the database with at least 200 parts **on Wednesday, up to 70 parts**
    - Get all of the cooling system mapped in
    - Don't worry about all of the choices available - Just get what you can
10)


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
### Wednesday 12/20/2017
I didn't take notes on these days once they were over.
I must have entered in data, finished my models and got all of my different apps linked up to the index

### Thursday 12/21/2017
Morning: 5-min Stand-ups & AJAX Demo
Afternoon: Signed up with Worksource Oregon, sent an email, filled out work history and other details.
Got one item to display from my database to my screen


### Friday 12/22/2017
Got all of the items from the database displayed on the screen
Got some of the selection stuff done with Matthews help
Now I broke it again... @ 3:45