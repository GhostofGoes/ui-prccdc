# Author: Christopher Goes

$urls = @("https://ninite.com/.net4.6.2-malwarebytes-notepadplusplus-putty-winscp/", "https://download.microsoft.com/download/8/E/E/8EEFD9FC-46B1-4A8B-9B5D-13B4365F8CA0/EMET%20Setup.msi", "https://download.microsoft.com/download/A/5/0/A50F33AD-842E-43E8-AE99-3AF984A67A52/Security_Compliance_Manager_Setup.exe")
$filenames = @("ninite1.exe", "EMET Setup.msi", "Security_Compliance_Manager_Setup.exe")
$msis = @("EMET Setup.msi")

Import-Module BitsTransfer
For($I=0;$I -lt $urls.count;$I++){
    Start-BitsTransfer -Source $urls[$I] -Destination $filenames[$I]
}

foreach( $msi in $msis ) {
    msiexec.exe /i $msi /passive /norestart
}


# The following comes from this gist: https://gist.github.com/alirobe/7f3b34ad89a159e6daa1
# Which was derived from here: https://github.com/Disassembler0/Win10-Initial-Setup-Script/
# Raise UAC level
Set-ItemProperty -Path "HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\System" -Name "ConsentPromptBehaviorAdmin" -Type DWord -Value 5
Set-ItemProperty -Path "HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\System" -Name "PromptOnSecureDesktop" -Type DWord -Value 1

# Disable sharing mapped drives between users
Remove-ItemProperty -Path "HKLM:\Software\Microsoft\Windows\CurrentVersion\Policies\System" -Name "EnableLinkedConnections"

# Enable Firewall
Set-NetFirewallProfile -Profile * -Enabled True

# Stop and disable Home Groups services
Write-Host "Stopping and disabling Home Groups services..."
Stop-Service "HomeGroupListener"
Set-Service "HomeGroupListener" -StartupType Disabled
Stop-Service "HomeGroupProvider"
Set-Service "HomeGroupProvider" -StartupType Disabled

# Disable Remote Assistance
Write-Host "Disabling Remote Assistance..."
Set-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\Remote Assistance" -Name "fAllowToGetHelp" -Type DWord -Value 0

# Disable Autoplay
Write-Host "Disabling Autoplay..."
Set-ItemProperty -Path "HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\AutoplayHandlers" -Name "DisableAutoplay" -Type DWord -Value 1

#Disable Sticky keys prompt
Write-Host "Disabling Sticky keys prompt..." 
Set-ItemProperty -Path "HKCU:\Control Panel\Accessibility\StickyKeys" -Name "Flags" -Type String -Value "506"

# Show hidden files
Write-Host "Showing hidden files..."
Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" -Name "Hidden" -Type DWord -Value 1

# Install Powershell man pages locally (low priority, uses bandwidth)
Update-Help
