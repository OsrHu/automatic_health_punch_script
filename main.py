import yaml
from config import Configuration
import schedule
from job import daka


def main():
    config = Configuration.getConfig()
    schedule.every().day.at(config["schedule"]).do(daka)
    while True:
        schedule.run_pending()


if __name__ == '__main__':
    with open('application.yml', 'r', encoding='utf-8') as f:
        Configuration.createConfig(yaml.load(f.read(), Loader=yaml.Loader))
        main()
