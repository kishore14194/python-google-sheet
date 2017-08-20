# This python file can be used to view, add, delete values from Google Sheet

1. Create a Google Sheet and name it as "New_refund_sheet"
2. Open google developer console
    * Goto
            --> Library
                    --> Create new project
                            --> Enable Google Drive API
                                    --> Create credentials
                                            --> Choose API from as WEB SERVER and data will you be accessing to APPLICATION DATA
                                                    --> Set service account name, choose the role as PROJECT -> EDITOR and set key type as JSON
                                                            --> A JSON file will be generated
                                                                    --> Rename and Replace the file with drive_secret_key.json

3. Install the libraries in requirement.txt file
4. In drive_secret_key.json, copy the "client_email" key and share it with the google sheet that you need to gonna access.
5. Now the sheet is accessible and can be edited.