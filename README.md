Python TSV to SQL Server Integration Project

This project connects to a directory containing TSV files, processes them to extract data, and inserts it into a SQL Server database. It demonstrates how to use Python to work with TSV files and SQL Server via `pyodbc`.

## Requirements

- Python 3.x
- `pyodbc` for database connection
- `configparser` for reading configuration files
- `shutil` for file management
- `os` for file handling

## Setup


1. Clone the repository:
   ```bash
   git clone https://github.com/shivampuniani/integration_tsv_sql

2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt

3. Configure the database connection:

Update the connection details in the config.ini file with your SQL Server credentials. Here's the format:   
   [database]  
   server = SQLEXPRESS  
   database = Test_Database  
   username = sa  
   password = 12345678  
   [fileData]
   filePath = <path_to_tsv_files>  
   fileContains = <file_name_contains>  
   fileSuccessPath = <path_to_success_directory>  
   fileErrorPath = <path_to_error_directory>


Update the connection strings (if required) in main.py for both SQL Server and the TSV file handling.
SQL Server: Update the SERVER, DATABASE, UID, and PWD placeholders in the config.ini file.
TSV Files: Ensure the path to your TSV files is correct in the config.ini file.


4. Run the script:
   ```bash
   python Python_Tabs_separated_values_file_to_SQL.py


TSV-SQL-Integration-project/  
│  
├── Python_Tabs_separated_values_file_to_SQL.py                  # Your main Python program  
├── requirements.txt                                             # Python dependencies  
├── README.md                                                    # Project documentation  
├── config.ini                                                   # config file to store and configure sql server and file data   
├── .gitignore                                                   # Git ignore rules  
└── log_file.txt                                                 # Log file (will be generated when running the program)  
