#DAY 3 2021

$script:data = (gc 'C:\Users\coryj\OneDrive\Desktop\Programming\advent of code\powershell\2021\day3input.txt')

Function Do-PartOne {
    $gamma = ""
    $epsilon = ""
    For($iter = 0; $iter -le 11; $iter++) {
        $counter = @{Ones = 0; Zeros = 0}
        ForEach($line in $data) {
            if($line[$iter] -eq "0") {
                $counter.Zeros += 1
            } else {
                $counter.Ones += 1
            }
        }
        if($counter.Ones -gt $counter.Zeros) {
            $gamma += "1"
        } else {
            $gamma += "0"
        }
    }
    $stringiter = $gamma.ToCharArray()
    ForEach($letter in $stringiter) {
        if($letter -eq "0") {
            $epsilon += "1"
        } else {
            $epsilon += "0"
        }
    }
    $gammadec = [Convert]::ToInt32($gamma,2)
    $epsilondec = [Convert]::ToInt32($epsilon,2)
    Write-Host "Part One Answer:" ($gammadec * $epsilondec)
}

Function Do-PartTwo {
    Function Get-Oxygen {
        $newdata = $data
        For($iter = 0; $iter -le 11; $iter++) {
            $counter = @{Ones = 0; Zeros = 0}
            $oxygen = @()
            $common = "0"
            ForEach($line in $newdata) {
                if($line[$iter] -eq "1") {
                    $counter.Ones += 1
                } else {
                    $counter.Zeros += 1
                }
            }
            if($counter.Ones -ge $counter.Zeros) {
                $common = "1"
            }
            ForEach($line in $newdata) {
                if($line[$iter] -eq $common) {
                    $oxygen += $line
                }
            }
            $newdata = $oxygen
            if($oxygen.Count -eq 1) {
                $script:finaloxygen = [Convert]::ToInt32($oxygen[0],2)
                return
            }
        }
    }
    Function Get-Scrubber {
        $newdata = $data
        For($iter = 0; $iter -le 11; $iter++) {
            $counter = @{Ones = 0; Zeros = 0}
            $scrubber = @()
            $uncommon = "1"
            ForEach($line in $newdata) {
                if($line[$iter] -eq "1") {
                    $counter.Ones += 1
                } else {
                    $counter.Zeros += 1
                }
            }
            if($counter.Zeros -le $counter.ones) {
                $uncommon = "0"
            }
            ForEach($line in $newdata) {
                if($line[$iter] -eq $uncommon) {
                    $scrubber += $line
                }
            }
            $newdata = $scrubber
            if($scrubber.Count -eq 1) {
                $script:finalscrubber = [Convert]::ToInt32($scrubber[0],2)
                return
            }
        }
    }
    Get-Oxygen
    Get-Scrubber
    Write-Host "Part Two Answer:" ($finalscrubber * $finaloxygen)
}

Do-PartOne
Do-PartTwo