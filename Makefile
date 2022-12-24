requirements:
	pip3 install -r requirements.txt
	pip3 install -U -r requirements.txt

build:
	pyinstaller main.py
	cp -r ./lang ./dist/main/lang
	tar -zcvf dist.tgz ./dist/main