from subprocess import Popen, PIPE

SCRIPT = """/usr/bin/osascript <<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""

def set_background(filename):
    p = Popen(SCRIPT % filename, shell=True, stdout=PIPE, stderr=PIPE)
    output, error = p.communicate()
    if p.returncode != 0:
        print 'setting desktop failed: %d %s %s' % (p.returncode, output, error)

if __name__ == '__main__':
    import sys
    set_background(sys.argv[1])
