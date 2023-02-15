import yaml

extra_attributes = ["contacts","name","shortdescription","description","postdate"]

def get_yaml(f):
    with open(f, "r") as stream:
        try:
            data = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return data

print("Hi there. Checking your projects")

metadata=get_yaml("project_metadata.yml")

all_attributes = metadata.keys()

# find projects

import os,sys
filelist=[]
for root, dirs, files in os.walk("./projects"):
    for file in files:
        #append the file name to the list
        if file.endswith('yml'):
            filelist.append(os.path.join(root,file))

for f in filelist:
    data = get_yaml(f)
    found_attributes=data.keys()
    for att in found_attributes:
        if att not in all_attributes and att not in extra_attributes:
            print("Found unexpected attribute")
            print(f)
            print(att)
            sys.exit(1)
        if att not in extra_attributes:
            vals = data[att]
            for v in vals:
                if v not in metadata[att] and v!="Any":
                    print("Found unexpected value")
                    print(f)
                    print(att)
                    print(v)
                    sys.exit(1)
    for att in all_attributes:
        if att not in found_attributes:
            print("Missing expected attribute")
            print(f)
            print(att)
            sys.exit(1)
    for att in extra_attributes:
        if att not in found_attributes:
            print("Missing expected attribute")
            print(f)
            print(att)
            sys.exit(1)

print("Success")
print("Checked ",str(len(filelist)),"projects")
