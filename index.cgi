#!/usr/bin/perl
use CGI;
use strict;



if (-e "./pwd") {
    print "Content-type:text/html\r\n\r\n";
    print "<html lang=\"en\"><meta charset=\"utf-8\">\n";
    //<link rel=\"stylesheet\" type=\"text/css\" href=\"http://blog.fefe.de/bild.css\">";
    print "<head>\n";
    print "<title>Blog</title>\n";
    print "</head>\n<body><h2><a href=\"?\" style=\"text-decoration:none;color:black\">Blog</a></h2>";
    print "<b>This is your sub title where you can describe what the blog is all about...</b>\n";
    print "<p style=\"text-align:right\">Here you can put your contact info:  <a href=\"mailto:bloguser\">E-Mail</a><p>\n";



} else {
print "Content-type:text/html\r\n\r\n<html lang=\"en\"><meta charset=\"utf-8\">\n<body><h2>This blog seems unconfigured, please contact the administrator!</h2></body></html>";
exit;
}
