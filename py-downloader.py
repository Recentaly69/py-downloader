# python downloader (py-downloader) by sch#4975

import sys, requests

def main():

    url = sys.argv[1] # takes the second cmd argument as source

    response = requests.get(url, stream=True) # parse download
    length_of_download = float(response.headers.get('content-length')) # get file size
    name_of_file = url.split("/")[-1]
    name_of_file = name_of_file.replace("%",'').replace('.','').replace("20",'').replace("-",'').replace("fitgirlrepackssite",'') # removes unnecessary strings

    with open(name_of_file, "wb") as data:

        print(f"\nCurrent progress for {name_of_file}:")
        download_progress = 0
        for datasize in response.iter_content(chunk_size=4096): # split downloads to 4MB worth of data for progress bar
            download_progress += len(datasize) # add progress for what we already downloaded
            data.write(datasize) # write the file into our new file
            finished = int(50 * download_progress / length_of_download)
            sys.stdout.write("\r[%s%s]" % ('*' * finished, ' ' * (50-finished)) )  # the progress bar :)  
            sys.stdout.flush() # reset stdout.write output

if __name__ == '__main__': # execute main() only when imports are done

    main()
