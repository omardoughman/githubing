# 1. Import the module (The ID Card and the Engine)
Import-Module "D:\pv\Toolbox.psd1" -Force

# 2. Use the new commands you just built!
Write-Host "--- Running Module Commands ---" -ForegroundColor Cyan

Get-Greeting -Name "Omar"
Get-ComputerPower

Write-Host "--- Done! ---" -ForegroundColor Green
# Import your module
Import-Module "D:\pv\Toolbox.psd1" -Force

# Create the .db file
New-ToolboxDatabase -DbPath "D:\pv\my_project.db"

# Check if it exists
if (Test-Path "D:\pv\my_project.db") {
    Write-Host "SUCCESS: Your .db file is sitting on your D: drive!" -ForegroundColor Cyan
}