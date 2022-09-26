from crawler import current_time, check_data_isexist

site = check_data_isexist(current_time())
print(type(site[0]['count(*)']))