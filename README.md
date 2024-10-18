Dante Thomas
2150 Fulton Streett
San Francisco, CA 94118

Landscaping Autobiller
October 18, 2024
Overview:

I am creating a program that will calculate customers' final prices based on the services provided during their lawn care service.
This program will take in parameters related to the lawn care service, like Sq. yardage of the lawn, length of the grass, and travel time.
It will also have binary parameters like single or double mow, and difficult or simple terrain. The program will output a bill that
contains a final price, as well as a breakdown of the associated costs. This program will output the bill as a savable file,
that can be indexed and accessed later.

Goals:

Develop the price calculator: Using information from Boris’ previous mowing customers, find monetary values for each parameter,
and how they may increase the price when certain services are done in combination. Each output file should also hold basic job
information, like date, customer name, and other important information.

Develop a user interface and saving system for the bills: Once the program has created a bill for a customer, it will be stored
in a searchable database, with other previous jobs. To extend the application of the program, the previous job could be selected
and automatically set the parameters used the previous time the customer was billed. The user could then make changes to the job
and save it as a new file. The searchable database should be searchable by date of job and by customer.

Specifications
I will be coding in Python. I intend to use built-in functions where I can, and develop the user interface as much as possible.
I may begin by just outputting the receipts as text files, and implementing the file search and reuse at a later time. All of
the functions to calculate the price for the customer should be simple and just involve simple arithmetic operations. I will
use information from the company owner to decide on the monetary value of each service provided on a job. This can be changed
and modified as the program is used. 
Code/Function Breakdown

create_bill()
This will be the wrapper function that calculates the final price for each customer. It will call on the other functions that
take single parameters, to calculate the subprice for each service. It will also adjust the price if the final price needs to
be changed, (extra services, discount, extra difficulty, etc.).

size_price(sq_yards, terrain)
This will be the function that calculates the portion of the price related to the size of the yard. I want to implement a flag
that allows the user to default to a small, medium, or large lawn. If the size, is 1,2, or 3, it will correspond to a small
medium, or large lawn. If the size is 0, it will calculate the size based on the square footage of the yard. If difficult
terrain is present, the terrain parameter will increase the price accordingly.
