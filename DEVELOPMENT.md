## DEVELOPMENT - Flask Web App - Docker
Bilgisayarina `docker` indir.

Reponun klonunu al. Ve klasorun icine git. Daha sonra sadece `$ sudo docker-compose up` komutu ile herseyi ayaga kaldir.

Daha sonrasinda "localhost:5000/initial_db" diyerek tablolari olusturuyoruz.

## DEVELOPMENT - Flask Web App - Manuel

1.Bilgisayarinizda python, git ve pip araci kurulmus olmali.

2.[pipenv](https://github.com/pypa/pipenv) araci kurmalisiniz. pip paketi ile rahatca kurabilirsiniz.

```bash
$ pip install pipenv
```

3.Reponun klonunu alin. Ve klasorun icine giriniz. Ve pipenv ile bagimliliklari kurunuz.

```bash
$ git clone https://github.com/vanhohen/bi-usis
$ cd bi-usis/app
$ pipenv install
```

4.Virtual environment aktiflestirilmis shell acin ve projeyi calistirin.

```bash
$ pipenv shell
Spawning environment shell (/usr/bin/zsh). Use 'exit' to leave.
source /home/pleycpl/.local/share/virtualenvs/bi-usis-nhPhaM-A/bin/activate
$ source /home/pleycpl/.local/share/virtualenvs/bi-usis-nhPhaM-A/bin/activate
(bi-usis-nhPhaM-A) $
(bi-usis-nhPhaM-A) $ python app.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 111-111-111

```

Mysql indir. Ayarlarini yap.

## DEVELOPMENT - Database Schema

1. [draw.io](https://www.draw.io) sitesini acin.
2. Sonrasinda Sol kisimdan File->OpenFrom->Github diyerek auth olun.
3. Sonrasin reponun icinden database klasorun altindan DatabaseSchemaDiagram.xml tiklayin.
4. Eger bir degislik yaptiysaniz sol ust kisimda "Unsaved changes. Click here to save" butonuna tiklayip commit atin.
