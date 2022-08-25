    def runOlScript(outdest, filefmt, olreadfolder, olprocessedfolder, guiEntry, proc):
    outdest = os.path.normpath(outdest)
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = _find_subfolder(outlook.Folders, olreadfolder)
    if inbox is None:
        sys.exit(f'No Folder {olreadfolder} found!!! Exiting.')
    procbox = _find_subfolder(outlook.Folders, olprocessedfolder)
    if procbox is None:
        sys.exit(f'Folder {olprocessedfolder} not found!!! Exiting.')

    messages = inbox.Items
    if len(messages) == 0:
        _scriptOutput( 'No emails found in folder [{}]'.format(olreadfolder), gui_entry)
    mail_counter = 0
    for msg in list(messages):
        b_processed = False
        if proc == 'olatt':
            for atmt in msg.Attachments:
                if filefmt == 'blank' or str.lower(_right(atmt.FileName, len(filefmt))) == str.lower(filefmt):
                    temp_filename = os.path.normpath(os.path.join(outdest, f'{msg.Subject} {atmt.FileName}'))
                    try:
                        atmt.SaveAsFile(temp_filename)
                        print('File Successfully Saved [{}]'.format(temp_filename))
                        b_processed = True
                    except Exception as e:
                        _scriptOutput(str(e) + ' | File NOT saved [{}]'.format(temp_filename), gui_entry)
        if proc == 'olbody':
            listbody = msg.Body.split("\r\n")
            temp_filename = os.path.normpath(os.path.join(outdest, f'{msg.Subject} {msg.CreationTime.strftime("%Y%m%d")} .csv'))
            b_processed = True
            with open(temp_filename, 'w', newline='') as file:
                writer = csv.writer(file)
                for row in listbody:
                    writer.writerow([row])
        if b_processed and procbox is not None:
            mail_counter += 1
            msg.Move(procbox)

    return 'Succesfully processed {} emails!'.format(mail_counter) if mail_counter > 0 else 'No emails processed'
