# returns True if malicious
# returns false otherwise
import re

'''
REGULAR EXPRESSION IS BASED ON https://forensics.cert.org/latk/loginspector.py
'''

def detectSXX(query):
    regex = re.compile('/(\b)(on\S+)(\s*)=|script|(<\s*)(\/*)script/')
    if regex.search(query):
        return True

    regex = re.compile("<(?:[^>=]|='[^']*'|=\"[^\"]*\"|=[^'\"][^\\s>]*)*>")
    if regex.search(query):
        return True
    return False




def detectSQLi(query):

    if check_regex('drop|delete|truncate|update|insert|select|declare|union|create|concat', query):
        return True

    if check_regex('((\%3D)|(=))[^\n]*((\%27)|(\')|(\-\-)|(\%3B)|(;))|\w*((\%27)|(\'))((\%6F)|o|(\%4F))((\%72)|r|(\%52))', query):
        return True

    if check_regex('exec(\s|\+)+(s|x)p\w+', query):
        return True

    if check_regex('/\w*((\%27)|(\'))((\%6F)|o|(\%4F))((\%72)|r|(\%52))/ix', query):
        return True

    if check_regex('/(\%27)|(\')|(\-\-)|(\%23)|(#)/ix', query):
        return True

    if check_regex('.*\[select\]\s+.*\[into\].*', query):
        return True

    if check_regex('.*\[select\]\s+.*\[from\].*', query):
        return True

    if check_regex('.*\[insert\]\s+.*\[into\].*', query):
        return True

    if check_regex('.*\[drop\]\s+.*\[database\].*', query):
        return True

    if check_regex('.*\[drop\]\s+.*\[table\].*', query):
        return True

    if check_regex('.*\[delete\]\s+.*\[from\].*', query):
        return True

    if check_regex('.*\[exec\].*(%28|\().*(%29|\)).*', query):
        return True

    if check_regex('.*\[update\](%20|\+)(%20|\+|.)*\[set\].*', query):
        return True

    if check_regex('((WHERE|OR)[ ]+[\(]*[ ]*([\(]*[0-9]+[\)]*)[ ]*=[ ]*[\)]*[ ]*\3)|AND[ ]+[\(]*[ ]*([\(]*1[0-9]+|[2-9][0-9]*[\)]*)[ ]*[\(]*[ ]*=[ ]*[\)]*[ ]*\4', query):
        return True

    return False


def check_regex(reg, query):
    regex = re.compile(reg, re.IGNORECASE)
    if regex.search(query):
        return True



'''
REGULAR EXPRESSION IS BASED ON https://www.trustwave.com/Resources/SpiderLabs-Blog/ModSecurity-Advanced-Topic-of-the-Week--Remote-File-Inclusion-Attack-Detection/
'''


def detectRFI(query):
    regex = re.compile('^(?:ht|f)tps?:\/\/(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', re.IGNORECASE)
    if regex.search(query):
        return True

    regex = re.compile('(?:\binclude\s*\([^)]*(ht|f)tps?:\/\/)', re.IGNORECASE)
    if regex.search(query):
        return True

    regex = re.compile('(?:ft|htt)ps?.*\?+$', re.IGNORECASE)
    if regex.search(query):
        return True

    regex = re.compile('^(?:ht|f)tps?://(.*)\?$', re.IGNORECASE)
    if regex.search(query):
        return True

    return False


'''
REGULAR EXPRESSION IS BASED ON https://github.com/emposha/PHP-Shell-Detector
'''


def detectWebShell(query):
    regex = re.compile(
        '%(preg_replace.*\/e|`.*?\$.*?`|\bcreate_function\b|\bpassthru\b|\bshell_exec\b|\bexec\b|\bbase64_decode\b|\bedoced_46esab\b|\beval\b|\bsystem\b|\bproc_open\b|\bpopen\b|\bcurl_exec\b|\bcurl_multi_exec\b|\bparse_ini_file\b|\bshow_source\b)%',
        re.IGNORECASE)
    if regex.search(query):
        return True

    return False

