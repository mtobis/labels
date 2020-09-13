template = """<html>
<head>
<style type=text/css>

@page {
        size: letter portrait;
        @frame content_frame {
            left: 50pt;
            width: 330pt;
            top: 50pt;
            height: 692pt;
            -pdf-frame-border: 1;    /* for debugging the layout */
        }
    }


@font-face {
  font-family: Lato,"Lato";
  src: url(Lato2OFL/Lato-Regular.ttf);
}


/* Bold */
@font-face {
   font-family: Lato;
   src: url(Lato2OFL/Lato-Regular.ttf);
   font-weight: bold;
}

/* Italic */
@font-face {
   font-family: Lato;
   src: url(Lato2OFL/Lato-Italic.ttf);
   font-style: italic;
}

/* Bold and italic */
@font-face {
   font-family: Lato;
   src: url(Lato2OFL/Lato-BoldItalic.ttf);
   font-weight: bold;
   font-style: italic;
}

p {
  text-align: center;
color: red;
}
</style>
</head>
<body>
%CONTENT
</body>
</html>
"""

separator = """<div>
    <pdf:nextpage /> 
</div> """

block = """<div style="border-style:solid; border-color: black; padding:20px; margin:40px; text-align:center; overflow:hidden; width:400px; clear=both;" >
<span style="font-size:x-large; font-family:Lato;">TITLE gggg</span><br/>
<b>ARTIST ggg</b><br/>
MEDIUM ggg<br/>
DIMENSIONS<br/>
PRICE
</div>
<p>&nbsp;</p>
"""

outfnam = "test.html"

outf = open(outfnam,"w")

content = block + block + separator + block

outtext = template.replace("%CONTENT",content)

outf.write(outtext)
outf.close()
