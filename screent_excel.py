text = ""
for i in range(65, 65+5):
    e_id = str(chr(i))+str(1)
    dlg.child_window(auto_id = e_id).click_input()
    ei = dlg.child_window(auto_id=e_id)
    ei.click_input()
    text+=(ei.legacy_properties()['Value'])
    text+=" "
print("Text read from sample.xlsx is:",(text))
