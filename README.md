# porter-squiggle
A recreation of the squiggle used during Porter Robinson's Nurture set near the end of Divinity.


Dependencies needed:
1. numpy
2. VPython
3. OpenSimplex
4. Jupyter Notebooks

VPython only works either in the browser version at https://www.glowscript.org/ or inside of a Jupyter Notebook. The code would run quicker on glowscript's IDE, but the
code isn't written to run there and you can't use outside modules like numpy. Since you need Jupyter Notebooks to run the code, you likely have Anaconda, so depending on your 
installation, you likely already have numpy installed. To install the others, open an Anaconda Prompt and type:

`pip install vpython opensimplex`


To change the size of the window produced, change the width and height in line 47 where it says `scene = vp.canvas(title='Nurturebook Pro', width=1000, height=1000)`
You can tweak the way the scribble looks by adjusting the parameters at the top: freq, resolution, and amp. Freq is likely to produce the changes you're looking for.
