# [Honest Fitness](https://honestfitness.herokuapp.com/) 

Honest Fitness is a blog page offering free advice and guidance on their exercise and fitness goals.

The blog is divided in to 3 categories of posts, General, Training and Exercise.

General focuses on common topics, Training focuses on structure to workouts and hobbits and Exercise focuses on common exercise mistakes and best practise.

The review section is for users to leave reviews on people or places such as gyms they have been to or trainers they have used to help guide others towards valuable resources in the fitness community.

Users of the site can view all posts, reviews and comments left by the authors and users but can only post to the site if they are a registered user.

All reviews and comments left by users are subject to approval to avoid any hateful, negative or derogatory content being published to the site.

![Responsive Mock-up](images/Mockup.png)



## Table of contents

- [UX and UI](#ux-and-ui)
    - [Site goals](#site-goals)
    - [User goals](#user-goals)
    - [Admin goals](#admin-goals)
    - [Flowchart](#flowchart)
- [Features](#features)
    - [Existing Features](#existing-features)
    - [Features Left To Implement](#features-left-to-implement)
- [Testing](#testing)
    - [Python](#python)
    - [User Testing](#user-testing)
- [Code Validation](#validator-testing)
- [Unfixed Bugs](#unfixed-bugs)
- [Deployment](#deployment)
- [Credits](#credits)
- [Content](#content)
- [Media](#media)

## UX

## Site goals

The site aim for Honest Fitness is for a simplistic fitness blog for users to learn more information about their training habits and common mistakes. To simplify the experience the site has been categorized so users can easily jump to sections that are of more interest to them than other. Users can engage in the site through commenting on posts, liking posts and leaving reviews on people or places related to fitness. The site should be easily navigated by users and content should be easy to read and functionality like commenting, liking and reviewing should be simplictic and error free to the users.

## User goals:
- All user stories were created and implemented using an agile approach to the project and can be found in the project section of the Honest Fitness Repository hosted on Github using a standard Kanban board [Honest Fitness Project](https://github.com/StephenKennyGains/HonestFitness/projects)
- In additon to the User stories linked above, below are the additional site goals for users
- The user should feel that the site is easy to navigate and that content is easy to filter through to find relevant content.
- The user login, registration and logout functionality should be seamless, match the style of the site and have no errors in the process.
- Users should feel that they can easily engage with the site and other users of the site without any unnecessary blocks or hassle.

## Admin goals:
- All admin stories were created and implemented using an agile approach to the project and can be found in the project section of the Honest Fitness Repository hosted on Github using a standard Kanban board [Honest Fitness Project](https://github.com/StephenKennyGains/HonestFitness/projects)
- As an admin, the site should be seamless to control and moderate with CRUD functionality to be easily implemented.
- The admin panel via Django should make the creation of the site easy for the admin and allow for constant updating and moderation of the site.
- The admin should be able to easily control the content uploaded by users to ensure that the site is kept to a standard and is free from unwanted and unnecessary content uploaded from users. 

## Flowchart

The flowchart for this program was made on LucidChart. The flowchart takes you through both the development strategy for the program and the user experience and where their options are to continue or exit the program and to be given additional instructions on the game along with difficulty choices.

![Flowchart](media/readme_images/Honest_Fitness_Flowchart.png)

## App Features

The application has been kept simple to allow for easy navigation for users through both the content and site structure. While having the ability to interact with the site, some level of moderation is still required and so there are some limitations to the users interactivity to the site as outlined below. 

### Existing Features

- __Blog Post Views__

  - The main aspect of the site is the blog post content and to keep the content streamlined to the user it has been categorized into three different categories. The categories are General, Training and Exercise. This allows users to self filter to sections of the site which are more appealing to the them as not all users will be interested in each category of post.

- __Categorized Post Pages__

  - As the home page is limited to the 3 most recent posts for each category to limit the content of the home page and avoid having a visual overload to the user, there is a button placed below each category for users to then view a seperate page containing all posts from a particular category ordered from latest to oldest so recurring users can easily view the most recent and up to date posts.

- __Full View Posts__

  - To allow users to view the blog post in a full, unobstructed manner, each blog post will redirect users to a new template which will show only the post and the site header and footer. This view is also where users habve the option to like posts and comment on them to interact with the posts. Comments related to each post will be displayed in this view. The comments will be ordered from oldest to newest to that users can view the comments in order as a conversation. The option to comment will be in a sepearate form to complete and will be dependant on admin approval to publish.

- __Reviews Page__

  - The Reviews page will feature both Admin created reviews and user created views which will display as cards and give the review title, location, review and a rating between 1-5 stars. The option for users to review themselves will be dependant on their logged in status. For ease of access, I have pinned the form in to a button which is at the top of the page so that in the event of numerous reviews being left, the user will not have to scroll too far to see the ability to review something themselves. To keep the page clean, the form will expand and push other content down instead of resting over existing content or lenghtening the page excesively.  

 ![Board Run Through](images/terminal_playthrough.png)

### Features Left to Implement

- I would like to include a feature for users to ask for feedback anonymously by way of a form which requests the users current problem, training summary, nutritional summary and other relevant details which would then be used to post as a new blog post under another category of real life stories.
- I would like to add media storage for uploading short videos on common exercise mistakes and how to correct them. This would be accompanied by a short write up and would be related to the exercise section of the blog.
- A feature for users to be able to like others comments would be a nice additonal feature and for top liked comments to be highlighted and pinned to a seperate section above each post comments section as this can be a way of spreading more useful information to users seeking the same advice.

## Testing 

### __Python Testing__

- This is for the written tests section 

### __User Testing__

- This is for user testing


### Validator Testing

- HTML Testing
  = HTML HERE

- CSS Testing
  - CSS HERE

- Python
    - No errors were returned when passing through the official [PEP8](http://pep8online.com/) website. There were originally some syntax errors which were corrected and are no longer present. 


## Unfixed Bugs

- There are no unfixed bugs at present.

## Deployment 

### Heroku Deployment
- Ensure all dependancies such as third party libraries are listed in your requirements.txt file using the command pip3 freeze --local > requirements.txt
- Ensure all code is correct and ready for deployment.
- Log into Heroku.
- Click "New" and select "create new app" from the drop-down menu. This is found in the upper right portion of the window.
- Provide a name for your application, this needs to be unique, and select your region.
- Click "Create App".
- Navigate to "Resources" tab.
- Click on Resources and Search for Heroku Postgres and select it on the list to add to the project.
- Navigate to the "Deploy" section.
- Scroll down to "Deployment Method" and select "GitHub".
- Authorize the connection of Heroku to GitHub.
- Search for your GitHub repository name, and select the correct repository.
- Navigate to the settings tab
- Select revel config vars and add the following,
  - Your Cloudinary URL, your Database URL form the Heroku Postgres and your SECCRET_KEY.
- For Deployment there are two options, Automatic Deployments or Manual.
- Automatic Deployment: This will prompt Heroku to re-build your app each time you push your code to GitHub.
- Manual Deployment: This will only prompt Heroku to build your app when you manually tell it to do so.
- Ensure the correct branch is selected "master/Main", and select the deployment method that you desire. In this case, I will be using Automatic Deployment.

### Clone Repository
- On GitHub go to the main page of the Repository.
- Above the list of files click the code button with the drop-down arrow.
- To clone the repository using HTTPS, under "Clone with HTTPS", click on the clipboard.
- Open the Git Bash terminal.
- Change the current working directory to the location where you want the cloned directory.
- Type git clone, and then paste the URL you copied earlier from step 3.
- Press Enter to create your local clone.

## Credits 

 - I would like to give huge credit to the Code Institute support team. I ran into a few issues that I could not resolve after a few hours of trouble shooting and was given excellent guidance and help to be able to continue with my project.
 - Thanks to my mentor Adegbenga Adeye for all his help as I changed my project plan a few times due to unforseen circumstances through the months leading up to the project.

### Content 

- No additional content has been added to the project apart from the media listed below.
- Project Resources are as follows:
  - Adobe XD for Wireframes
  - LucidChart for Flowcharts and ERD
  - Multi Device Website Mockup Generator: Used to generate mockup image.
  - Font Awesome for Icons
  - Bootstrap for HTML format
  - Google Fonts for project fonts
  - Github and Gitpod for version control and deployment
  - Django for the project Framework
  - Summernote, used to format blog posts
  - Cloudinary for media storage
  - Crispy forms for the commenting form

### Media

- Media for the blog posts was taken from Unsplash.com(https://unsplash.com/)
- Currently used images are from the following artists
  - 