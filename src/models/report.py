from .db_conn import db, ma
from flask import jsonify
import json


def select_1():
    sql = "select pres_name , death_age from president Order by death_age"
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None


def select_2():
    sql = " select party ,pres_name from president "
    sql += " Order by party , pres_name"
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None


def select_3():
    sql = " select death_age, pres_name from president "
    sql += " where death_age > 0 "
    sql += " order by death_age asc, pres_name desc ;"
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None


def select_4():
    sql = " select pres_name , spouse_name , pr_age ,sp_age from pres_marriage "
    sql += " order by  pr_age"
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None


def select_5():
    sql = " select * from president where pres_name like 'Reagan%' "
    sql += " order by pres_name"
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None


def select_6():
    sql = " select * from president where pres_name NOT LIKE 'Reagan%'"
    sql += " order by pres_name"
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None       


def select_7():
    sql = " select * from president where death_age < 70"
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None       


def select_8():
    sql = " select * from president where pres_name between 'Eisenhower' AND 'Nixon' "
    sql += " order by pres_name asc"
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None 


def select_9():
    sql = " select * from president where yrs_serv IN (2,4,6,8) "
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None 


def select_10():
    sql = " select * from president where party = 'Republican'"
    sql += " order by pres_name asc"
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None 


def select_11():
    sql = " select pres_name , spouse_name , nr_children from PRES_MARRIAGE where nr_children > 5"
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None 


def select_12():
    sql = " select pres_name , spouse_name , pr_age, sp_age from PRES_MARRIAGE where pr_age > 20 and sp_age <= 20"
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None 


def select_13():
    sql = " select pres_name , spouse_name , pr_age, sp_age from PRES_MARRIAGE where pr_age = sp_age "
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None 


def select_14():
    sql = "  select avg(pr_age) from PRES_MARRIAGE "
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None 


def select_15():
    sql = "  select avg(nr_children) from PRES_MARRIAGE where mar_year > 1900  "
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None 


def select_16():
    sql = "  select avg(votes) from election where Election_year >= 1901 and Winner_loser_indic = 'W' ;  "
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None 


def select_17():
    sql = " select count(distinct(election_year)) from election  "
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None 


def select_18_1():
    sql = " select count(DISTINCT Candidate) from election where Winner_loser_indic = 'L'  "
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None 


def select_18_2():
    sql = " select distinct(candidate)from election  "
    sql += " where Winner_loser_indic = 'L' and candidate NOT IN (select distinct(candidate) from election where Winner_loser_indic = 'W')  " 
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None 


def select_19():
    sql = " select count(year_entered) from state where admin_entered is null ;  "
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None 


def select_20():
    sql = "  select avg(death_age) from president where party = 'Republican' and Birth_yr > 1850  "
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None 


def select_21():
    sql = "  sselect pres_name,count(pres_name) from pres_marriage  "
    sql += " group by pres_name  " 
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None 


def select_22():
    sql = "  select count(pres_name) from PRESIDENT "
    sql += " where birth_yr + death_age > 1970  " 
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None 


def select_23():
    sql = "  select count(pres_name) from ADMINISTRATION "
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None 


def select_24():
    sql = "   select count (distinct(pres_name)) from ADMINISTRATION "
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None 


def select_25():
    sql = "   select min(sp_age) from PRES_MARRIAGE "
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None 


def select_26():
    sql = "   select pres_name, spouse_name , nr_children from PRES_MARRIAGE where sp_age < 20 "
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None 


def select_27():
    sql = " select avg(pr_age - sp_age) from PRES_MARRIAGE "
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None 


def select_28():
    sql = " select count(pres_name) from PRES_MARRIAGE where pr_age - 2 > sp_age "
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None 


def select_29():
    sql = " select avg(pr_age / sp_age) from PRES_MARRIAGE "
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None 


def select_30():
    sql = " select * from pres_marriage where pr_age < sp_age and sp_age - 2 < pr_age "
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None 


def select_31():
    sql = " SELECT MAX(CAST(YRS_SERV AS FLOAT)/CAST(DEATH_AGE AS FLOAT))*100, MIN(CAST(YRS_SERV AS FLOAT)/CAST(DEATH_AGE AS FLOAT))*100 "
    sql += " FROM PRESIDENT WHERE DEATH_AGE>0;  " 
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None 


def select_32():
    sql = "  select election_year , candidate from election "
    sql += " where election_year > 1900  " 
    sql += " order by election_year desc  " 
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None 



def select_33():
    sql = "  select election_year , candidate from election "
    sql += " where election_year > 1976  " 
    sql += " oorder by election_year desc  " 
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None 


