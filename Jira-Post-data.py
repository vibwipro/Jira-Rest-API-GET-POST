from jira import JIRA
import re

options = {
 'server': 'https://jira.digital.abc.com/',
 'verify': False }
jira = JIRA(options, basic_auth=('l-user', '/password-'))

issue = jira.issue('Repository-1')

issue.update(fields={'summary' : 'Updated-1' \
 #,'assignee': {'name':'johnd'} \
 })
