import win32print
import os
import time

# Specify the printer name and directory path
printer_name = r"\\PROD-SIDE-20\Zebra  ZP 450-200 dpi"
directory_path = r"C:\Users\PROD 0\Downloads"

# Keep track of the files already printed
printed_files = set()

while True:
    # Get a list of all .zpl files in the directory
    zpl_files = [f for f in os.listdir(directory_path) if f.endswith('.zpl')]

    # Find any new files that haven't been printed yet
    new_files = set(zpl_files) - printed_files

    # Print any new files
    for file_name in new_files:
        file_path = os.path.join(directory_path, file_name)

        # Open the file and read the content
        with open(file_path, 'rb') as f:
            file_content = f.read()

        # Open the printer and print the file
        printer_handle = win32print.OpenPrinter(printer_name)
        job_info = win32print.GetPrinter(printer_handle, 2)
        job_id = win32print.StartDocPrinter(printer_handle, 1, (file_name, None, "RAW"))
        win32print.StartPagePrinter(printer_handle)
        win32print.WritePrinter(printer_handle, file_content)
        win32print.EndPagePrinter(printer_handle)
        win32print.EndDocPrinter(printer_handle)
        win32print.ClosePrinter(printer_handle)

        # Add the file to the list of printed files
        printed_files.add(file_name)

        # Print status message
        print(f"Printed {file_name} on {printer_name}")

        # Delete the file after printing
        os.remove(file_path)

    # Wait for a few seconds before checking again
    time.sleep(5)

    # If no new files were found, print a message saying so
    if not new_files:
        print("No new .zpl files found")
