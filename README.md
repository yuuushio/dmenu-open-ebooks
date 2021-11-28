# Description
Cool script that allows you to select and open an ebook via dmenu, given the directory that contains these desired books/pdfs.
- Lists all the pdf/epub files in the specified directory via dmenu
- The selected file will be opened in zathura for viewing

# Dependencies
- [Zathura](https://wiki.archlinux.org/title/Zathura) (with pdf support) : Document viewer.
- [dmenu](https://tools.suckless.org/dmenu/)

# Usage
```bash
python ebooks.py -p <path/to/directory>
```

If you want to permanently run the program on a certain directory, there's a `custom_path` variable which you can change to the desired directory. Then you can run the program without any extra arguments each time:

```python
python ebooks.py
```

If your DE/WM allows you to do so, better use would be to bind this program to a key.

# Demo
