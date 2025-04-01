import os
import pyodbc
import shutil
import configparser

def get_db_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    db_config = {
        'server': config.get('database', 'server'),
        'database': config.get('database', 'database'),
        'username': config.get('database', 'username'),
        'password': config.get('database', 'password'),
        'filePath': config.get('fileData', 'filePath'),
        'fileContains': config.get('fileData', 'fileContains'),
        'fileSuccessPath' : config.get('fileData', 'fileSuccessPath'),
        'fileErrorPath' : config.get('fileData', 'fileErrorPath'),
    }
    return db_config


def db_connection(server, database, uid, pwd):
    
    conn = pyodbc.connect(
        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'UID={uid};'
        f'PWD={pwd}'
    )
    return conn

def main():
    db_config = get_db_config()
    conn = db_connection(db_config["server"], db_config["database"], db_config["username"], db_config["password"])
    cursor = conn.cursor()


    your_path = db_config["filePath"]
    success_Path = db_config["fileSuccessPath"]
    error_Path = db_config["fileErrorPath"]

        
    Test_No  = ""
    data = {  
    'AVG_A' : 0, 'MIN_A' : 0, 'MAX_A' : 0, 'CVP_A' : 0,
    'AVG_C' : 0, 'MIN_C' : 0, 'MAX_C' : 0, 'CVP_C' : 0,
    'AVG_D' : 0, 'MIN_D' : 0, 'MAX_D' : 0, 'CVP_D' : 0, 
    'AVG_E' : 0, 'MIN_E' : 0, 'MAX_E' : 0, 'CVP_E' : 0, 
    'AVG_F' : 0, 'MIN_F' : 0, 'MAX_F' : 0, 'CVP_F' : 0, 
    'AVG_K' : 0, 'MIN_K' : 0, 'MAX_K' : 0, 'CVP_K' : 0, 
    'AVG_L' : 0, 'MIN_L' : 0, 'MAX_L' : 0, 'CVP_L' : 0, 
    'AVG_R' : 0, 'MIN_R' : 0, 'MAX_R' : 0, 'CVP_R' : 0}

    files = os.listdir(your_path)
    for file in files:
        if db_config["fileContains"] in file:
            with open(your_path+'\\'+file) as f:
                contents = f.read()
                for item in contents.split("\n"):
                        if "Identifier" in item:
                            Test_No = item.split("\t")[1].replace("Identifier :","")
                        elif "Average" in item:
                            averageData = item.split("\t")
                            data['AVG_A'] = averageData[2]
                            data['AVG_C'] = averageData[4]
                            data['AVG_D'] = averageData[5]
                            data['AVG_E'] = averageData[6]
                            data['AVG_F'] = averageData[7]
                            data['AVG_K'] = averageData[12]
                            data['AVG_L'] = averageData[13]
                            data['AVG_R'] = averageData[19]
                        elif "Minimum" in item:
                            minimumData = item.split("\t")
                            data['MIN_A'] = minimumData[2]
                            data['MIN_C'] = minimumData[4]
                            data['MIN_D'] = minimumData[5]
                            data['MIN_E'] = minimumData[6]
                            data['MIN_F'] = minimumData[7]
                            data['MIN_K'] = minimumData[12]
                            data['MIN_L'] = minimumData[13]
                            data['MIN_R'] = minimumData[19] 
                        elif "Maximum" in item:
                            maximumData = item.split("\t")
                            data['MAX_A'] = maximumData[2]
                            data['MAX_C'] = maximumData[4]
                            data['MAX_D'] = maximumData[5]
                            data['MAX_E'] = maximumData[6]
                            data['MAX_F'] = maximumData[7]
                            data['MAX_K'] = maximumData[12]
                            data['MAX_L'] = maximumData[13]
                            data['MAX_R'] = maximumData[19]
                        elif "CV %" in item:
                            cvData = item.split("\t")
                            data['CVP_A'] = cvData[2]
                            data['CVP_C'] = cvData[4]
                            data['CVP_D'] = cvData[5]
                            data['CVP_E'] = cvData[6]
                            data['CVP_F'] = cvData[7]
                            data['CVP_K'] = cvData[12]
                            data['CVP_L'] = cvData[13]
                            data['CVP_R'] = cvData[19]
                                         
        if Test_No != "": 
            cursor = conn.cursor()
            cursor.execute('''
                                    INSERT INTO [Test_Database].[dbo].[Test_TSV]([Test_No],[AVG_F],[CVP_F],[AVG_L],[AVG_K],[AVG_E],[AVG_A],[AVG_R],[AVG_D],[AVG_C],
                                    [MAX_F] ,[MIN_F] ,[MIN_A] ,[MAX_A] ,[CVP_A] ,[MIN_C] ,[MAX_C] ,[CVP_C] ,[MIN_R]  ,[MAX_R]  ,
                                    [CVP_R] ,[MIN_D] ,[MAX_D] ,[CVP_D] ,[MIN_E] ,[MAX_E] ,[CVP_E] ,[MIN_K] ,[MAX_K] ,[CVP_K] ,[MIN_L] ,[MAX_L] ,[CVP_L], [status])
                                    VALUES
                                    (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,'5')
                                    ''',str(Test_No) ,str(data['AVG_F']) ,str(data['CVP_F']) ,str(data['AVG_L']) ,str(data['AVG_K'])
                                       ,str(data['AVG_E']) ,str(data['AVG_A']) ,str(data['AVG_R']) ,str(data['AVG_D']) ,str(data['AVG_C'])
                                     ,str(data['MAX_F']) ,str(data['MIN_F']) ,str(data['MIN_A']) ,str(data['MAX_A'])
                                    ,str(data['CVP_A']) ,str(data['MIN_C']) ,str(data['MAX_C']) ,str(data['CVP_C']) ,str(data['MIN_R'])
                                    ,str(data['MAX_R'])  ,str(data['CVP_R']) ,str(data['MIN_D']) ,str(data['MAX_D']) ,str(data['CVP_D'])
                                   ,str(data['MIN_E']) ,str(data['MAX_E']) ,str(data['CVP_E']) ,str(data['MIN_K']) ,str(data['MAX_K'])
                                    ,str(data['CVP_K']) ,str(data['MIN_L']) ,str(data['MAX_L']) ,str(data['CVP_L']))
            conn.commit()  
                               
            shutil.move(os.path.join(your_path, file),os.path.join(success_Path, file))                      
        if Test_No == "":
             shutil.move(os.path.join(your_path, file),os.path.join(error_Path, file))


if __name__ == "__main__":
    main()
