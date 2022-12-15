import subprocess
import os

def main():
    SYNAPSE_WS = os.environ.get("TARGET_WS")
    SPARK_POOL_NAME = os.environ.get("SPARK_POOL_NAME")
    WHEEL_FILE_NAME = os.environ.get("WHEEL_FILE_NAME")

    def run(cmd, message=None):
        result = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
        if result.returncode == 1: # if the command failed
            error_output = 'FAILED'
            # Output the error_output to the GITHUB_OUTPUT environment file
            # For more info, see: https://github.blog/changelog/2022-10-11-github-actions-deprecating-save-state-and-set-output-commands/ 
            subprocess.run(["powershell", "-Command", f'"ErrorOutput={error_output}" >> $env:GITHUB_OUTPUT'])
            raise Exception(result.stderr.decode())
        else:
            print(message)
        return result 

    get_spark_pool_info = f'''$spark_pool_info = Get-AzSynapseSparkPool -WorkspaceName "{SYNAPSE_WS}" -Name "{SPARK_POOL_NAME}";
                            $pool_packages = ($spark_pool_info.WorkspacePackages;
                            $pool_packages.Name'''

    get_workspace_packages = f'Get-AzSynapseWorkspacePackage -WorkspaceName "{SYNAPSE_WS}"'

    remove_from_spark_pool_and_packages = f'''
                                    $package = Get-AzSynapseWorkspacePackage -WorkspaceName "{SYNAPSE_WS}" -Name "{WHEEL_FILE_NAME}";
                                    Update-AzSynapseSparkPool -WorkspaceName "{SYNAPSE_WS}" -Name "{SPARK_POOL_NAME}" -PackageAction Remove -Package $package;
                                    Remove-AzSynapseWorkspacePackage -WorkspaceName "{SYNAPSE_WS}" -Name "{WHEEL_FILE_NAME}" -Force
                                    '''

    remove_from_workspace_packages = f'Remove-AzSynapseWorkspacePackage -WorkspaceName "{SYNAPSE_WS}" -Name "{WHEEL_FILE_NAME}" -Force'

    print(f"Getting info from Spark Pool")
    get_spark_pool_info_result = run(get_spark_pool_info, "Successfully retrieved spark pool info")
    print('herererere', get_spark_pool_info_result.stdout.decode())
    
    if WHEEL_FILE_NAME in get_spark_pool_info_result.stdout.decode():
            print("Wheel file is located on the spark pool. Attempting to remove it from the spark pool and workspace packages")
            remove_result = run(remove_from_spark_pool_and_packages, "Successfully removed wheel file from the spark pool and workspace packages")
    else:
        get_workspace_packages_result = run(get_workspace_packages, "Successfully retrieved workspace package info")
        if WHEEL_FILE_NAME in get_workspace_packages_result.stdout.decode():
            remove_result = run(remove_from_workspace_packages, "Successfully removed wheel from the workspace packages")

    add_wheel_to_pool_and_packages = f'''
                                $package = New-AzSynapseWorkspacePackage -WorkspaceName "{SYNAPSE_WS}" -Package ".\dist\{WHEEL_FILE_NAME}";
                                Update-AzSynapseSparkPool -WorkspaceName "{SYNAPSE_WS}" -Name "{SPARK_POOL_NAME}" -PackageAction Add -Package $package
                                '''
    add_wheel_to_pool_and_packages_result = run(add_wheel_to_pool_and_packages, "Successfully added the new wheel to the workspace packages and spark pool")

if __name__ == "__main__":
    main()


























# if get_spark_pool_info_result.returncode == 1:
#     raise Exception(get_spark_pool_info_result.stderr.decode())

# if 'pytest-7.1.3-py3-none-any.whl' in get_spark_pool_info_result.stdout.decode():
#         remove_result = run(remove_spark_pool)
#         if remove_result.returncode == 1:
#             raise Exception(remove_result.stderr.decode())


# add_wheel_to_pool_and_packages = '''$package = New-AzSynapseWorkspacePackage -WorkspaceName "synapsemultiplereposws" -Package ".\SynapseBuildDeployWheel\pytest-7.1.3-py3-none-any.whl";
#                             Update-AzSynapseSparkPool -WorkspaceName "synapsemultiplereposws" -Name "sparkpool1" -PackageAction Add -Package $package'''
# add_wheel_to_pool_and_packages_result = run(add_wheel_to_pool_and_packages)
# if add_wheel_to_pool_and_packages_result.returncode == 1:
#     raise Exception(add_wheel_to_pool_and_packages_result.stderr.decode())
# else:
#     print(add_wheel_to_pool_and_packages_result.stdout.decode())










# hello_command = "WRITE-HOST 'Hello World!'"
# hello_info = run(hello_command)

# print(hello_info.stdout.decode())

#   $package = Get-AzSynapseWorkspacePackage -WorkspaceName "synapsemultiplereposws" -Name "pytest-7.1.3-py3-none-any.whl"; 
#         Update-AzSynapseSparkPool -WorkspaceName "synapsemultiplereposws" -Name "sparkpool1" -PackageAction Remove -Package $package


