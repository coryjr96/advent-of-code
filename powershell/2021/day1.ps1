#DAY 1 2021

$script:data = (gc 'C:\Users\coryj\OneDrive\Desktop\Programming\advent of code\powershell\2021\day1input.txt')

Function Do-PartOne {
    $count = 0
    for ($index = 1; $index -le $data.Count; $index++) {
        if ([int]$data[$index] -gt [int]$data[$index - 1]) {
            $count++
        }
    }
    Write-Host "Part One Answer:" $count
}

Function Do-PartTwo {
    $count = 0
    for ($index = 0; $index -le $data.Count; $index++) {
        $group = [int]$data[$index] + [int]$data[$index + 1] + [int]$data[$index + 2]
        $group2 = [int]$data[$index + 1] + [int]$data[$index + 2] + [int]$data[$index + 3]
        if ($group -lt $group2) {
            $count++
        }
    }
    Write-Host "Part Two Answer:" $count
}

Do-PartOne 
Do-PartTwo
