How can I find the full path to a font from its display name on a Mac?

To find the full path to a font from its display name on a Mac, you can use the ATSFontGetFileReference function from the ApplicationServices framework after looking up the ATSFontRef. This can be done using ctypes in Python.



I learned Swing back in the day but now I've moved to Python and want to make some apps with GUIs. I haven't had the time to learn a new GUI API so I've been using Jython, but I would prefer to use CPython.

You're looking for a way to create GUIs in Python without having to learn a new GUI API, and you'd prefer to use CPython over Jython. You're also interested in a cross-platform, language-agnostic GUI markup language that would allow you to switch between GUI libraries and use the same markup across different languages.





Python works on multiple platforms and can be used for desktop and web applications, thus I conclude that there is some way to compile it into an executable for Mac, Windows and Linux.

The problem being I have no idea where to start or how to write a GUI with it, can anybody shed some light on this and point me in the right direction please?
To create a directly-executable cross-platform GUI app using Python, you will need a GUI library with Python bindings and a program to convert your Python scripts into standalone executables.

Some popular cross-platform GUI libraries with Python bindings are:

Tkinter - based on Tk GUI toolkit (free for commercial projects)
WxPython - based on WxWidgets (free for commercial projects)
PyQt - based on Qt (costly license for commercial projects)
To convert your Python scripts into standalone executables, you can use:

py2exe for Windows
Freeze for Linux
py2app for Mac OS
You can start by choosing a GUI library and then use one of the above programs to create a single executable for your desired platform.



When asked to create system XYZ and you ask to do it in Python over PHP or Ruby, what are the main features you can mention when they require you to explain it?

When explaining why you want to use Python over PHP or Ruby, you can mention that it's a matter of personal preference or situational details. If you're more comfortable and experienced with Python, you can say so. You can also ask if they're more comfortable with one of the other environments, and consider the long-term maintenance of the system. Additionally, if they ask you to use a technology or language you're not familiar with, be sure to inform them that it may take longer to complete.




"<p>I've got a menu in Python. That part was easy. I'm using <code>raw_input()</code> to get the selection from the user. </p>

