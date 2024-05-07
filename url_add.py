#Create a loop, adding URLs to an array for now. 
#Future, for a database with fields like "done" etc... 
#Do you want to add another?

site_urls = []

def show_url(site_urls):
    while True:
        site_urls.append (input("Add your URL"))
        add_another = input("Add another?")
        if add_another == "T":
            continue
        else:
            print(site_urls)
            return site_urls
            exit()

show_url(site_urls)

for urls in site_urls:
    print(urls)

# Open a file in write mode ('w')
with open('urls.txt', 'a') as f:
    # Write content to the file
    f.write(f"{urls}\n")