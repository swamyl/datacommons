
"""
Created on Fri Jun  1 09:37:39 2018

@author: swamyl
"""



import xml.etree.ElementTree as ET
import glob
import json




# read data_dict file
def data_dict(xml_file):

    subj_dd_tree = ET.parse(xml_file)
    subj_root = subj_dd_tree.getroot()

    data_dict = []

    # iterate over variables tag
    for child in subj_root:
        if child.tag == "variable":
            var = { "id": child.attrib['id'], "type": None }
            data_dict.append(var)
            encoded_values = []
            #all the tags in xml
            for gchild in child:
                if gchild.tag == "name":
                    var[gchild.tag] = gchild.text
                if gchild.tag == "description":
                    var[gchild.tag] = gchild.text
                if gchild.tag == "type":
                    var[gchild.tag] = gchild.text
                if gchild.tag == "comment":
                    var[gchild.tag] = gchild.text
                if gchild.tag == "unit":
                    var[gchild.tag] = gchild.text
                if gchild.tag == "logical_min":
                    var[gchild.tag] = gchild.text
                if gchild.tag == "logical_max":
                    var[gchild.tag] = gchild.text    
                #handle the encoded values
                if gchild.tag == "value":
                    encoded_values.append({ 'code': gchild.attrib['code'], 'value':gchild.text })   

            if var['type'] == "encoded values":
                var['values'] = encoded_values
                #print(var)
    xml_data = { "data_dict": data_dict }
    return xml_data

filelist=glob.glob("C:/Users/swamyl/Desktop/decrypted_files%2Fphs000920.v2.pht004897.v2.TOPMed_WGS_GALAII_Subject.data_dict.xml")
for name in filelist :
    #print (name)
    my_dict=data_dict(name)   
json_data=json.dumps(my_dict, indent=4, sort_keys=False)
print(json_data)
file = open(name+".json","w")
file.write(json_data)
file.close()
