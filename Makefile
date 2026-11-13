.PHONY: build pdf site check preview clean

build:
	.venv/bin/python scripts/build.py

pdf:
	.venv/bin/python scripts/build.py --pdf

site:
	.venv/bin/python scripts/build.py --website

check:
	.venv/bin/python scripts/check_pdf.py output/cv-natalie-rebecchi.pdf

preview:
	.venv/bin/python scripts/preview.py output/cv-natalie-rebecchi.pdf
	.venv/bin/python scripts/screenshot_site.py

clean:
	rm -rf output