def select_34():
    sql = "  select pres_name,min(pr_age),max(pr_age) from PRES_MARRIAGE "
    sql += " group by pres_name  " 
    sql += " having count(pres_name)>1 and max(pr_age)> (min(pr_age)*2) " 
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None 


def select_35():
    sql = " select election_year , count(candidate) from election "
    sql += " where election_year > 1870  " 
    sql += " group by election_year " 
    sql += " having count(candidate) > 2 " 
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None 


def select_36():
    sql = " select avg(pr_age) ,avg(sp_age) from PRES_MARRIAGE "
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None 


def select_37():
    sql = " select avg(nr_children) from PRES_MARRIAGE "
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None 


def select_38():
    sql = " select pres_name , sum(nr_children), min(pr_age) from PRES_MARRIAGE "
    sql += " where pres_name in (select pres_name from PRES_MARRIAGE where pr_age <= 20) " 
    sql += " group by pres_name " 
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None         


def select_39():
    sql = " select pres_name , sum(nr_children),min (pr_age) from PRES_MARRIAGE "
    sql += " where pr_age > 35 and pres_name not in (select pres_name from PRES_MARRIAGE where pr_age <= 35) " 
    sql += " group by pres_name" 
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None         


def select_40():
    sql = " select pres_name , pr_age , mar_year from PRES_MARRIAGE "
    sql += " where nr_children = 0 " 
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None         


def select_41():
    sql = " select pres_name,sum(nr_children) from pres_marriage "
    sql += " where nr_children >= 2 " 
    sql += " group by pres_name " 
    sql += " having count(nr_children) > 1 " 
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None         


def select_42():
    sql = " select pres_name, spouse_name from PRES_MARRIAGE "
    sql += " where nr_children > 5 "  
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None                 


def select_43():
    sql = " select distinct party from president " 
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None   


def select_44():
    sql = " select party ,count(party) from PRESIDENT "
    sql += " where birth_yr > 1850  "  
    sql += " group by party  "  
    sql += " having count (party) > 7  " 
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None                 


def select_45():
    sql = " SELECT state_born FROM PRESIDENT "
    sql += " where birth_yr > 1880 "  
    sql += " group by state_born "  
    sql += " having count (state_born) > 1  " 
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None                 


def select_46():
    sql = "  SELECT party , max(death_age) FROM PRESIDENT "
    sql += " group by party ,death_age is not null "  
    sql += " and death_age < 0"  
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None    


def select_47():
    sql = "  select death_age,count(pres_name) from president "
    sql += " where death_age is not null "  
    sql += " group by death_age "  
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None    


def select_48():
    sql = "  SELECT party , max(death_age) ,min(death_age) FROM PRESIDENT "
    sql += " group by party ,death_age is not null and death_age < 0 "    
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None    


def select_49():
    sql = " SELECT state_born, count(pres_name), avg(death_age), max(yrs_serv), min(yrs_serv) FROM PRESIDENT "
    sql += " group by state_born "    
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None   


def select_50():
    sql = " select vice_pres_name , pres_name from admin_pr_vp "   
    sql += " where vice_pres_name in ( select  vice_pres_name from admin_pr_vp group by vice_pres_name having count(vice_pres_name) > 1 and max(pres_name) != min(pres_name) )	"  
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None  


def select_51():
    sql = " select admin_nr,count(pres_name) from admin_pr_vp "
    sql += " group by admin_nr "    
    sql += " having count(vice_pres_name) > 1 "    
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None    


def select_52():
    sql = " select admin_nr ,count(pres_name) from administration "
    sql += " group by admin_nr "    
    sql += " having count(pres_name) > 1 "    
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None  


def select_53():
    sql = " select pres_name,min(year_inaugurated) from administration "
    sql += " group by pres_name "        
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None  


def select_54():
    sql = " select hobby , count(hobby) from pres_hobby "
    sql += " group by hobby "        
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None  


def select_55():
    sql = " select * from president where yrs_serv > 6 "        
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None  


def select_56():
    sql = " select year_entered , count(year_entered) from state "
    sql += " group by year_entered "        
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None  


def select_57():
    sql = " select count(year_entered) from state where year_entered = 1776 "       
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None  


def select_58():
    sql = " SELECT AVG(c.hob)  "     
    sql += " FROM ( SELECT COUNT(HOBBY) as hob FROM PRES_HOBBY GROUP BY HOBBY) as c "   
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None 


def select_59():
    sql = " select pres_name,sum(nr_children) from pres_marriage  "
    sql += " where nr_children > 2 "   
    sql += " group by pres_name "       
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None  


def select_60():
    sql = " select * from pres_marriage  "
    sql += " where nr_children > 2 "        
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None  


