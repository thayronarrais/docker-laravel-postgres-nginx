import os
import yaml


def test_services_exist():
    compose_file = os.path.join(os.path.dirname(__file__), os.pardir, "docker-compose.yml")
    with open(compose_file, 'r') as f:
        compose = yaml.safe_load(f)
    services = compose.get('services', {})
    for svc in ['redis', 'postgres', 'webserver', 'php-fpm']:
        assert svc in services
