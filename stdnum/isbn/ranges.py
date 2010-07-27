# ranges.py - list of ISBN prefix data and utility functions
#
# Copyright (C) 2010 Arthur de Jong
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301 USA

"""This module contains that current ISBN group and registrant prefixes as
they are registered with the International ISBN Agency. This information
is needed to correctly split an ISBN into an EAN.UCC prefix, a group prefix,
a registrant, an item number and a check-digit."""

# The place where the current version of RangeMessage.xml can be downloaded.
_download_url = 'http://www.isbn-international.org/agency?rmxml=1'

# What follows is a representation of the prefixes that are defined by
# International ISBN Agency to correctly split ISBNs. See the download()
# and output() methods on how to download and generate this data.

# generated from RangeMessage.xml, downloaded from
# http://www.isbn-international.org/agency?rmxml=1
# serial 0aad2b046ddd9b30e080cb2b24afc868
# date Thu, 20 May 2010 18:36:55 GMT
_prefixes = """
978 0-5 600-649 7-7 80-94 950-989 9900-9989 99900-99999
978-0 00-19 200-699 7000-8499 85000-89999 900000-949999 9500000-9999999
978-1 00-09 100-399 4000-5499 55000-86979 869800-998999 9990000-9999999
978-2 00-19 200-349 35000-39999 400-699 7000-8399 84000-89999 900000-949999
978-2 9500000-9999999
978-3 00-02 030-033 0340-0369 03700-03999 04-19 200-699 7000-8499 85000-89999
978-3 900000-949999 9500000-9539999 95400-96999 9700000-9899999 99000-99499
978-3 99500-99999
978-4 00-19 200-699 7000-8499 85000-89999 900000-949999 9500000-9999999
978-5 00-19 200-420 4210-4299 430-430 4310-4399 440-440 4410-4499 450-699
978-5 7000-8499 85000-89999 900000-909999 91000-91999 9200-9299 93000-94999
978-5 9500000-9500999 9501-9799 98000-98999 9900000-9909999 9910-9999
978-600 00-09 100-499 5000-8999 90000-99999
978-601 00-19 200-699 7000-7999 80000-84999 85-99
978-602 00-19 200-799 8000-9499 95000-99999
978-603 00-04 05-49 500-799 8000-8999 90000-99999
978-604 0-4 50-89 900-979 9800-9999
978-605 01-09 100-399 4000-5999 60000-89999 90-99
978-606 0-0 10-49 500-799 8000-9199 92000-99999
978-607 00-39 400-749 7500-9499 95000-99999
978-608 0-0 10-19 200-449 4500-6499 65000-69999 7-9
978-609 00-39 400-799 8000-9499 95000-99999
978-612 00-29 300-399 4000-4499 45000-49999 50-99
978-613 0-9
978-614 00-39 400-799 8000-9499 95000-99999
978-615 00-09 100-499 5000-7999 80000-89999
978-616 00-19 200-699 7000-8999 90000-99999
978-617 00-49 500-699 7000-8999 90000-99999
978-7 00-09 100-499 5000-7999 80000-89999 900000-999999
978-80 00-19 200-699 7000-8499 85000-89999 900000-999999
978-81 00-19 200-699 7000-8499 85000-89999 900000-999999
978-82 00-19 200-699 7000-8999 90000-98999 990000-999999
978-83 00-19 200-599 60000-69999 7000-8499 85000-89999 900000-999999
978-84 00-14 15000-19999 200-699 7000-8499 85000-89999 9000-9199
978-84 920000-923999 92400-92999 930000-949999 95000-96999 9700-9999
978-85 00-19 200-599 60000-69999 7000-8499 85000-89999 900000-979999
978-85 98000-99999
978-86 00-29 300-599 6000-7999 80000-89999 900000-999999
978-87 00-29 400-649 7000-7999 85000-94999 970000-999999
978-88 00-19 200-599 6000-8499 85000-89999 900000-949999 95000-99999
978-89 00-24 250-549 5500-8499 85000-94999 950000-999999
978-90 00-19 200-499 5000-6999 70000-79999 800000-849999 8500-8999 90-90
978-90 910000-939999 94-94 950000-999999
978-91 0-1 20-49 500-649 7000-7999 85000-94999 970000-999999
978-92 0-5 60-79 800-899 9000-9499 95000-98999 990000-999999
978-93 00-09 100-499 5000-7999 80000-94999 950000-999999
978-94 000-599 6000-8999 90000-99999
978-950 00-49 500-899 9000-9899 99000-99999
978-951 0-1 20-54 550-889 8900-9499 95000-99999
978-952 00-19 200-499 5000-5999 60-65 6600-6699 67000-69999 7000-7999 80-94
978-952 9500-9899 99000-99999
978-953 0-0 10-14 150-549 55000-59999 6000-9499 95000-99999
978-954 00-28 2900-2999 300-799 8000-8999 90000-92999 9300-9999
978-955 0000-1999 20-49 50000-54999 550-799 8000-9499 95000-99999
978-956 00-19 200-699 7000-9999
978-957 00-02 0300-0499 05-19 2000-2099 21-27 28000-30999 31-43 440-819
978-957 8200-9699 97000-99999
978-958 00-56 57000-59999 600-799 8000-9499 95000-99999
978-959 00-19 200-699 7000-8499 85000-99999
978-960 00-19 200-659 6600-6899 690-699 7000-8499 85000-92999 93-93 9400-9799
978-960 98000-99999
978-961 00-19 200-599 6000-8999 90000-94999
978-962 00-19 200-699 7000-8499 85000-86999 8700-8999 900-999
978-963 00-19 200-699 7000-8499 85000-89999 9000-9999
978-964 00-14 150-249 2500-2999 300-549 5500-8999 90000-96999 970-989
978-964 9900-9999
978-965 00-19 200-599 7000-7999 90000-99999
978-966 00-14 1500-1699 170-199 2000-2999 300-699 7000-8999 90000-99999
978-967 00-29 300-499 5000-5999 60-89 900-989 9900-9989 99900-99999
978-968 01-39 400-499 5000-7999 800-899 9000-9999
978-969 0-1 20-39 400-799 8000-9999
978-970 01-59 600-899 9000-9099 91000-96999 9700-9999
978-971 000-015 0160-0199 02-02 0300-0599 06-09 10-49 500-849 8500-9099
978-971 91000-98999 9900-9999
978-972 0-1 20-54 550-799 8000-9499 95000-99999
978-973 0-0 100-169 1700-1999 20-54 550-759 7600-8499 85000-88999 8900-9499
978-973 95000-99999
978-974 00-19 200-699 7000-8499 85000-89999 90000-94999 9500-9999
978-975 00000-00999 01-01 02-24 250-599 6000-9199 92000-98999 990-999
978-976 0-3 40-59 600-799 8000-9499 95000-99999
978-977 00-19 200-499 5000-6999 700-999
978-978 000-199 2000-2999 30000-79999 8000-8999 900-999
978-979 000-099 1000-1499 15000-19999 20-29 3000-3999 400-799 8000-9499
978-979 95000-99999
978-980 00-19 200-599 6000-9999
978-981 00-11 1200-1999 200-289 2900-9999
978-982 00-09 100-699 70-89 9000-9799 98000-99999
978-983 00-01 020-199 2000-3999 40000-44999 45-49 50-79 800-899 9000-9899
978-983 99000-99999
978-984 00-39 400-799 8000-8999 90000-99999
978-985 00-39 400-599 6000-8999 90000-99999
978-986 00-11 120-559 5600-7999 80000-99999
978-987 00-09 1000-1999 20000-29999 30-49 500-899 9000-9499 95000-99999
978-988 00-16 17000-19999 200-799 8000-9699 97000-99999
978-989 0-1 20-54 550-799 8000-9499 95000-99999
978-9927 00-09 100-399 4000-4999
978-9928 00-09 100-399 4000-4999
978-9929 0-3 40-54 550-799 8000-9999
978-9930 00-49 500-939 9400-9999
978-9931 00-29 300-899 9000-9999
978-9932 00-39 400-849 8500-9999
978-9933 0-0 10-39 400-899 9000-9999
978-9934 0-0 10-49 500-799 8000-9999
978-9935 0-0 10-39 400-899 9000-9999
978-9936 0-1 20-39 400-799 8000-9999
978-9937 0-2 30-49 500-799 8000-9999
978-9938 00-79 800-949 9500-9999
978-9939 0-4 50-79 800-899 9000-9999
978-9940 0-1 20-49 500-899 9000-9999
978-9941 0-0 10-39 400-899 9000-9999
978-9942 00-89 900-994 9950-9999
978-9943 00-29 300-399 4000-9999
978-9944 0000-0999 100-499 5000-5999 60-69 700-799 80-89 900-999
978-9945 00-00 010-079 08-39 400-569 57-57 580-849 8500-9999
978-9946 0-1 20-39 400-899 9000-9999
978-9947 0-1 20-79 800-999
978-9948 00-39 400-849 8500-9999
978-9949 0-0 10-39 400-899 9000-9999
978-9950 00-29 300-849 8500-9999
978-9951 00-39 400-849 8500-9999
978-9952 0-1 20-39 400-799 8000-9999
978-9953 0-0 10-39 400-599 60-89 9000-9999
978-9954 0-1 20-39 400-799 8000-9999
978-9955 00-39 400-929 9300-9999
978-9956 0-0 10-39 400-899 9000-9999
978-9957 00-39 400-699 70-84 8500-8799 88-99
978-9958 0-0 10-49 500-899 9000-9999
978-9959 0-1 20-79 800-949 9500-9999
978-9960 00-59 600-899 9000-9999
978-9961 0-2 30-69 700-949 9500-9999
978-9962 00-54 5500-5599 56-59 600-849 8500-9999
978-9963 0-2 30-54 550-734 7350-7499 7500-9999
978-9964 0-6 70-94 950-999
978-9965 00-39 400-899 9000-9999
978-9966 000-199 20-69 7000-7499 750-959 9600-9999
978-9967 00-39 400-899 9000-9999
978-9968 00-49 500-939 9400-9999
978-9970 00-39 400-899 9000-9999
978-9971 0-5 60-89 900-989 9900-9999
978-9972 00-09 1-1 200-249 2500-2999 30-59 600-899 9000-9999
978-9973 00-05 060-089 0900-0999 10-69 700-969 9700-9999
978-9974 0-2 30-54 550-749 7500-9499 95-99
978-9975 0-0 100-399 4000-4499 45-89 900-949 9500-9999
978-9976 0-5 60-89 900-989 9900-9999
978-9977 00-89 900-989 9900-9999
978-9978 00-29 300-399 40-94 950-989 9900-9999
978-9979 0-4 50-64 650-659 66-75 760-899 9000-9999
978-9980 0-3 40-89 900-989 9900-9999
978-9981 00-09 100-159 1600-1999 20-79 800-949 9500-9999
978-9982 00-79 800-989 9900-9999
978-9983 80-94 950-989 9900-9999
978-9984 00-49 500-899 9000-9999
978-9985 0-4 50-79 800-899 9000-9999
978-9986 00-39 400-899 9000-9399 940-969 97-99
978-9987 00-39 400-879 8800-9999
978-9988 0-2 30-54 550-749 7500-9999
978-9989 0-0 100-199 2000-2999 30-59 600-949 9500-9999
978-99901 00-49 500-799 80-99
978-99903 0-1 20-89 900-999
978-99904 0-5 60-89 900-999
978-99905 0-3 40-79 800-999
978-99906 0-2 30-59 600-699 70-89 90-94 950-999
978-99908 0-0 10-89 900-999
978-99909 0-3 40-94 950-999
978-99910 0-2 30-89 900-999
978-99911 00-59 600-999
978-99912 0-3 400-599 60-89 900-999
978-99913 0-2 30-35 600-604
978-99914 0-4 50-89 900-999
978-99915 0-4 50-79 800-999
978-99916 0-2 30-69 700-999
978-99917 0-2 30-89 900-999
978-99918 0-3 40-79 800-999
978-99919 0-2 300-399 40-69 900-999
978-99920 0-4 50-89 900-999
978-99921 0-1 20-69 700-799 8-8 90-99
978-99922 0-3 40-69 700-999
978-99923 0-1 20-79 800-999
978-99924 0-1 20-79 800-999
978-99925 0-3 40-79 800-999
978-99926 0-0 10-59 600-999
978-99927 0-2 30-59 600-999
978-99928 0-0 10-79 800-999
978-99929 0-4 50-79 800-999
978-99930 0-4 50-79 800-999
978-99931 0-4 50-79 800-999
978-99932 0-0 10-59 600-699 7-7 80-99
978-99933 0-2 30-59 600-999
978-99934 0-1 20-79 800-999
978-99935 0-2 30-59 600-699 7-8 90-99
978-99936 0-0 10-59 600-999
978-99937 0-1 20-59 600-999
978-99938 0-1 20-59 600-899 90-99
978-99939 0-5 60-89 900-999
978-99940 0-0 10-69 700-999
978-99941 0-2 30-79 800-999
978-99942 0-4 50-79 800-999
978-99943 0-2 30-59 600-999
978-99944 0-4 50-79 800-999
978-99945 0-5 60-89 900-999
978-99946 0-2 30-59 600-999
978-99947 0-2 30-69 700-999
978-99948 0-4 50-79 800-999
978-99949 0-1 20-89 900-999
978-99950 0-4 50-79 800-999
978-99952 0-4 50-79 800-999
978-99953 0-2 30-79 800-939 94-99
978-99954 0-2 30-69 700-999
978-99955 0-1 20-59 600-799 80-89 90-99
978-99956 00-59 600-859 86-99
978-99957 0-1 20-79 800-999
978-99958 0-4 50-94 950-999
978-99959 0-2 30-59 600-999
978-99960 0-0 10-94 950-999
978-99961 0-3 40-89 900-999
978-99962 0-4 50-79 800-999
978-99963 00-49 500-999
978-99964 0-1 20-79 800-999
978-99965 0-3 40-79 800-999
978-99966 0-2 30-69 700-799
978-99967 0-1 20-59 600-899
979 10-10
979-10 00-19 200-699 7000-8999 90000-97599 976000-999999
"""

