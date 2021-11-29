# Dmenu-open-ebooks
Open your ebooks from dmenu; cool script that displays your list of books, contained inside a *specified* directory, in dmenu, where you can select the desired one and open it for viewing.
- Lists all the pdf/epub files in the specified directory via dmenu
- The selected file will be opened in zathura

## Requirements
- [Zathura](https://wiki.archlinux.org/title/Zathura) (with pdf support) : Document viewer.
- [dmenu](https://tools.suckless.org/dmenu/)

## Usage
```bash
python ebooks.py -p <path/to/directory>
```

If you want to permanently run the program on a certain directory, there's a `custom_path` variable which you can change to the desired directory. Then you can run the program without any extra arguments each time:

```python
python ebooks.py
```

If your DE/WM allows you to do so, better use would be to bind this program to a key.

## Demo
