import subprocess
import sys, getopt

custom_path = "~/Books/"

def main(args):
    global custom_path
    
    # validate arguments
    # use custom_path (~/Books) if no directory supplied
    if len(args)>=1:
        if args[0] == '-p':
            dir_path = args[1]
        elif len(args) == 1 and args[0] == 'd':
            dir_path = custom_path
        else:
            AssertionError("Invalid argumnets, using default path of '~/Books/'")
    else:
        dir_path = custom_path
        
    # add '/' if it's omitted in the command line argument
    # eg: if supplied something like ~/Books
    if dir_path[-1] != '/':
        dir_path += '/'
    
    # exception handling in case of invalid directory or invalid file(s)
    try:
        # get all files in the directory
        # - returns a single string where each file is separated by '\n'
        file_list = subprocess.Popen([f'ls {dir_path}'], shell=True, stdout=subprocess.PIPE)\
        .communicate()[0].decode('utf-8')

        # clean up the string and append only those files ending with .pdf .epub
        # ie, filter out all the books in the directory
        book_list = ""
        for f in file_list.splitlines():
            if (f.lower().endswith(('.pdf', '.epub'))):
                book_list += f + "\n"

        # pipe the string containing book names into dmenu
        # dmenu then displays this list of books which the user can select from
        # store the book (string) that was selected from dmenu
        selected_book = subprocess.Popen([f"printf '%s' '{book_list}' | dmenu -l {len(book_list.splitlines())} -i"],\
            shell=True, stdout=subprocess.PIPE)\
                .communicate()[0].decode('utf-8').splitlines()[0]

        # pass that selected string into zathura - thereby effectively opening the book for viewing
        zat = subprocess.Popen([f"zathura {dir_path}'{selected_book}'"], shell=True, stdout=subprocess.PIPE)
        
    except IOError:
        print("Invalid file/directory. Exiting.")
        raise SystemExit

if __name__ == "__main__":
    main(sys.argv[1:]) # since [0] is the program name itself

# TODO
# - number each entry
