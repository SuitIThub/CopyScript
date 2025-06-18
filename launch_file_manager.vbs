Set objShell = CreateObject("WScript.Shell")
Set objFSO = CreateObject("Scripting.FileSystemObject")

' Get the directory where this VBS script is located
strScriptPath = objFSO.GetParentFolderName(WScript.ScriptFullName)

' Change to the script directory and run the batch file
objShell.CurrentDirectory = strScriptPath
objShell.Run "run_file_manager.bat", 1, False 