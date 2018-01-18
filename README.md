# LogAnalysis

Small program that run few log analysis and puts output into comand line.

This prgram is for Log Analysis project for Udacity Nanodegree Fullstack web developer (*as of Janary 2018*).

## Running under Win10

To run this project you will need 
[Git Bash](https://git-scm.com/), 
[Python 3](https://www.python.org/)& 
[Vagrant](https://www.vagrantup.com/) 
instled on your machine.

Copy files into your local vagrant folder.

Copy [Udacity DB file](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) into your local vagrant folder.

Run Bash, navigate to your vagrant folder. 

Run Vagrant. 
```bash
vagrant up
```

Log into it.
```bash
winpty vagrant ssh
```

Navigate to your vagrant folder
```bash
cd /vagrant
```

Load DB ().
```bash
psql -d news -f newsdata.sql
```

Run program
```bash
python log_analysis.py
```

Next you will see results in comand line.
