menu:
	@echo "1. A ski"
	@echo "2. Cryptarithme"
	@read -p "Quel énigme souhaitez-vous sélectionner ? " choix; \
	docker run -it -v $(shell pwd):/app python python src/enigme$$choix.py
