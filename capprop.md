# HAuto
#### HardAuto

## Milestone 1

###### 1) Create a new Django project
1) Have 3 html files
    - Main page
    - Selected Vehicle page with all of the areas to be explored
    - My selected view area (I am thinking of the Engine bay)
2) Very basic layout of each html
    - mix of html, css, js
    
###### 2) Creating and establishing a database schema
- **_this is likely going to be the part that will take the longest._**
1) Create a database of vehicles starting with Year.
    1) Since I will only be focusing on one vehicle (1984-1987 Corolla GTS), I will use this as a setup for the future.
    2) Date range
        - Vehicle Manufacturer 
            - Model
                - Trim
2) Navigating the vehicle systems (example) - this area could easily provide 200 items
    1) Engine 
        - Cooling
            - Radiator
                - Radiator
                    - (display product information from part foreign key)
                - Radiator Cap
                - Radiator Drain Petcock
                - Radiator Mounts
                - Radiator Hardware
            - Radiator Fan
            - Radiator Hoses
            - Heater Core
            - Heater Core Hoses
            - Other Cooling Lines & Hoses
            - Water Pump
            - Thermostat
            - Overflow Tank
3) Create a database of parts manufacturers
    1) Under each manufacturer is a list of parts 
    2) Part Manufacturer (make 2 or 3 different ones)
        - Part number 
            - Product Details
            - Image placeholder
            - Availability (If discontinued?)
            - Foreign Key
4) Create a database of tools
    1) There are tools that are specially made, a manufacturer will be required 
        - maybe use 'generic' for easily found tools
        
###### 3) Verifying the correct info appears on the page
1) Editing the page to display the part correctly.
    1) Verify correct part number
    2) Correct photo appears
    3) Correct tools appear
    
## Milestone 2

###### 1) Develop the database further
1) Add onto the database
    1) Create a second car that items can be applied to
        - 1984-89 Toyota MR2 (shares the engine)
    2) Create a second tree off of Engine, the following are examples
        - Ignition
        - Lubrication
        - Belt Driven Accessories
        - Internals
        - Gaskets
        - Mounts & Brackets
        - Intake 
        - Exhaust
        - Covers
    3) Create a few more options for Part Manufacturers
###### 2) Create SVG images for the parts in the database
1) Hand drawn parts to SVG
    1) Converting quick & dirty hand drawn images into SVGs
    2) Apply these images to the parts in the database
    
###### 3) Editing the admin panel to add info quicker
1) If items are not in my excel sheets, having an easy way to add-in

###### 4) Developer blog
1) Providing updates to the site to any of the readers with a comment section where feedback can be left


## Milestone 3

###### 1) Make the pages *pretty*
1) Spend some time on the CSS/JS of the individual pages and give it visual appeal
    - When your head is killing you... this is a good thing to work on

###### 2) Create a sidebar that has hyperlinks to Youtube videos 
1) Use the Youtube API to search the model of car & the part selected for videos 
    - Not sure if they should be hyperlinked back to Youtube or displayed on the page.
    - Could appear in a pop-up?
    
###### 3) Create SVG views for different views in addition to a product tree. 
1) Hand drawn views of the System to look at
    - links to a closer view of parts on a specific area of the vehicle
    - Mouse over highlight & (maybe) AJAX to display data OR just to a pop-up displaying data


## Milestone 4

###### 1) Complete the database for the primary car
1) Fill the database with all of the 'systems' and the parts associated
    - this will help adding, deleting, or setting to discontinued parts
    
###### 2) Put a guide of regular maintenance intervals
1) Display a guide of regular intervals
    - In each interval have video links or instructions on completing the tasks
    - Put together a chart of fluids used for the car
    
###### 3) Put together a page of most commonly used tools for the vehicle
1) Provide a list of commonly used tools 
2) Maybe even a list of commonly used tools in a specific area or 'system'

###### 4) AWS Deploy?
1) Insane?
2) TOS?
3) Disclaimer?
4) Lawyer up?


## Wishlist
###### 1) LEGO style instructions
1) LEGO style instructions regarding how to replace a part - Not entirely dependent on Youtube
    - This will require all sorts of creation.
    
###### 2) Work in another vehicle
1) Pick another vehicle and start the process again
    - develop the process further on the second time around
    - there will likely be new things or better ways of doing something
    - look for ways to automate 

