Coding on paper
===============
Sounds like a good idea. **No!**

This is my implementation of a post on r/ProgrammerHumor about
["coding on paper"](https://www.reddit.com/r/ProgrammerHumor/comments/1blif1w/codingonpaper/), which I wanted to make
for some reason.

This uses Python-tesseract for OCR and `eval()` to run that code in Python. Before actually running, this will show the
scanned code and ask if you want to actually run that code, but you can turn that feature off using `-f`.

Scan to a file named `./code.png`. It will detect the file and show you the code. Does not work if indented currently.