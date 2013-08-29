xoomProject
===========

Objective is to log vital statistics of the Indian Rupee and then make a transaction when the price is right! 



This project comes with a crontab file - 

PERL_LWP_SSL_VERIFY_HOSTNAME=0
0 */2 * * * perl -MLWP::UserAgent -e 'my $ua=LWP::UserAgent->new(); my $r = $ua->get("https://www.xoom.com/india"); $r->decoded_content =~ m/1\s*USD\s*=\s*(\d+\.\d+)\s*INR/i; print (localtime .",$1\n");' >> INRfile
0 */2 * * * python /Users/aagrawal/Documents/XoomProject/xoomScraper.py >> /Users/aagrawal/INRfilePython

-------------------

