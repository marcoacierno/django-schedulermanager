projecttest:
	rm -rf test-project/django_schedulermanager
	cp -r django_schedulermanager test-project/django_schedulermanager

release: activate-virtualenv
	python setup.py sdist upload -r pypi

test-release: activate-virtualenv
	python setup.py register -r testpypi

register: activate-virtualenv
	python setup.py register -r pypi

activate-virtualenv:
	source ~/.virtualenvs/django-schedulermanager/bin/activate
