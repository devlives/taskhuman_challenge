## TaskHuman Coding Challenge

#### Prerequisites
Please follow the following steps to set up the environment. This must be run on [*nix like](https://en.wikipedia.org/wiki/Unix-like) systems. If you are using windows please use a virtual box to install an ubuntu server and follow the following steps:

a. Create a fresh virtualenv w/ Python 3.6 and also install docker and docker compose.
-   Our docker versions are docker 17.12.0 and docker-compose 1.18.0.

b. Run `make init` to set up the environment and install all the prerequisites.

c. Run `make test` to make sure all of the smoke tests are passing without any issues

d. Run `make run` to bring up the airflow server
	i. Once this command is executed, the airflow server should be visible at http://localhost:8080
	ii. You should be able to see a DAG name example_dag
	iii. Along with airflow, postgres database would be installed to store the airflow metadata at port 5432. Please use `docker ps` command to see the containers that are up and the ports they bound into. Connection to postgres is essential to accomplish the task below. If you are using SQLAlchemy the connection can be accessed using the following string: `postgresql+psycopg2://airflow:airflow@localhost:5432/airflow`


#### Task
For this challenge, you would be building the following data pipeline using Apache Airflow.

Step 1: You would create a DAG to fetch the users information from a [fake json site](https://jsonplaceholder.typicode.com/) 
         The DAG should be scheduled every 45 minutes

Step 2: The user data is in a nested JSON format. [Here](https://jsonplaceholder.typicode.com/users) is how it looks like.  Convert this data into a table format (for example python list of list object or a pandas dataframe).

Step 3: Create a branch operator to accomplish the following conditions:

case A - Target Table Missing: Check if the target table to load the above user information exist in postgres destination. If the target table doesn't exist (for example when you load the data for the first time), create a table called `users` in the database `airflow` and load the data. 

case B - Target Table Exists: If the target table exists, continue to load the data.
 
 For this step, you can use the psycopg2 python driver which is already provided to you. The connection string is visible on airflow.cfg file or is also mentioned above.
 
**Bonus**

 Additional cookie points for:
	*  Implementing `airflow sensors` to check for http response while fetching the user data in step 1. You can be creative by providing a slackoperator or email operator in case of failed http response.
	* Not using pandas to convert into dataframe in step 2.
	* Please make sure to run `make lint` to confirm if the code is pep8 compliant
	* Use airflow postgres hooks for Step 3 above.

**What To Submit**

  
To build a pipeline, you would need to create a DAG. A sample DAG is given in the location dags/example_dag.py it will be necessary to create a DAG. We have provided an example DAG for reference,  `dags/dag_example.py`. 
When you create a DAG, please place it into this directory and it would automatically be mounted onto the docker container when you run the container using `make run`

#### Some Materials To Read

a. Get started developing workflows with Apache Airflow [link](http://michal.karzynski.pl/blog/2017/03/19/developing-workflows-with-apache-airflow/)

b. Airflow Docs are at [link](https://airflow.apache.org/)

c. Another nice medium post [link](https://medium.com/airbnb-engineering/airflow-a-workflow-management-platform-46318b977fd8)