def select_61():
    sql = " select pres_name, yrs_serv , sum(votes) from president , election  "
    sql += " where  pres_name = candidate and yrs_serv > 4 " 
    sql += " group by pres_name , yrs_serv, candidate "      
    sql += "having max(winner_loser_indic) != min(winner_loser_indic) "       
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None  


def select_62():
    sql = " select pres_name , yrs_serv , round(avg(votes),3) from president , election  "
    sql += " where president.pres_name = election.candidate and winner_loser_indic = 'W' " 
    sql += " group by pres_name , yrs_serv "           
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None  


def select_63():
    sql = " select pres_name , year_inaugurated , count(winner_loser_indic) from administration , election  "
    sql += " where administration.pres_name = election.candidate and winner_loser_indic = 'L' " 
    sql += "group by pres_name , year_inaugurated "           
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None  


def select_64():
    sql = " select pres_name , count(hobby) from pres_hobby  "
    sql += " group by pres_name " 
    sql += "having count(hobby) = (select max(c)  as b from (select count(*) as c from pres_hobby group by pres_name) as count) "           
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None  


def select_65():
    sql = " select pres_name,yrs_serv from president  "
    sql += " where yrs_serv = (select max(yrs_serv) from president)"           
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None  


def select_66():
    sql = " select state_name, year_entered from state  "
    sql += " where year_entered in (select year_entered from state group by year_entered having count(year_entered)>2)"           
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None  


def select_67():
    sql = " select * from state  "
    sql += " where admin_entered in (select admin_entered from state group by admin_entered having count(admin_entered) >= 2) "           
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None  


def select_68():
    sql = " select party ,count(pres_name) from president  "
    sql += " where birth_yr > 1850 "       
    sql += " group by party "  
    sql += " count(birth_yr) = (select max(b) from (select count(birth_yr) as b from president where birth_yr > 1850 group by party ) as count) "      
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None  


def select_69():
    sql = " select pres_name , yrs_serv from president  "
    sql += " group by pres_name , yrs_serv "       
    sql += " having yrs_serv = ( select max(yrs_serv) from president where yrs_serv in ( select max(yrs_serv) from president group by pres_name )) "       
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None  


def select_70():
    sql = " select party , count(pres_name) from president  "
    sql += " where birth_yr > 1850 "       
    sql += " group by party "  
    sql += " order by  party "       
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None  


def select_71():
    sql = " select pres_name from PRES_MARRIAGE  "
    sql += " where nr_children > 1 "       
    sql += " group by pres_name "  
    sql += " having count(spouse_name) > 1 "       
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None  


def select_72():
    sql = " select     year_inaugurated ,president.pres_name, birth_yr, yrs_serv, death_age,party,state_born from president, administration  "
    sql += " where president.pres_name = administration.pres_name and administration.year_inaugurated = (select min(year_inaugurated) from administration where year_inaugurated > (select  min(mar_year) from pres_marriage where pres_name like 'Reagan%' group by pres_name ) ) "             
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None  


def select_73():
    sql = " select PS.pres_name , (AD.year_inaugurated - PS.birth_yr) from administration AD , president PS "
    sql += " where AD.pres_name = PS.pres_name "       
    sql += " group by PS.pres_name , (AD.year_inaugurated - PS.birth_yr)  "  
    sql += " having AD.year_inaugurated - PS.birth_yr = (select MIN(UP.YE) from( select AD.pres_name as ADP, (AD.year_inaugurated - PS.birth_yr) from administration AD , president PS where AD.pres_name = PS.pres_name group by AD.pres_name , (AD.year_inaugurated - PS.birth_yr) )  as UP  ) "       
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None 



def select_74():
    sql = " select pres_name , count(pres_name),sum(nr_children) from PRES_MARRIAGE  "
    sql += " where pr_age < 40 "       
    sql += " group by pres_name "  
    sql += " having count(pres_name) > 1 and sum(nr_children) > 2"       
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None


def select_75():
    sql = " select pres_name , sum(nr_children) from PRES_MARRIAGE  "
    sql += " where pr_age > 50 and sp_age < 30 "       
    sql += " group by pres_name "       
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None


def select_76():
    sql = " select WW.election_year , WW.Winner_votes , WL.Looser_votes  "
    sql += " from (select election_year,sum(votes) as Winner_votes from election where winner_loser_indic = 'W' group by election_year) AS WW, (select election_year,sum(votes) as Looser_votes from election where winner_loser_indic = 'L' group by election_year) AS WL "       
    sql += " where WW.election_year = WL.election_year "  
    sql += " order by election_year "       
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None


def select_77():
    sql = " select avg(MS.MM) "
    sql += " from    (select min(pr_age) as MM from PRES_MARRIAGE group by pres_name) as MS "            
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None


