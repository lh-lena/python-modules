## _00_myawesomescript.sh

The goal of this exercise is to write and turn-in a shell script that displays the real
address of a supposedly valid bit.ly address (that is, "the address the bit.ly link leads
towards).
As stated in this exercise header, you can only use the following shell commands:
curl, grep and cut. You best bet is to start reading the curl manual. To do so, type
man curl in your terminal.

Here is an example of how your shell script should behave:
$> ./myawesomescript.sh bit.ly/1O72s3U
http://42.fr/
$>

## _01_var_to_dict.py 

Create a script named var_to_dict.py in which you will copy the following list of d
couples as is in one of your functions:
d = [
('Hendrix' , '1942'),
('Allman' , '1946'),
('King' , '1925'),
('Clapton' , '1945'),
('Johnson' , '1911'),
('Berry' , '1926'),
('Vaughan' , '1954'),
('Cooder' , '1947'),
('Page' , '1944'),
('Richards' , '1943'),
('Hammett' , '1962'),
('Cobain' , '1967'),
('Garcia' , '1942'),
('Beck' , '1944'),
('Santana' , '1947'),
('Ramone' , '1948'),
('White' , '1975'),
('Frusciante', '1970'),
('Thompson' , '1949'),
('Burton' , '1939')
]

Your script must turn this variable into a dictionary. The year will be the key, the
name of the musician the value. It must then display this dictionary on the standard
output following a clear format:
1970 : Frusciante
1954 : Vaughan
1948 : Ramone
1944 : Page Beck
1911 : Johnson
...
