# Environment variables

# synapsemultiplereposws = $Env:TARGET_WS
# sparkpoolwheel = $Envsparkpoolwheel
# # 'My_Setup_File-1.0-py3-none-any.whl' = $Env:WHEEL_FILE_NAME

# 'My_Setup_File-1.0-py3-none-any.whl' = 'My_Setup_File-1.0-py3-none-any.whl'


$get_workspace_packages = (Get-AzSynapseWorkspacePackage -WorkspaceName "synapsemultiplereposws").Name

if ('My_Setup_File-1.0-py3-none-any.whl' -in $get_workspace_packages) {
    Remove-AzSynapseWorkspacePackage -WorkspaceName "synapsemultiplereposws" -Name "My_Setup_File-1.0-py3-none-any.whl" -Force;
    $package = New-AzSynapseWorkspacePackage -WorkspaceName "synapsemultiplereposws" -Package ".\dist\My_Setup_File-1.0-py3-none-any.whl";
    Update-AzSynapseSparkPool -WorkspaceName "synapsemultiplereposws" -Name "sparkpool3" -PackageAction Add -Package $package
}



# $spark_pool_info = Get-AzSynapseSparkPool -WorkspaceName "synapsemultiplereposws" -Name "sparkpoolwheel"

# $spark_pool_info = (Get-AzSynapseSparkPool -WorkspaceName "synapsemultiplereposws" -Name "sparkpoolwheel")
# $spark_pool_info

# if ('My_Setup_File-1.0-py3-none-any.whl' -in $spark_pool_info) {
#     'here2'
#     $package = Get-AzSynapseWorkspacePackage -WorkspaceName "synapsemultiplereposws" -Name "openpyxl-3.0.10-py2.py3-none-any.whl";
#     'starting to remove package'
#     Update-AzSynapseSparkPool -WorkspaceName "synapsemultiplereposws" -Name "sparkpoolwheel" -PackageAction Remove -Package $package;
#     'removed from spark pool'
#     Remove-AzSynapseWorkspacePackage -WorkspaceName "synapsemultiplereposws" -Name "sparkpoolwheel" -Force;

#     $package = New-AzSynapseWorkspacePackage -WorkspaceName "synapsemultiplereposws" -Package ".\dist\'My_Setup_File-1.0-py3-none-any.whl'";
#     Update-AzSynapseSparkPool -WorkspaceName "synapsemultiplereposws" -Name "sparkpoolwheel" -PackageAction Add -Package $package

# } else {
#     Write-Host 'HERE'
#     $get_workspace_packages = (Get-AzSynapseWorkspacePackage -WorkspaceName "synapsemultiplereposws").Name
#     if ('My_Setup_File-1.0-py3-none-any.whl' -in $get_workspace_packages) {
#         'hello'}}
#         Remove-AzSynapseWorkspacePackage -WorkspaceName "synapsemultiplereposws" -Name "'My_Setup_File-1.0-py3-none-any.whl'" -Force;
        
#         $package = New-AzSynapseWorkspacePackage -WorkspaceName "synapsemultiplereposws" -Package ".\dist\'My_Setup_File-1.0-py3-none-any.whl'";
#         $package
#         Update-AzSynapseSparkPool -WorkspaceName "synapsemultiplereposws" -Name "sparkpoolwheel" -PackageAction Add -Package $package
#     }    
#     else {
#         $package = New-AzSynapseWorkspacePackage -WorkspaceName "synapsemultiplereposws" -Package ".\dist\'My_Setup_File-1.0-py3-none-any.whl'";
#         Update-AzSynapseSparkPool -WorkspaceName "synapsemultiplereposws" -Name "sparkpoolwheel" -PackageAction Add -Package $package
#     }
# }




























# try{
#     $spark_pool_info = Get-AzSynapseSparkPool -WorkspaceName "synapsemultiplereposws" -Name "sparkpoolwheel"

#     if ('My_Setup_File-1.0-py3-none-any.whl' -in $spark_pool_info.WorkspacePackages.Name) {
#         $package = Get-AzSynapseWorkspacePackage -WorkspaceName "synapsemultiplereposws" -Name "'My_Setup_File-1.0-py3-none-any.whl'";
#         Update-AzSynapseSparkPool -WorkspaceName "synapsemultiplereposws" -Name "sparkpoolwheel" -PackageAction Remove -Package $package;
#         Remove-AzSynapseWorkspacePackage -WorkspaceName "synapsemultiplereposws" -Name "sparkpoolwheel" -Force;

#         $package = New-AzSynapseWorkspacePackage -WorkspaceName "synapsemultiplereposws" -Package ".\dist\'My_Setup_File-1.0-py3-none-any.whl'";
#         Update-AzSynapseSparkPool -WorkspaceName "synapsemultiplereposws" -Name "sparkpoolwheel" -PackageAction Add -Package $package

#     } else {
#         Write-Host 'HERE'
#         $get_workspace_packages = Get-AzSynapseWorkspacePackage -WorkspaceName "synapsemultiplereposws"
#         $get_workspace_packages
#         if ('My_Setup_File-1.0-py3-none-any.whl' -in $get_workspace_packages.Name) {
#             Remove-AzSynapseWorkspacePackage -WorkspaceName "synapsemultiplereposws" -Name "'My_Setup_File-1.0-py3-none-any.whl'" -Force;
            
#             $package = New-AzSynapseWorkspacePackage -WorkspaceName "synapsemultiplereposws" -Package ".\dist\'My_Setup_File-1.0-py3-none-any.whl'";
#             $package
#             Update-AzSynapseSparkPool -WorkspaceName "synapsemultiplereposws" -Name "sparkpoolwheel" -PackageAction Add -Package $package
#         }    
#         else {
#             $package = New-AzSynapseWorkspacePackage -WorkspaceName "synapsemultiplereposws" -Package ".\dist\'My_Setup_File-1.0-py3-none-any.whl'";
#             Update-AzSynapseSparkPool -WorkspaceName "synapsemultiplereposws" -Name "sparkpoolwheel" -PackageAction Add -Package $package
#         }
#     }
# }
# catch {

#     throw $Error
# }