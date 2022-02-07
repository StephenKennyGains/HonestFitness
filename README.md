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

![Flowchart](images/Flowchart_bombsquad.png)

## App Features

This game does not revolve around skill and instead revolves around luck. To create a better user experience, I wanted to ensure I gave adequate options for both explaining the game or proceeding and to have the option of a short or long game. The reason for this is that since the game revolves around luck over skill, by creating a 4 choice and an 8 choice playing board, the probability of success dramatically changes form, each board. 

### Existing Features

- __User Prompt and Welcome__

  - The first stage to the program is basic with a simple message to welcome to the game with the title clearly displayed along with a prompt asking for the users name in an input field which is then relayed back to them in the following line. This is to show the user how the input function will work throughout the remainder of the game and to give them feedback to show them that their input is being received by the program.

![Welcome and User Prompt](images/terminal_initial_prompt.png)

- __Instructions__

  - The second feature is to give the option for instructions for the user or to proceed straight to board selection. Although new users may want some guidance on how to play, I wanted to leave the option available to a recurring player to bypass this stage and go straight to board selection.

![Instructions](images/terminal_instructions.png)

- __Board Selection and Display__

  - The first prompt for the user to initiate the game is to choose the length of their game, choosing between a short path and a long path.
  - A different message will show to the user depending on their choice of board length to give a sense of the level of difficulty ahead.
  - When selected the board will then display in a format that gives the player a more visual representation of the aim of the game showing 4 columns and either 4 or 8 rows depending on the user choice.
  - There is a start and an end displayed and the rows are lettered, and columns numbered which are then relayed back to the user as they progress through the game. 

![Board Selection and Display](images/terminal_select_board.png)

- __Board Run Through__

 - After the board has been selected the user now has inputs to be made to choose whether their next step will be 1, 2, 3 or 4 with the aim to choose a position with no hidden bomb. The initial message will also give them the probability percentage of them guessing correctly through the whole level.
 - If the player selects a position with a randomly allocated bomb, the display will show them BOOM and that they have died and give the option to try again or exit the program.
 - If a player makes it through a stage, they will be given a new probability of making it to the end successfully and tell them they are safe.
 - Upon reaching the end the player is congratulated and given the choice to either play again or to exit the program.

 ![Board Run Through](images/terminal_playthrough.png)

### Features Left to Implement

- There are some features I have thought about including and have been relying on feedback from users as to whether they would improve the experience.
- The first would be to update the board display with each step for the user. To do this I would put the small and large board into a lit and then display the list to the user after each step to show them how many steps are left. This wass left out originally to avoid over-crowding the terminal but feel this could be avoided by clearing the terminal after each guess.
- The second feature to implement would be relaying back to the user their position of death or executing a bomb on their previous turns. Although I did put this in as a feature in my initial development, I removed it after as I felt that on the long board play it could be deterring to a user to see multiple failed attempts given how unlikely it is for a user to succeed through the long board. To get around this I would only display the most recent playthrough and offer one free skip of a row as an incentive to play again

## Testing 

### __Python Testing__

- This is for the written tests section 

### __User Testing__

- This is for user testing


### Validator Testing 

- Python
    - No errors were returned when passing through the official [PEP8](http://pep8online.com/) website. There were originally some syntax errors which were corrected and are no longer present. 


## Unfixed Bugs

- There are no unfixed bugs at present.

## Deployment 

### Heroku Deployment
- Ensure all code is correct and ready for deployment.
- Log into Heroku.
- Click "New" and select "create new app" from the drop-down menu. This is found in the upper right portion of the window.
- Provide a name for your application, this needs to be unique, and select your region.
- Click "Create App".
- Navigate to "Settings" and scroll down to "build packs".
- Click "build packs" and then click both "python" and "node.js"(node.js is needed for the mock terminal.)
- Ensure that the python buildpack is above the node.js buildpack, You can click and drag the packs to re-arrange them.
- Navigate to the "Deploy" section.
- Scroll down to "Deployment Method" and select "GitHub".
- Authorize the connection of Heroku to GitHub.
- Search for your GitHub repository name, and select the correct repository.
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

 - Ardit Sulce- The Python Mega Course. I have not linked the site for this credit as I purchased the course through StackSocial. I believe the original course location was through Udemy which was then sold onto StackSocial as a part of a developer learning bundle which I have found very helpful. 
 - Although the course material from Code Institute does explain all the same methods which I used in my project, I personally struggle to use and grasp concepts if I do not understand exactly how and why a process is working. I found this course by Ardit Sulce very informative and helpful for helping me understand the basic principles for a lot of the code used in basic Python.

### Content 

- No additional content has been added to this site.

### Media

- No media has been used in the site and media in this file have been created myself.