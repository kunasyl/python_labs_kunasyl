from services import Services


def init():
    
    services = Services()
    resources = services.get_resources()
    
    for resource in resources:
        services.parse_data_and_insert(resource=resource, max_page_number=10)


if __name__ == "__main__":
    init()