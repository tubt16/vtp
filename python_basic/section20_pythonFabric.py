from fabric.api import *

def greeting(msg):
    print "Good %s" %msg

def system_info():
    print "Disk space"
    local("df -h")

    print "RAM size"
    local("free -m")

    print "System uptime"
    local("uptime")

def remote_exec():
    print "Get system info"
    run("df -h")
    run("free -m")
    run("uptime")

    sudo ("yum install mariadb-server -y")
    sudo ("systemctl start mariadb")
    sudo ("systemctl enable mariadb")

def web_setup(WEBURL, DIRNAME):
    print "##########################################"
    local("apt install zip unzip -y")

    print "##########################################"
    print "Installing dependencies"
    print "##########################################"
    sudo ("yum install -y httpd unzip wget")

    print "##########################################"
    print "Start, enable service"

    sudo ("systemctl start httpd")
    sudo ("systemctl enable httpd")

    print "##########################################"
    print "Download and pushing website to webservers"
    local (("wget -O website.zip %s") % WEBURL)
    local ("unzip -o website.zip")

    with lcd(DIRNAME):
        local("zip -r tooplate.zip * ")
        put("tooplate.zip", "/var/www/html", use_sudo=True)

    with cd("/var/www/html"):
        sudo("unzip -o tooplate.zip")

    sudo("systemctl restart httpd")

    print "Website setup is done"