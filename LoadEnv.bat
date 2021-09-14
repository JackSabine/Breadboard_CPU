set anaconda_dir=C:\Users\jack\anaconda3
set vscode_dir=C:\Users\jack\AppData\Local\Programs\Microsoft VS Code
set project_dir=C:\Users\jack\OneDrive\Documents\GitHub\Breadboard_CPU\Programming
set envname=budgetlake

call "%anaconda_dir%\Scripts\activate.bat" "%anaconda_dir%"
call conda activate %envname%
start "" "%vscode_dir%\Code.exe" -r "%project_dir%"
exit