<p>The problem is that <code>raw_input</code> (and input) require the user to press <kbd>Enter</kbd> after they make a selection. Is there any way to make the program act immediately upon a keystroke? Here's what I've got so far:</p> <pre><code>import sys print """"""Menu 1) Say Foo 2) Say Bar"""""" answer = raw_input(""Make a selection&gt; "") if ""1"" in answer: print ""foo"" elif ""2"" in answer: print ""bar"" </code></pre> <p>It would be great to have something like</p> <pre><code>print menu while lastKey = """": lastKey = check_for_recent_keystrokes() if ""1"" in lastKey: #do stuff... </code></pre>
"


To make the program act immediately upon a keystroke, you can use the following code on Linux:

import sys
import select
import termios
import tty

def getkey():
    old_settings = termios.tcgetattr(sys.stdin)
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    answer = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
    return answer

print """Menu
1) Say Foo
2) Say Bar"""

answer = getkey()

if "1" in answer: print "foo"
elif "2" in answer: print "bar"

For Windows, you can use the msvcrt module:

import msvcrt

print """Menu
1) Say Foo
2) Say Bar"""

answer = msvcrt.getch()

if b'1' in answer: print("foo")
elif b'2' in answer: print("bar")





"<p>Basically I want to get the number of lines-of-code in the repository after each commit.</p>

<p>The only (really crappy) ways I have found is to use git filter-branch to run ""wc -l *"", and a script that run git reset --hard on each commit, then ran wc -l</p>

<p>To make it a bit clearer, when the tool is run, it would output the lines of code of the very first commit, then the second and so on.. This is what I want the tool to output (as an example):</p>

<pre><code>me@something:~/$ gitsloc --branch master
10
48
153
450
1734
1542
</code></pre>

<p>I've played around with the ruby 'git' library, but the closest I found was using the .lines() method on a diff, which seems like it should give the added lines (but does not.. it returns 0 when you delete lines for example)</p>

<pre><code>require 'rubygems'
require 'git'

total = 0
g = Git.open(working_dir = '/Users/dbr/Desktop/code_projects/tvdb_api')


last = nil
g.log.each do |cur|
  diff = g.diff(last, cur)
  total = total + diff.lines
  puts total
  last = cur
end
</code></pre>
"



To achieve the desired output, you can use the following Python script:

import subprocess
import sys

def get_lines_of_code(commit):
    git = subprocess.Popen(["git", "show", commit + ":."), stdout=subprocess.PIPE)
    out, err = git.communicate()
    lines = out.count(b'\n') + 1 if out else 0
    return lines

def main(argv):
    git = subprocess.Popen(["git", "log", "--format=%H", "--reverse"], stdout=subprocess.PIPE)
    out, err = git.communicate()
    commits = out.decode().split('\n')[:-1]  # Remove empty string at the end
    for commit in commits:
        lines = get_lines_of_code(commit)
        print(lines)

if __name__ == '__main__':
    sys.exit(main(sys.argv))

This script uses the git show command to get the contents of each commit, and then counts the number of lines in the output. The git log command is used to get a list of commit hashes in reverse order.

Please note that this script assumes that you are running it from the root directory of your Git repository. Also, this script counts the total number of lines in the repository after each commit, including all files. If you want to count only the lines in a specific file or directory, you will need to modify the script accordingly.








"<p>Python uses the reference count method to handle object life time. So an object that has no more use will be immediately destroyed.</p>

<p>But, in Java, the GC(garbage collector) destroys objects which are no longer used at a specific time.</p> <p>Why does Java choose this strategy and what is the benefit from this?</p> <p>Is this better than the Python approach?</p> "
Java chooses a different strategy for garbage collection because the reference count method used by Python has some drawbacks. One of the main issues is circular references, where objects reference each other and cannot be deleted even if they are no longer needed. Python's CPython implementation addresses this with a separate garbage collection routine, but it can still be a problem.

Another drawback of reference counting is that it can make execution slower, as the interpreter needs to check the reference count every time an object is referenced or dereferenced. Garbage collection, on the other hand, can be done in a separate thread and can be more efficient in certain situations.

The benefit of Java's approach is that it can handle circular references more effectively and can be more efficient in terms of performance. However, whether it is better than the Python approach depends on the specific use case and requirements. Java's garbage collection can provide more predictable performance and can be more suitable for large-scale applications, but it can also introduce pauses in the application when the garbage collector runs.

In contrast, Python's reference counting can provide more immediate destruction of objects, which can be beneficial in certain situations. Ultimately, the choice between the two approaches depends on the specific needs of the application and the trade-offs between performance, predictability, and simplicity.





"<p>At the beginning of all my executable Python scripts I put the <a href=""http://en.wikipedia.org/wiki/Shebang_(Unix)"">shebang</a> line:</p>

<pre><code>#!/usr/bin/env python </code></pre> <p>I'm running these scripts on a system where <code>env python</code> yields a Python 2.2 environment. My scripts quickly fail because I have a manual check for a compatible Python version:</p> <pre><code>if sys.version_info &lt; (2, 4): raise ImportError(""Cannot run with Python version &lt; 2.4"") </code></pre> <p>I don't want to have to change the shebang line on every executable file, if it's possible; however, I don't have administrative access to the machine to change the result of <code>env python</code> and I don't want to force a particular version, as in:</p> <pre><code>#!/usr/bin/env python2.4 </code></pre> <p>I'd like to avoid this because system may have a newer version than Python 2.4, or may have Python 2.5 but no Python 2.4.</p> <p>What's the elegant solution?</p> <p>[Edit:] I wasn't specific enough in posing the question -- I'd like to let users execute the scripts without manual configuration (e.g. path alteration or symlinking in <code>~/bin</code> and ensuring your PATH has <code>~/bin</code> before the Python 2.2 path). Maybe some distribution utility is required to prevent the manual tweaks?</p> "


To switch to a different Python version, you can prepend the directory for that Python's executable to the PATH environment variable before invoking your script. This way, you don't have to change the shebang line on every executable file, and users can execute the scripts without manual configuration.

For example, if the desired Python version is installed in /path/to/python, you can run your script like this:

PATH=/path/to/python:$PATH ./your_script.py

This will ensure that the correct Python version is used to run your script, without requiring any manual tweaks or changes to the shebang line.

Alternatively, you can also use a distribution utility like setuptools or pip to manage your Python packages and ensure that the correct version is used. However, this approach may require more setup and configuration.

In summary, the elegant solution is to modify the PATH environment variable to point to the desired Python version before running your script. This approach is flexible, easy to implement, and doesn't require any changes to the shebang line or manual configuration by user