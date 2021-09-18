set anaconda_dir=C:\Users\%USERNAME%\anaconda3
set vscode_dir_NULL=C:\Users\%USERNAME%\AppData\Local\Programs\Microsoft VS Code
set vscode_dir_VOID=C:\Program Files\Microsoft VS Code
set project_dir=%CD%\Programming
set envname=budgetlake

call "%anaconda_dir%\Scripts\activate.bat" "%anaconda_dir%"
call conda activate %envname%
if exist "%vscode_dir_NULL%\Code.exe" (
	start "" "%vscode_dir_NULL%\Code.exe" -r "%project_dir%"
) else (
	start "" "%vscode_dir_VOID%\Code.exe" -r "%project_dir%"
)

exit