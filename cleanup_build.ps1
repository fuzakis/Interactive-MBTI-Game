# Cleanup script for MBTI Game build
# Removes unnecessary files and folders before rebuilding

$gamePath = "c:\FuzakisProject\Renpy\MBTI Game\game"

# Items to remove
$itemsToRemove = @(
    "$gamePath\saves",
    "$gamePath\cache",
    "$gamePath\temp_test.txt",
    "$gamePath\Catatan Test play MBTI Game.txt",
    "$gamePath\questions_logic_generated full.txt",
    "$gamePath\questions_logic.rpy.bak",
    "$gamePath\questions_logic_generated.rpy.bak"
)

Write-Host "Starting cleanup of Ren'Py game directory..." -ForegroundColor Green
Write-Host ""

foreach ($item in $itemsToRemove) {
    if (Test-Path $item) {
        $itemInfo = Get-Item $item
        $size = 0
        
        if ($itemInfo.PSIsContainer) {
            $size = (Get-ChildItem -Path $item -Recurse -Force | Measure-Object -Property Length -Sum).Sum / 1MB
            Remove-Item -Path $item -Recurse -Force
            $sizeRounded = [math]::Round($size, 2)
            Write-Host "[OK] Deleted folder: $(Split-Path $item -Leaf) ($sizeRounded MB)" -ForegroundColor Green
        } else {
            $size = $itemInfo.Length / 1MB
            Remove-Item -Path $item -Force
            $sizeRounded = [math]::Round($size, 2)
            Write-Host "[OK] Deleted file: $(Split-Path $item -Leaf) ($sizeRounded MB)" -ForegroundColor Green
        }
    } else {
        Write-Host "[SKIP] Not found: $(Split-Path $item -Leaf)" -ForegroundColor Gray
    }
}

Write-Host ""
Write-Host "Cleanup complete!" -ForegroundColor Green
Write-Host "Your game directory is now ready for a clean rebuild." -ForegroundColor Green
