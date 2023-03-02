from services import Services


def init():
    
    services = Services()
    resources = services.get_resources()
    
    for resource in resources:
        resource_articles = services.parser(resource)
        # print(resource_articles)
        services.insert_data_to_table(resource_articles)


if __name__ == "__main__":
    init()