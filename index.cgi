#!/usr/local/bin/perl
use CGI;
use strict;



if (-e "./pwd") {
    print "Content-type:text/html\r\n\r\n";
    print "<html lang=\"en\"><meta charset=\"utf-8\">\n";
 #   //<link rel=\"stylesheet\" type=\"text/css\" href=\"http://blog.fefe.de/bild.css\">";
    print "<head>\n";
    print "<title>Blog</title>\n";
    print "</head>\n<body><h2><a href=\"?\" style=\"text-decoration:none;color:black\">Blog</a></h2>";
    print "<b>This is your sub title where you can describe what the blog is all about...</b>\n";
    print "<p style=\"text-align:right\">Here you can put your contact info:  <a href=\"mailto:bloguser\">E-Mail</a><p>\n";

    my $time_now = time();
    
    my @months = qw( Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec );
    my @days = qw(Sun Mon Tue Wed Thu Fri Sat Sun);

    my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime();
    my $this_year = 1900+ $year;
    my $maxtime = 2147483647;
    my $ts = sprintf("%X", ($maxtime - $time_now));
    print "Timenow:$time_now maxtime:$maxtime   $mday $months[$mon] $days[$wday]\n Timestamp:$ts ThisYear:$this_year\n";
    my $cgi = new CGI();
    if ($cgi->param("ts")) {
	$ts = $cgi->param('ts');	
    }
    if (! $cgi->param("admin")) {
    	if ($cgi->param("y")) {
		$year =$cgi->param('y');	
	}
	if ($cgi->param("m")) {
		$mon = $cgi->param('m');
	}
        if ($cgi->param("d")) {
	    	$yday = $cgi->param('d');
 	}	
    } else { ############ Insert entry
	if (!(-d $this_year)) {
		mkdir ($this_year);
    	}
    
	if (!(-d "$this_year/$mon")) {
		mkdir ("$this_year/$mon");
	}
	if (!(-d "$this_year/$mon/$mday")) {
                mkdir ("$this_year/$mon/$mday");
        }
	open (LOGENTRY, ">$this_year/$mon/$mday/$ts") or die "Could not open file $!";
 	my $entry = to_html($cgi->param('e'));
	print LOGENTRY $entry;	
   	close (LOGENTRY); 
    }


} else {
print "Content-type:text/html\r\n\r\n<html lang=\"en\"><meta charset=\"utf-8\">\n<body><h2>This blog seems unconfigured, please contact the administrator!</h2></body></html>";
exit;
}

sub to_html {
	my $formtext = shift;
	$formtext =~ s/(\")/&quot;/g;
	$formtext =~ s/(>)/&gt;/g;
	$formtext =~ s/(<)/&lt;/g;
	$formtext =~ s/(ß)/&szlig;/g;
	$formtext =~ s/(ä)/&auml;/g;
	$formtext =~ s/(ö)/&ouml;/g;
	$formtext =~ s/(ü)/&uuml;/g;
	$formtext =~ s/(Ä)/&Auml;/g;
        $formtext =~ s/(Ö)/&Ouml;/g;
        $formtext =~ s/(Ü)/&Uuml;/g;



	return ($formtext);

}
