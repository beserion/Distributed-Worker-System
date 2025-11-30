.PHONY: build-plugin up clean

build-plugin:
	cd plugins/c_plugin && $(MAKE)

up:
	docker-compose up --build

clean:
	cd plugins/c_plugin && $(MAKE) clean
