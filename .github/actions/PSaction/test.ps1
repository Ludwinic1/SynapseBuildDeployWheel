# Environment variables

$synapse_ws = $Env:TARGET_WS
$spark_pool_name = $Env:SPARK_POOL_NAME
$wheel_file_name = $Env:WHEEL_FILE_NAME

# Logic

# Get-AzSynapseSparkPool -WorkspaceName "$synapse_w" -Name "$spark_pool_name"


# try {
#     Get-AzSynapseSparkPool -WorkspaceName "$synapse_w" -Name "$spark_pool_name"
# }
# catch {
#     throw $Error
# }

# try { NonsenseString }
# catch {
#   Write-Host "An error occurred:"
#   Write-Host $_
# }

try {
    $spark_pool_info = Get-AzSynapseSparkPool -WorkspaceName "$synapse_ws" -Name "$spark_pool_name"

    if ($wheel_file_name -in $spark_pool_info.WorkspacePackages.Name) {
        $package = Get-AzSynapseWorkspacePackage -WorkspaceName "$synapse_ws" -Name "$wheel_file_name";
        Update-AzSynapseSparkPool -WorkspaceName "$synapse_ws" -Name "$spark_pool_name" -PackageAction Remove -Package $package;
        Remove-AzSynapseWorkspacePackage -WorkspaceName "$synapse_ws" -Name "$spark_pool_name" -Force;

        $package = New-AzSynapseWorkspacePackage -WorkspaceName "$synapse_ws" -Package ".\dist\$wheel_file_name";
        Update-AzSynapseSparkPool -WorkspaceName "$synapse_ws" -Name "$spark_pool_name" -PackageAction Add -Package $package

    } else {
        $get_workspace_packages = Get-AzSynapseWorkspacePackage -WorkspaceName "$synapse_ws"
        if ($wheel_file_name -in $get_workspace_packages.Name) {
            Remove-AzSynapseWorkspacePackage -WorkspaceName "$synapse_ws" -Name "$wheel_file_name" -Force;
            
            $package = New-AzSynapseWorkspacePackage -WorkspaceName "$synapse_ws" -Package ".\dist\$wheel_file_name";
            Update-AzSynapseSparkPool -WorkspaceName "$synapse_ws" -Name "$spark_pool_name" -PackageAction Add -Package $package
        }    
        else {
            $package = New-AzSynapseWorkspacePackage -WorkspaceName "$synapse_ws" -Package ".\dist\$wheel_file_name";
            Update-AzSynapseSparkPool -WorkspaceName "$synapse_ws" -Name "$spark_pool_name" -PackageAction Add -Package $package
        }
    }
}
catch {
    throw $Error
}






# import subprocess
# import os

# def main():
#     synapse_ws = os.environ.get("TARGET_WS")
#     spark_pool_name = os.environ.get("SPARK_POOL_NAME")
#     wheel_file_name = os.environ.get("WHEEL_FILE_NAME")

#     def run(cmd, message=None):
#         result = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
#         if result.returncode == 1: # if the command failed
#             my_output = 'FAILED'
#             subprocess.run(["powershell", "-Command", f'"myOutput={my_output}" >> $env:GITHUB_OUTPUT'])
#             # print(f"::set-output name=myOutput::{my_output}")
#             # print(f"myOutput={my_output}" >> $GITHUB_OUTPUT)
#             raise Exception(result.stderr.decode())
#         else:
#             print(message)
#         return result 

#     # my_output = 'FAILED2'
#     # test1 = run(f'"myOutput={my_output}" >> $env:GITHUB_OUTPUT')

#     get_spark_pool_info2 = f'''$spark_pool_info = Get-AzSynapseSparkPool -WorkspaceName "{synapse_ws}" -Name "{spark_pool_name}";
#                             $pool_packages = $spark_pool_info.WorkspacePackages;
#                             $pool_packages.Name'''


#     # get_spark_pool_info = f'Get-AzSynapseSparkPool -WorkspaceName "{synapse_ws}" -Name "{spark_pool_name}"'

#     get_workspace_packages = f'Get-AzSynapseWorkspacePackage -WorkspaceName "{synapse_ws}"'

#     remove_from_spark_pool_and_packages = f'''$package = Get-AzSynapseWorkspacePackage -WorkspaceName "{synapse_ws}" -Name "{wheel_file_name}";
#                                     Update-AzSynapseSparkPool -WorkspaceName "{synapse_ws}" -Name "{spark_pool_name}" -PackageAction Remove -Package $package;
#                                     Remove-AzSynapseWorkspacePackage -WorkspaceName "{synapse_ws}" -Name "{wheel_file_name}" -Force'''

#     remove_from_workspace_packages = f'Remove-AzSynapseWorkspacePackage -WorkspaceName "{synapse_ws}" -Name "{wheel_file_name}" -Force'

#     print(f"Getting info from Spark Pool")
#     get_spark_pool_info_result = run(get_spark_pool_info2, "Successfully retrieved spark pool info")
    
#     if wheel_file_name in get_spark_pool_info_result.stdout.decode():
#             print("Wheel file is located on the spark pool. Attempting to remove it from the spark pool and workspace packages")
#             remove_result = run(remove_from_spark_pool_and_packages, "Successfully removed wheel file from the spark pool and workspace packages")
#     else:
#         get_workspace_packages_result = run(get_workspace_packages, "Successfully retrieved workspace package info")
#         if wheel_file_name in get_workspace_packages_result.stdout.decode():
#             remove_result = run(remove_from_workspace_packages, "Successfully removed wheel from the workspace packages")

#     add_wheel_to_pool_and_packages = f'''$package = New-AzSynapseWorkspacePackage -WorkspaceName "{synapse_ws}" -Package ".\dist\{wheel_file_name}";
#                                 Update-AzSynapseSparkPool -WorkspaceName "{synapse_ws}" -Name "{spark_pool_name}" -PackageAction Add -Package $package'''
#     add_wheel_to_pool_and_packages_result = run(add_wheel_to_pool_and_packages, "Successfully added the new wheel to the workspace packages and spark pool")

# if __name__ == "__main__":
#     main()