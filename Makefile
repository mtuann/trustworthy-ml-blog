build:
	pelican content -s publishconf.py

serve:
	pelican --listen --reload

deploy:
	ghp-import output -b main -p # Or adapt to your chosen deployment method