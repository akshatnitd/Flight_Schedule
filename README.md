
A simple utitlity script which will show the flight schedule between any two airports.

Modules required: 

Selenium: It can be installed using 'sudo pip install selenium'/'sudo apt-get install python-selenium'

Bs4: It can be installed using 'sudo pip install bs4'/'sudo apt-get install python-bs4'

It is implemented using the BeautifulSoup module of bs4 and the webdriver module of selenium to scrape data from 
the website (https://www.yatra.com).

How to use:

The script will show the flights between two airports on a specific dates as entered by the user, along with the Departure time, Arrival time, Duration and the price (per adult). 
The script shows results for both one-way journey and round-trip journey. . 

To run the script:

Type 'python flights.py' from your terminal. 

All the flight results will be displayed on the terminal, as well as saved in a file called 'search_result.txt' in the same directory.
