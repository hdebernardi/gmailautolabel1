# install required modules
all:
	pip install -r requirements.txt

# clean all including virtual environment
clean_all:
	rm -rf env build dist mailautolabel.egg-info

# clean directories generated by setup.py
clean:
	rm -rf build dist mailautolabel.egg-info
