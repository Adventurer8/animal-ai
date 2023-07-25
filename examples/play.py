import sys
import random
import os

from animalai.envs.environment import AnimalAIEnvironment

def load_config_and_play(configuration_file: str) -> None:
    """
    Loads a configuration file for a single arena and lets you play manually
    :param configuration_file: str path to the yaml configuration
    :return: None
    """
    env_path = "../env/AAI_v3.0.1_build_linux_090422.x86_64"
    port = 5005 + random.randint(
        0, 1000
    )  # use a random port to avoid problems if a previous version exits slowly

    print("initializaing AAI environment")
    environment = AnimalAIEnvironment(
        file_name=env_path,
        base_port=port,
        arenas_configurations=configuration_file,
        play=True,
    )

    # Run the environment until signal to it is lost
    try:
        while environment._process:
            continue
    except KeyboardInterrupt:
        pass
    finally:
        environment.close()


# If an argument is provided then assume it is path to a configuration and use that
# Otherwise load a random competition config.
if __name__ == "__main__":
    if len(sys.argv) > 1:
        configuration_file = sys.argv[1]
    else:
        # Introductory experiments - Basic Food Variations
        conf = ['01-01-01', '01-01-02', '01-01-03', '01-02-01', '01-02-02', '01-02-03', '01-03-01', '01-03-02', '1-03-03']
        
        competition_folder = "../configs/competition/"
        configuration_files = os.listdir(competition_folder)
        # configuration_files = conf

        configuration_random = random.randint(0, len(configuration_files)-1)
        configuration_file = competition_folder + configuration_files[configuration_random]
        # configuration_file = competition_folder + configuration_files[configuration_random] + '.yaml'
        print(F"Using configuration file {configuration_file}")
    
    load_config_and_play(configuration_file=configuration_file)