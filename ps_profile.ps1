function Test-GitRepository {
    $gitDir = Get-Command git -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Source
    return [bool]$gitDir
}

# Open everything python script
function open {
    [CmdletBinding(DefaultParameterSetName='NoArgument')]
    param (
        [Parameter(Mandatory=$false, Position=0, ValueFromRemainingArguments=$true)]
        [string[]] $Argument
    )

    $scriptPath = "C:\Users\BLABLA\open_everything.py"
    & python $scriptPath $Argument
}

# git branches
if (Test-GitRepository) {
    Import-Module posh-git
}

Clear-Host

# Import the Chocolatey Profile that contains the necessary code to enable
# tab-completions to function for `choco`.
# Be aware that if you are missing these lines from your profile, tab completion
# for `choco` will not function.
# See https://ch0.co/tab-completion for details.
$ChocolateyProfile = "$env:ChocolateyInstall\helpers\chocolateyProfile.psm1"
if (Test-Path($ChocolateyProfile)) {
  Import-Module "$ChocolateyProfile"
}
