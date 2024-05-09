from antipattern_descriptions import compose_error_descriptions

def check_shared_volume_antipattern(node, matches):
    if isinstance(node, dict) and 'services' in node:
        volumes = {}
        for service, config in node['services'].items():
            if 'volumes' in config:
                for volume in config['volumes']:
                    if volume in volumes:
                        matches.append([f"Antipattern found in services: {volumes[volume]} and {service}. {compose_error_descriptions[4]}",10])
                    volumes[volume] = service
