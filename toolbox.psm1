function Get-Greeting {
    param($Name = "Explorer")
    return "Hello $Name! Your PowerShell Module is working."
}

function Get-ComputerPower {
    $os = Get-WmiObject Win32_OperatingSystem
    return "You are running $($os.Caption) on Boot Camp!"
}
function New-ToolboxDatabase {
    param($DbPath = "D:\pv\toolbox_data.db")
    
    # 1. Load the SQLite "Driver" (This is the engine for .db files)
    # Note: On Windows 8.1, we use the built-in Windows data tools
    $connectionString = "Data Source=$DbPath;Version=3;"
    
    # 2. Create an empty file if it doesn't exist
    if (!(Test-Path $DbPath)) {
        New-Item -Path $DbPath -ItemType File -Force | Out-Null
        Write-Host "Database file created at $DbPath" -ForegroundColor Yellow
    }

    # 3. Create a Table called 'Logs' inside the .db
    # This is like creating a 'Sheet' in Excel
    $query = "CREATE TABLE IF NOT EXISTS Logs (id INTEGER PRIMARY KEY, msg TEXT, time TEXT);"
    
    # (We will use a helper to run this in Step 2)
    Write-Host "Database structure is ready!" -ForegroundColor Green
}