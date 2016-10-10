# a Douban movie spider based on scrapy

## python

```
virtualenv venv --no-site-packages
```

```
source venv/bin/activate
```

```
pip freeze > requirements.txt
```

```
pip install -r requirements.txt
```
scrapy
pypiwin32
psycopg2

start spider
```
scrapy crawl doubanMovie
scrapy crawl doubanAllMovie
```

## server 

```
sudo chown -R user:group directory
```

```
git init --bare
```

in kooks, post-receive
```
sudo touch post-receive
```

```
git --work-tree=dir_of_proj --git-dir=dir_of_git_repo checkout -f
```

make post-receive executable
```
sudo chmod +x filename
```

install scrapy failed
```
sudo apt-get build-dep python-lxml

sudo pip install lxml --upgrade
sudo apt-get install build-essential libssl-dev libffi-dev python-dev

pip install scrapy

```

###install postgresql and psycopg2
```
sudo apt-get install postgresql
```
```
sudo apt-get install python-psycopg2
```
```
sudo apt-get install libpq-dev
```

```
pip install psycopg2
```

### postgresql 

```
sudo -i -u postgres
psql

postgre: \q

```

```
createuser --interactive
```

list database
```
select datname from pg_database;
```


list user
```
\du
```

create user
```
CREATE user agovil WITH PASSWORD 'Kh@rt0um';
```

```
psql -h localhost -d postgres –p 5432
```


### linux cmd

```
sudo passwd user
```
