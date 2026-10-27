param(
    [Parameter(Position=0)]
    [string]$Target = (Get-Location).Path
)
$ErrorActionPreference = "Stop"
$Installer = Join-Path $PSScriptRoot "install_instructions.py"
if (-not (Test-Path $Installer)) { throw "install_instructions.py not found beside this script." }
python $Installer $Target
if ($LASTEXITCODE -ne 0) { throw "Guide installation failed. Check that Python 3 is installed." }
