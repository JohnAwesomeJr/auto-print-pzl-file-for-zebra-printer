# auto-print-pzl-file-for-zebra-printer

This is a python sctipt that is designed to run in the background of a windows machine that will automaticly print a ".zpl" file as soon as it arives in a spacific folder in windows.

1. open up the "printer.py" file in a text editor.
1. change the printer_name variable to be the printer that you want to use. make sure you only change what is inside the quote marks. there is a lower case r right before the string and that is there on purpose. you can find out what the printer name is by trying to print a page in microsoft edge and it will give you a list of all available printers. just find the one you want and copy the path exactly.
1. now change the directory_path to the path you want the script to check if there are any new .zpl files. it will check it every 5 seconds.

1. Open Task scheduler
1. From Action menu select Create Task
1. make sure Run weather the user is logged in or not is checked (don't check hidden)
1.configure for windows 10 (or your windows version
At Triggers tab, click New.
Begin the task: at system startup.
1. press okay
1. At Actions tab, click New
1. At New Action window, click Browse.
1. action: Start Program
1. program/script should be ```"C:\Windows\System32\cmd.exe"```
1. in the add arguments box type ```/k python3 "C:\Users\PROD 0\Desktop\printer.py"``` but change it to match the path of printer.py script.
1. now restart your computer and the script should be running in the background. to check if it is working try putting a .zpl file in the directory you added to the directory_path variable in the printer.py file.
1. thats it! have fun!