def select_78():
    sql = " select avg(MS.MM) "
    sql += " from     (select max(pr_age) as MM from PRES_MARRIAGE group by pres_name having count(pres_name) > 1) as MS "            
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None


def select_79():
    sql = " select PR.pres_name , max(PR.birth_yr) , max(PM.pr_age) as age2 from president PR, PRES_MARRIAGE PM "
    sql += " where PR.pres_name = PM.pres_name "  
    sql += " group by  PR.pres_name , PM.pres_name "  
    sql += " having count (spouse_name) > 1 "  
    sql += "  order by PR.pres_name "            
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None



def select_80():
    sql = " select PR.pres_name , PR.birth_yr , EL.election_year "
    sql += " from president PR , election EL , (select EL.candidate , min(EL.election_year) as year from election EL where winner_loser_indic = 'W' group by EL.candidate having COUNT(EL.election_year) > 1 ) as EMIN "  
    sql += "where PR.pres_name = EL.candidate and EL.candidate = EMIN.candidate and EL.election_year > EMIN.year and winner_loser_indic = 'W' "              
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None


def select_81():
    sql = " select Win.elect1 ,birth_yr "
    sql += " from (    select el1.candidate as elect1, count(candidate) as c1	from election el1 where winner_loser_indic = 'W' group by el1.candidate  ) as Win  , (select el2.candidate as elect2 , count(candidate) as c2 from election el2  where winner_loser_indic = 'L' group by el2.candidate ) as Loser , president PR "  
    sql += " where Win.elect1 = Loser.elect2 and Win.elect1 = PR.pres_name and Win.c1 = Loser.c2 "             
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None


def select_82():
    sql = " select PS.pres_name , PS.c1 "
    sql += " from (select am.pres_name  , count(am.pres_name) as c1  from administration am   group by am.pres_name) as PS	,	(select pm.pres_name , count(PJ.spouse_name) as c2 from president pm left outer join pres_marriage PJ on pm.pres_name = PJ.pres_name group by pm.pres_name ) as SP where PS.pres_name = SP.pres_name and PS.c1 > SP.c2 "             
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None

def select_83():
    sql = " select AM.NAM1 , PMR.nr_cnt "
    sql += " from     (select ADM.pres_name as NAM1 , count(ADM.admin_nr) as an from administration ADM group by ADM.pres_name ) as AM, from pres_marriage PM group by PM.pres_name ) as PMR "  
    sql += " where AM.NAM1 = PMR.NAM2 and AM.an = PMR.nr_cnt "              
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None


def select_84():
    sql = " select candidate , votes , cast(votes as float) / cast (SUM as float)* 100 as VOT "
    sql += " from election ,( select sum(votes) as s1 from election where election_year = (	 select election_year from election where votes = ( select max(votes) as m2 from election where winner_loser_indic = 'W') ) )as SUM  , (select max(votes) as m1 from election where winner_loser_indic = 'W') as max "  
    sql += " where votes = max.m1  "           
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None


def select_85():
    sql = " select pr.pres_name from president pr "
    sql += " where pr.pres_name in (select APP.vice_pres_name from admin_pr_vp APP group by APP.vice_pres_name)  "           
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None


def select_86():
    sql = " select pr.pres_name from president pr "
    sql += " where pr.pres_name not in (select APP.vice_pres_name from admin_pr_vp APP group by APP.vice_pres_name)  "           
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None


def select_87():
    sql = " select pr.pres_name from  president pr "
    sql += " where pr.pres_name not in (select EL.candidate from election EL)  "           
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None

def select_88():
    sql = " select PRM.pres_name , PRM.pr_age from pres_marriage PRM"
    sql += " where PRM.pr_age < (select avg(PRE.min) as av1 from (select PM.pres_name,min(PM.pr_age) as m1 from pres_marriage PM group by PM.pres_name) as PRE  "           
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None

def select_89():
    sql = " select PRM.pres_name , PRM.age"
    sql += " from   (select PM.pres_name , nr_children , min(PM.pr_age) as age from pres_marriage PM  group by PM.pres_name,nr_children ) as PRM, (select HB.pres_name,count(HB.hobby) as c1 from pres_hobby HB  group by HB.pres_name ) as HOB  "  
    sql += " where PRM.pres_name = HOB.pres_name and PRM.nr_children < HOB.c1"
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None       


def select_90():
    sql = " select pr.pres_name from  president pr "
    sql += " where pr.pres_name not in (select pr.pres_name from pres_marriage pr)  "           
    result = db.engine.execute(sql)
    result_data = [dict(r) for r in result]

    if(len(result_data) > 0):
        return result_data
    else:
        return None