def _expand():
    """Ensures that the prefix list is expanded as a dictionary to allow
    easy lookups. The default text form is compact but not very efficient."""
    global _prefixes
    if type(_prefixes) == dict:
        return
    # build a new dictionary of ranges from the string
    new_prefixes = dict()
    for line in _prefixes.splitlines():
        if line:
            ( prefix, r ) = line.split(' ', 1)
            range_list = new_prefixes.setdefault(prefix, [])
            for r in r.split(' '):
                low, high = r.split('-')
                range_list.append((len(low), low, high))
    # save the dictionary
    _prefixes = new_prefixes

def lookup(prefix, number):
    """Look up the specified prefix and split the provided number split in
    the correct parts. If the prefix cannot be found or the number is not
    in any of the defined ranges a tuple with one element is returned.
    The prefix and number together are expected to form a complete ISBN13
    number.

    >>> lookup('978', '9024538270')
    ('90', '24538270')
    >>> lookup('978-0', '471117094')
    ('471', '117094')
    """
    _expand()
    try:
        for length, low, high in _prefixes[prefix]:
            if low <= number[:length] <= high:
                return number[:length], number[length:]
    except KeyError:
        pass
    return ( '', number )

def load(fp):
    """Loads the data from the specified file descriptor. The provided file
    should match the format of the RangeMessage.xml file."""
    # this is in-line to avoid importing xml.sax for normal use
    import xml.sax
    # initialise data
    global _prefixes
    _prefixes = dict()
    # SAX handler class
    class RangeHandler(xml.sax.ContentHandler):
        def __init__(self):
            self._gather = None
            self._prefix = None
            self._range = None
            self._length = None
        def startElement(self, name, attrs):
            if name in ( 'MessageSerialNumber', 'MessageDate', 'Prefix',
                         'Range', 'Length',  ):
                self._gather = ''
        def characters(self, content):
            if self._gather is not None:
                self._gather += content
        def endElement(self, name):
            if name == 'MessageSerialNumber':
                global _download_serial
                _download_serial = self._gather.strip()
            elif name == 'MessageDate':
                global _download_date
                _download_date = self._gather.strip()
            elif name == 'Prefix':
                self._prefix = self._gather.strip()
            elif name == 'Range':
                self._range = self._gather.strip()
            elif name == 'Length':
                self._length = int(self._gather.strip())
            elif name == 'Rule' and self._length:
                r = ( self._length, ) + tuple( x[:self._length] for x in self._range.split('-') )
                _prefixes.setdefault(self._prefix, []).append(r)
            self._gather = None
    # start the actual parsing
    parser = xml.sax.make_parser()
    parser.setContentHandler(RangeHandler())
    parser.parse(fp)

