import requests
import json
import logging
import datetime
import base64
from datetime import datetime

curr_ts_str = str(datetime.now())
Cur_ts = datetime.strptime(curr_ts_str, '%Y-%m-%d %H:%M:%S.%f')

serverURL = 'https://jira.digital.abc.com/'
user = 'l-abc-a-cde'
password = '/password-'
jql = '/rest/api/2/search?jql=project%3D%22ACOEAIOPS%22'
response = requests.get(serverURL + jql,verify=False,auth=(user, password))
print (response)
data = response.json()
data_issue = data.get('issues', 'null')
print (data.get('startAt', 'null'))

for issue in data_issue:
    print (issue['key'])
    data_fields = issue['fields']

#--------Summary---------------------
    data_field_summary = data_fields['summary']
    print ('Summary : ' + data_field_summary)

#------Question 1 ----------------------------
    data_field_question_1 = data_fields['customfield_10803']
    print ('Question 1 : ' + data_field_question_1)

#------description ----------------------------
    data_field_description = data_fields['description']
    print ('description : ' + data_field_description)

#------assignee ----------------------------
    data_field_assignee = data_fields.get('assignee', 'null')
    print (data_field_assignee)
    #try:    
    #    data_assignee_name = data_field_assignee['name']
    #    print (data_assignee_name)
    #except KeyError:
    #    pass

#-----created- ----------------------------
    data_field_created = data_fields['created']
    print ('created : ' + data_field_created)

#----updated-- ----------------------------
    data_field_updated = data_fields['updated']
    print ('updated : ' + data_field_updated)

#    print (datetime.strptime(data_field_updated, "%Y-%m-%d %H:%M:%S.%f"))
