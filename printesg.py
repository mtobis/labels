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
   src: url(Lato2OFL/Lato-Bold.ttf);
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
</div>
<p>&nbsp;</p> """


block = """<div style="border: 2px solid black; text-align:center; overflow:hidden; width:400px; clear=both; padding:30px; {color} {bordermod} ">
<span style="font-size:x-large; font-family:Lato; font-weight:800;">{title} gg<em>gg</em></span><br/>
<b>{artist} ggg</b><br/>
{info}<br/>
{price}
</div>
"""




block2 = block.replace('">',' border-top: 0;">',1)

block3 = """<p>&nbsp;</p><div style="border: 2px solid black; overflow:hidden; width:400px; clear=both; text-align:center; color: white; border-bottom: 0; padding:30px;">
<span style="font-size:x-large; font-family:Lato; ">TITLE gggg</span><br/>
<b>ARTIST ggg</b><br/>
MEDIUM ggg<br/>
DIMENSIONS<br/>
PRICE
</div>
"""

b1dict = {
    "color": "",
    "bordermod": "",
    "title": "Frilly Tulip",
    "artist": "Michael Tobis",
    "info": 'alcohol ink on tracing paper, 8.5" x 11 "',
    "price": '$1'
    }

b1 = block.format(**b1dict)

b2dict = b1dict.copy()
b2dict["bordermod"] = ' border-top: 0; '

b2 = block.format(**b2dict)

b3dict = b1dict.copy()
b3dict["bordermod"] = ' border-bottom: 0; '
b3dict["color"] = ' color: white; '

b3 = block.format(**b3dict)

outfnam = "test.html"

outf = open(outfnam,"w")

content = b1 + "<p>&nbsp;</p>" + b3 + b2 + separator +"<p>next page</p>"

outtext = template.replace("%CONTENT",content)

outf.write(outtext)
outf.close()
