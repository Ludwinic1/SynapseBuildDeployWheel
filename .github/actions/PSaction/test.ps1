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
        Write-Host 'HERE'
        $get_workspace_packages = Get-AzSynapseWorkspacePackage -WorkspaceName "$synapse_ws"
        $get_workspace_packages
        if ($wheel_file_name -in $get_workspace_packages.Name) {
            Remove-AzSynapseWorkspacePackage -WorkspaceName "$synapse_ws" -Name "$wheel_file_name" -Force;
            
            # $package = New-AzSynapseWorkspacePackage -WorkspaceName "$synapse_ws" -Package ".\dist\$wheel_file_name";
            # Update-AzSynapseSparkPool -WorkspaceName "$synapse_ws" -Name "$spark_pool_name" -PackageAction Add -Package $package
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