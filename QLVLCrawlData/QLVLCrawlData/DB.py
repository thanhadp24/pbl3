import mysql.connector
from venv import logger

def save_company_into_DB(data):
    try:
        connection = mysql.connector.connect(user='root', password='1234', host='localhost', database='pbl3')
        cursor = connection.cursor()
        query = "INSERT INTO company (id, name, address, industry_id) VALUES (0, %s, %s, '3')"
        for i in data:
            getCompanyId = "SELECT id FROM company WHERE NAME = '" + str(i[0]) + "'"
            companyId = getIdFromDB(getCompanyId)
            if companyId == None:
                cursor.execute(query, i)
        connection.commit()
        connection.close()
    except Exception as e:
        logger.error(f"Error occured while saving data to DB: {e}")

def save_rank_into_DB(data):
    try:
        connection = mysql.connector.connect(user='root', password='1234', host='localhost', database='pbl3')
        cursor = connection.cursor()
        query = "INSERT INTO `rank` (id, name) VALUES (0, %s)"
        for i in data:
            getRankId = "SELECT id FROM `rank` WHERE NAME = '" + str(i) + "'"
            rankId = getIdFromDB(getRankId)
            if rankId == "":
                e = (i,)
                cursor.execute(query, e)
                
        connection.commit()
        connection.close()
    except Exception as e:
        logger.error(f"Error occured while saving data to DB: {e}")

def save_recruitment_into_DB(data):
    try:
        connection = mysql.connector.connect(user='root', password='1234', host='localhost', database='pbl3')
        cursor = connection.cursor()
        query = "INSERT INTO recruitment_detail (id, company_id, rank_id, job_name, salary, posted_date_at, deadline_to_apply, experience, number_of_recruitment, age_range, gender, qualification, probation_period, location, description, benefit, requirement, source_picture) VALUES (0, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        for i in data:
            getCompanyId = "SELECT id FROM company WHERE NAME = '" + str(i[0]) + "'"
            getRankId = "SELECT id FROM `rank` WHERE NAME = '" + str(i[2]) + "'"
            
            companyId = getIdFromDB(getCompanyId)
            rankId = getIdFromDB(getRankId)
            tmp = []
            tmp.append(companyId)
            tmp.append(rankId)
            tmp.extend(i[3:18])
            
            cursor.execute(query, tmp)
        connection.commit()
        connection.close()
    except Exception as e:
        logger.error(f"Error occured while saving data to DB: {e}")

def getIdFromDB(data):
    try:
        connection = mysql.connector.connect(user='root', password='1234', host='localhost', database='pbl3')
        cursor = connection.cursor()
        cursor.execute(data)
        res = cursor.fetchone()
        res = ''.join(str(x)for x in res)
        return res
    except Exception as e:
        logger.error(f"Error occured while saving data to DB: {e}")