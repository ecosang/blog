This project based on [https://github.com/cczhong11/Resume-Generator]

I installed Miktex instead of textlive. Miktex is lighter.

`BuildResume.py` constructs all structure. Overall structure is managed by sang.json
`GetLatex.py` loads data file stored in `ProjectJson` folder. 
In `ProjectJson` folder, the details of all information for each section put.
Therefore, edit / add sections in `BuildResume.py` and `GetLatex.py` first, and then add items in `ProjectJson`.

After that, run below script to create pdf file in 

`python BuildResume.py sang.json`