import requests
import json
import argparse
import sys



def main(page=None, thefile=None):
    if page is not None:
        data = downloadData(page)
        return reformat(data,page)     
    elif thefile is not None:
        data = parseFile(thefile)
        return reformat(data,page)
        
def downloadData(page):
    response = requests.get('https://api.fbi.gov/wanted/v1/list', params={'page': page})
    if response.status_code == 200:
        data = response.json()
    return data
          
def parseFile(thefile): 
    try:      
        with open(thefile, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except(Exception):
        print("File not found")
        sys.exit(1)

def reformat(data,page = None):
    if(len(data['items']))>0:
        li=[]
        for item in data['items']:
            title = item['title']
            if(item['subjects'] != None):
                subjects = ','.join(item['subjects'])
            else:
                subjects = ""
            if(item['field_offices'] != None):
                field_offices = ','.join(item['field_offices'])
            else:
                field_offices = ""
            result = f"{title}þ{subjects}þ{field_offices}"
            li.append(result)
            print(result)        
        return li
    else:
        print(f"No data exists in Page {page}")  
        return None
   
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Process FBI Most wanted list data ")
    parser.add_argument("--file", type=str, required=False, help="Downloads data From FBI API page.")
    parser.add_argument("--page", type=int, required=False, help="Retrieves data from specified file location.")   
    args = parser.parse_args()
    if args.page:
        main(page=args.page)
    elif args.file:
        main(thefile=args.file)
    else:
        parser.print_help(sys.stderr)
    