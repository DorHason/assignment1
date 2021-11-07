# assignment1
In this assignment I built a system that detects and reports modifications that were made to a database.
This is done by running a docker-server that holds a database, and exports the following three API endpoints:
1. GET /initialize 
Removes whatever is currently in the DB, and stores 5000 duplicates of the provided data entry  example. 
2. POST /modify data: {“entries”: << int >>} 
Randomly selects a number of entries (according to what was sent in data.entries,) and for each  entry modifies the value of the boolean field ‘is_modified’ from false, to true. 
3. GET /validate 
Goes over the database and finds the entries that were modified. Returns a human-readable  report that specifies how many entries were modified, and which ones (their ID’s). 

To run the server install the requirements and run "python app.py", or build the container using "docker-compose up --build" from the terminal.
Then, navigate to http://localhost:5000/initialize to initialize the application.
