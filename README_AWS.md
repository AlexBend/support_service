# AWS CodeDeploy

## Launch an instance

```
Choosing application and OS images
"ubuntu" for example

Key pair - выбрать SSH файл, заранее загруженый на AWS
```

## Настроить Security Groups
```
Inbound rules
Type: SSH, Port range: 22, Source: 0.0.0.0/0
Type: ALL TCP, Port range: 0 - 65535, Source: 0.0.0.0/0
```

## Уствновка на ubuntu
```
sudo apt update -y

sudo apt install docker-ce -y

sudo apt install docker-compose -y
```

## Загрузка с GitHub
```
git clone https://github.com/yourusername/yourrepository.git
```

## Start docker
```

sudo docker-compose build

sudo docker-compose up -d

sudo docker-compose exec app python src/manage.py collectstatic

sudo docker-compose exec app python src/manage.py migrate
 
sudo docker-compose exec app python src/manage.py createsuperuser
```