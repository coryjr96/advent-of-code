#DAY 2 2021

$script:data = Import-Csv 'C:\Users\coryj\OneDrive\Desktop\Programming\advent of code\powershell\2021\day2input.txt' -Delimiter " " -Header $('direction', 'value')

Function Do-PartOne {
    $horizontal = 0
    $depth = 0
    ForEach($line in $data) {
        if($line.direction -eq "forward") {
            $horizontal += $line.value
        } elseif($line.direction -eq "down") {
            $depth += $line.value
        } elseif($line.direction -eq "up") {
            $depth -= $line.value
        }
    }
    Write-Host "Part One Answer:" ($horizontal * $depth)
}

Function Do-PartTwo {
    $horizontal = 0
    $depth = 0
    $aim = 0
    ForEach($line in $data) {
        if($line.direction -eq "forward") {
            $horizontal += $line.value
            $depth += [int]$line.value * $aim
        } elseif($line.direction -eq "down") {
            $aim += $line.value
        } elseif($line.direction -eq "up") {
            $aim -= $line.value
        }
    }
    Write-Host "Part Two Answer:" ($horizontal * $depth)
}

Do-PartOne
Do-PartTwo