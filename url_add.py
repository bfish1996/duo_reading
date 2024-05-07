#Create a loop, adding URLs to an array for now. 
#Future, for a database with fields like "done" etc... 
#Do you want to add another?

url = []

def show_url():
    while True:
        url.append (input("Add your URL"))
        add_another = input("Add another?")
        if add_another == "T":
            continue
        else:
            print(url)
            exit()
    return site_url