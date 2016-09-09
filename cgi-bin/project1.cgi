#!/bin/bash
# Jingjie Zhang 106671199

echo 'Content-type: text/html'
echo ''

# return HTML
echo '<html>'
echo '<head>'
# have least one style sheet
echo '<link rel="stylesheet" rev="stylesheet" href="http://www.csun.edu/~jz710151/css/project1.css">'
echo '<meta http-equiv="Content-Type" content="text/html; charst=UTF-8">'
echo '<title>Jingjie Zhang</title>'
echo '</head>'
echo '<body><p>'
echo '<span id="zjj1">Jingjie Zhang Comp 490 Project1</span><br>'
echo '</p>'
echo '<body><p>'
echo '<span id="zjj1">Linked to CSS on sever</span><br>'
echo '</p>'
# consume information information from the file system
echo "<p>SCRIPT_FILENAME is $SCRIPT_FILENAME</p>" 
# respond to the GET verb;have a different response based upon the URI provided;consume information from a remote web-server
/usr/bin/curl -s ${QUERY_STRING}
echo '<p>'
echo 'Jingjie Zhang Comp 490 Project1<br>'
echo '</p></body>'
echo '</html>'

exit 0
