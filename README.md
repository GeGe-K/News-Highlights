# News-Highlights

## Author
### *Gloria Givondo* (09/11/2018)

## Description 
News-Highlights is an application that displays the latest news from various sources and categories e.g. Business from Wall Street Journal.

You can view the live link on: 

## User Stories
These are the behaviours that the application implenents for use by a user.

As a user, I would like: 
* To see various news sources on the homepage of the application.
* To select a news source and see all news articles from the selected news source in the application.
* To see the image, description and the time a news article was created.
* To click on an article and read the full article on the source website.

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display news sources | **On page load** | List of various news sources is displayed on landing page |
| Display articles from a news source | **View articles** | Redirected to a page with a list of articles from the source |
| Display the preview of an article | **On page load** | Each article displays an image, title, description, author and publication date |
| Read an entire article | **Read article** | Redirected to the the entire article |

## Setup / Installation Requirements
* Web browser
* Virtual environment
* Flask
* Python version 3.6


### Cloning the Repo
* In your terminal run:

        $ git clone https://github.com/GeGe-K/News-Highlights.git
        $ cd News-Highlights

## Running the Application 
* Create the virtual environment

        $ sudo apt-get install python3.6 -venv
        $ python3.6 -m venv virtual

* Activate virtual environment

        $ source virtual/bin/activate

* Install Flask and other Modules

        $ pip install -r requirements.txt

* Set up the API Key
        
        To be able to gather article info from the News API you will need an API Key.
        
        * Visit https://newsapi.org/ and register for an API key.
        * In the root directory of the project folder create a file: start.sh
        * Insert the following info into it: 
        
            export NEWS_API_KEY='<Your-Api-Key>'
            python3.6 manage.py server
                
        * Insert the API Key you received from News Api where <Your-Api-Key> is.

* Run the application in your terminal:

        $ chmod +x start.sh
        $ ./start.sh

## Testing the Application 
* To run the tests for the class files and check if they function well:

        $ python3.6 manage.py tests

## Technologies Used
* Virtual environment
* Flask
* Python version 3.6
* Flask-Bootstrap4
* Pip
* HTML
* CSS
* Heroku
* Visual Studio Editor

## Known Bugs
There are no known bugs. Contact gloriagivondo@gmail.com in-case of any bugs.

## License
The content of this site is license under the MIT license
Copyright (c) 2018 **Gloria**

