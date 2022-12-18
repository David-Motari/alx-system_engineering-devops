# Postmortem

The incident occurred at 00:07 East African Time on an isolated instance of Linux on an Apache web server. The error was caused by the GET requests sent to the server, which resulted in the failure of the HTML file to be interpreted.

# Debugging Process.
After opening the project, David, the Bug debugger, encountered the issue. He was then informed to address it at around 06:20 EAT. He immediately started working on the issue.
    First inspected the running processes using the command ps aux. Two apache2 processes - root and www-data - were running properly.
    After looking in the directory `/etc/apache2`, I was able to determine that the web server was accessing content from the directory `/var/www/html`.
    Used strance and curl to check the PID of root but no issue was found
    He then used strance and curl on the `www-data` and realised there was a typo on the path to a file in the `wp-settings.php`
    He corrected the typo and test to ensure evrything is working fine.
    I wrote a bash script for future error fixing.

# Summation
A typo was causing the server not to find the location of the file causing a critical error.
# Prevention
it paramount to automate most of the process when configuring the server thsu avoiding such instances. Its also important to run tests to avoid runtime errors. Monitoring of the servers is also an important outage preventative startegy. 