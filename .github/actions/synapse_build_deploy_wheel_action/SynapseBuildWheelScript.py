import subprocess

# print('hello')


def run(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed 

# hello_command = "WRITE-HOST 'Hello World!'"
# hello_info = run(hello_command)

# print(hello_info.stdout.decode())


new_command2 = 'Import-Module Az.Synapse; Get-AzSynapseWorkspacePackage -WorkspaceName "synapsemultiplereposws" -Name "pytest-7.1.3-py3-none-any.whl"'



# new_command = 'Get-AzSynapseWorkspacePackage -WorkspaceName "synapsemultiplereposws" -Name "pytest-7.1.3-py3-none-any.whl"'

new_command_test = run(new_command2)

print(new_command_test.stderr.decode())
print(new_command_test.stdout.decode())

print(new_command_test.returncode)

# print(new_command_test.stdout.decode())








# tenant_id = os.environ.get("TENANTID")
# client_id = os.environ.get("CLIENTID")
# client_secret = os.environ.get("CLIENTSECRET")
# notebook_names = os.environ.get("NOTEBOOKNAMES")

# url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/token'
# header = {'Content-Type': 'application/x-www-form-urlencoded'}  
# data = {
#     'client_id': client_id,
#     'client_secret': client_secret,
#     'grant_type': 'client_credentials',
#     'resource': 'https://dev.azuresynapse.net/'
#     }
# access_token_request = requests.get(url=url, headers=header, data=data)
# access_token = access_token_request.json()['access_token']


# url = 'https://synapsewsnjl1.dev.azuresynapse.net/pipelines/PL_SYNAPSE_NOTEBOOK_GITHUBACTIONS/createRun?api-version=2020-12-01'
# headers = {
#                 'Authorization': f'Bearer {access_token}',
#                 'Content-Type': 'application/json'
#         }
# data = {"notebook_names": notebook_names}
# data = json.dumps(data)
# b = requests.post(url = url, headers=headers, data=data)
# run_id = b.json()['runId']
# print("Creating pipeline run. Pipeline run_id:")
# print(run_id)
# print('\n')


# url = 'https://synapsewsnjl1.dev.azuresynapse.net/pipelineruns/0078c32c-0ce9-11ed-a190-a361fc785b84?api-version=2020-12-01'
# a = requests.get(url=url, headers=headers)
# print(a.json()['status'])

# import time 
# def checkValue():
#     status = False

#     timed = 0
#     while status is False:
#         url = f'https://synapsewsnjl1.dev.azuresynapse.net/pipelineruns/{run_id}?api-version=2020-12-01'
#         header = {
#                 'Authorization': f'Bearer {access_token}'
#             }
#         a = requests.get(url=url, headers=header)
#         check_status = a.json()['status']
#         run_start = a.json()['runStart']
#         run_end = a.json()['runEnd']
#         print(check_status)
#         if check_status == 'Succeeded' or check_status == 'Failed':
#             status = True 
#         else:
#             print(timed)
#             time.sleep(10)
#             timed += 10

#         if timed == 100:
#             break
        
#     return [check_status, run_start, run_end]

# status, start, end = checkValue()


# url = f'https://synapsewsnjl1.dev.azuresynapse.net/pipelines/PL_SYNAPSE_NOTEBOOK_GITHUBACTIONS/pipelineruns/55ba6341-39e8-4ed3-bcb2-4556f78e3071/queryActivityruns?api-version=2020-12-01'
# data = {"lastUpdatedAfter":"2020-07-26T13:44:02.1207551Z","lastUpdatedBefore":"2026-07-26T13:49:40.6838494Z"}
# data = json.dumps(data)
# d = requests.post(url=url, headers=headers, data=data)
# exit_value = d.json()['value'][0]['output']['status']['Output']['result']['exitValue']
# print(exit_value)

# print('\n')

# snapshot_url = d.json()['value'][0]['output']['status']['Output']['result']['notebookSnapshotStudioUrl']
# print(snapshot_url)


















# url = f'https://synapsewsnjl1.dev.azuresynapse.net/pipelines/PL_SYNAPSE_NOTEBOOK_GITHUBACTIONS/pipelineruns/{run_id}/queryActivityruns?api-version=2020-12-01'
# data = {"lastUpdatedAfter":"2020-07-26T13:44:02.1207551Z","lastUpdatedBefore":"2026-07-26T13:49:40.6838494Z"}
# data = json.dumps(data)
# d = requests.post(url=url, headers=header, data=data)
# d.json()