def download(url=None):
    """Download the RangeMessage.xml data from the International ISBN Agency
    website or from the specified URL."""
    import urllib
    load(urllib.urlopen(url or _download_url))

def _wrap(text, max_len, sep=' '):
    """Generator that returns lines of text that are no longer than
    max_len. The sep arguments is the string to split on."""
    while text:
        i = len(text)
        if i > max_len:
            i = text.rindex(' ', 20, max_len)
        yield text[:i]
        text = text[i+1:]

def output(fp=None):
    """Print the downloaded range data to stdout (or a file if one is
    provided) in the compact text format suitable for inclusion in this
    module."""
    _expand()
    if not fp:
        import sys
        fp = sys.stdout
    # first print the header if we can
    try:
        fp.write('# generated from RangeMessage.xml, downloaded from\n'
                 '# %(url)s\n'
                 '# serial %(serial)s\n'
                 '# date %(date)s\n'
                 '_prefixes = """\n' % { 'url':    _download_url,
                                         'serial': _download_serial,
                                         'date':   _download_date })
        headerprinted = True
    except NameError:
        headerprinted = False
    # print the actual prefixes
    prefixes = _prefixes.items()
    prefixes.sort()
    for prefix, ranges in prefixes:
        for line in _wrap(' '.join(r[1] + '-' + r[2] for r in ranges), 77 - len(prefix)):
            fp.write('%s %s\n' % ( prefix, line ) )
    # print the footer if the header was printed
    if headerprinted:
        fp.write('"""\n')