# get_spark_pool_info = 'Get-AzSynapseSparkPool -WorkspaceName "synapsemultiplereposws" -Name "sparkpool1"'
# check_spark_result = run(get_spark_pool_info)

# if 'pytest-7.1.3-py3-none-any.whl' in check_spark_result.stdout.decode():
    

# print(check_spark_result.stdout.decode())

# try:
#     check_spark_result = run(get_spark_pool_info)
#     print(check_spark_result.stdout.decode())
#     if 'pytest-7.1.3-py3-none-any.whl' in check_spark_result.stdout.decode():
#         remove_result = run(remove_spark_pool)
#         print(remove_result.stdout.decode())
#     elif 'pytest-7.1.3-py3-none-any.whl'  not in check_spark_result.stdout.decode():
#         check_result = run(check_package)
#         if check_result.returncode == 0:
#             remove_pk = run(remove_from_workspace_packages)
#             print('here')
# except Exception as e:
#     raise e









# check_result = run(check_package)
# if check_result.returncode == 0:
#     check_spark_result = run(get_spark_pool_info)
#     if 'pytest-7.1.3-py3-none-any.whl' in check_spark_result.stdout.decode():
#         remove_result = run(remove_spark_pool)
#         print(remove_result.stdout.decode())
#         new_result = run(remove_spark)
#         print(new_result.stdout.decode())
#         print('error', new_result.stderr.decode())


# add_wheel_packages = '''$package = New-AzSynapseWorkspacePackage -WorkspaceName "synapsemultiplereposws" -Package ".\SynapseBuildDeployWheel\dist\My_Setup_File-1.0-py3-none-any.whl"'''

# add_wheel_package = '''$package = New-AzSynapseWorkspacePackage -WorkspaceName "synapsemultiplereposws" -Package ".\SynapseBuildDeployWheel\pytest-7.1.3-py3-none-any.whl"'''
# # add_wheel = run(add_wheel_package)
# print(add_wheel.stdout.decode())
# print(add_wheel.stderr.decode())


#     remove_workspace_package = 'Remove-AzSynapseWorkspacePackage -WorkspaceName "synapsemultiplereposws" -Name "pytest-7.1.3-py3-none-any.whl" -Force'
#     remove_from_workspace_packages_result = run(remove_workspace_package)
#     print(remove_from_workspace_packages_result.stderr.decode())
# elif check_result.stderr.decode() and 'Status: 404 (Not Found)' not in check_result.stderr.decode():
#     raise Exception(check_result.stderr.decode())





# check_package = 'Get-AzSynapseWorkspacePackage -WorkspaceName "synapsemultiplereposws" -Name "pytest-7.1.3-py3-none-any.whl"'
# check_result = run(check_package)

# if check_result.stdout.decode():
#     remove_workspace_package = 'Remove-AzSynapseWorkspacePackage -WorkspaceName "synapsemultiplereposws" -Name "pytest-7.1.3-py3-none-any.whl" -Force'
#     remove_from_workspace_packages_result = run(remove_workspace_package)
#     print(remove_from_workspace_packages_result.stderr.decode())
# elif check_result.stderr.decode() and 'Status: 404 (Not Found)' not in check_result.stderr.decode():
#     raise Exception(check_result.stderr.decode())



# if check_result.stderr.decode() and 'Status: 404 (Not Found)' in check_result.stderr.decode():
    

# get_spark_pool_info = 'Get-AzSynapseSparkPool -WorkspaceName "synapsemultiplereposws" -Name "sparkpool1"'

# check_spark_result = run(get_spark_pool_info)

# if 'pytest-7.1.3-py3-none-any.whl' in check_spark_result.stdout.decode():
#     print('yesssss')

# print(check_spark_result.stdout.decode())

# check_result = run(check_package)

# if check_result.stderr.decode():
#     print('nooooo')
# else:
#     print('yessss')

# if check_result.stdout.decode():
#     print('standard output')
# else:
#     print('no std output')

# print(check_result.stderr.decode())
# # print(check_result.stdout.decode())

# print(check_result.returncode)



# new_command2 = '''Import-Module Az.Synapse;
#                   $package = New-AzSynapseWorkspacePackage -WorkspaceName "synapsemultiplereposws" -Package ".\SynapseBuildDeployWheel\dist\My_Setup_File-1.0-py3-none-any.whl"'''
                  
                  
                  
      


# $package = New-AzSynapseWorkspacePackage -WorkspaceName "${{ inputs.TARGET_WS }}" -Package ".\dist\${{ inputs.WHEEL_FILE_NAME }}


# new_command2 = '''Import-Module Az.Synapse; 
#                   $package = Get-AzSynapseWorkspacePackage -WorkspaceName "synapsemultiplereposws" -Name "pytest-7.1.3-py3-none-any.whl"; 
#                   Update-AzSynapseSparkPool -WorkspaceName "synapsemultiplereposws" -Name "sparkpool1" -PackageAction Remove -Package $package'''





# new_command = 'Get-AzSynapseWorkspacePackage -WorkspaceName "synapsemultiplereposws" -Name "pytest-7.1.3-py3-none-any.whl"'

# new_command_test = run(new_command2)

# print(new_command_test.stderr.decode())
# print(new_command_test.stdout.decode())

# print(new_command_test.returncode)

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


