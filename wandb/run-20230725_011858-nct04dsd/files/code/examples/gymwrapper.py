# from stable_baselines3 import PPO
from stable_baselines3 import DQN
import torch as th
import argparse

import sys
import random
import os
import time
# from stable_baselines3.common.vec_env.dummy_vec_env import DummyVecEnv
from gym_unity.envs import UnityToGymWrapper
from animalai.envs.environment import AnimalAIEnvironment


def parse_args():
    # fmt: off
    parser = argparse.ArgumentParser()
    parser.add_argument("--exp-name", type=str, default=os.path.basename(__file__).rstrip(".py"),
        help="the name of this experiment")
    parser.add_argument("--seed", type=int, default=1,
        help="seed of the experiment")
    parser.add_argument("--torch-deterministic", type=lambda x: bool(strtobool(x)), default=True, nargs="?", const=True,
        help="if toggled, `torch.backends.cudnn.deterministic=False`")
    parser.add_argument("--cuda", type=lambda x: bool(strtobool(x)), default=True, nargs="?", const=True,
        help="if toggled, cuda will be enabled by default")
    parser.add_argument("--track", type=lambda x: bool(strtobool(x)), default=True, nargs="?", const=True,
        help="if toggled, this experiment will be tracked with Weights and Biases")
    parser.add_argument("--wandb-project-name", type=str, default="cleanRL",
        help="the wandb's project name")
    parser.add_argument("--wandb-entity", type=str, default=None,
        help="the entity (team) of wandb's project")
    parser.add_argument("--capture-video", type=lambda x: bool(strtobool(x)), default=True, nargs="?", const=True,
        help="whether to capture videos of the agent performances (check out `videos` folder)")
    parser.add_argument("--save-model", type=lambda x: bool(strtobool(x)), default=False, nargs="?", const=True,
        help="whether to save model into the `runs/{run_name}` folder")
    parser.add_argument("--upload-model", type=lambda x: bool(strtobool(x)), default=False, nargs="?", const=True,
        help="whether to upload the saved model to huggingface")
    parser.add_argument("--hf-entity", type=str, default="",
        help="the user or org name of the model repository from the Hugging Face Hub")

    # Algorithm specific arguments
    parser.add_argument("--env-id", type=str, default="CartPole-v1",
        help="the id of the environment")
    parser.add_argument("--total-timesteps", type=int, default=500000,
        help="total timesteps of the experiments")
    parser.add_argument("--learning-rate", type=float, default=2.5e-4,
        help="the learning rate of the optimizer")
    parser.add_argument("--num-envs", type=int, default=1,
        help="the number of parallel game environments")
    parser.add_argument("--buffer-size", type=int, default=10000,
        help="the replay memory buffer size")
    parser.add_argument("--gamma", type=float, default=0.99,
        help="the discount factor gamma")
    parser.add_argument("--tau", type=float, default=1.,
        help="the target network update rate")
    parser.add_argument("--target-network-frequency", type=int, default=500,
        help="the timesteps it takes to update the target network")
    parser.add_argument("--batch-size", type=int, default=128,
        help="the batch size of sample from the reply memory")
    parser.add_argument("--start-e", type=float, default=1,
        help="the starting epsilon for exploration")
    parser.add_argument("--end-e", type=float, default=0.05,
        help="the ending epsilon for exploration")
    parser.add_argument("--exploration-fraction", type=float, default=0.5,
        help="the fraction of `total-timesteps` it takes from start-e to go end-e")
    parser.add_argument("--learning-starts", type=int, default=10000,
        help="timestep to start learning")
    parser.add_argument("--train-frequency", type=int, default=10,
        help="the frequency of training")
    args = parser.parse_args()
    # fmt: on
    assert args.num_envs == 1, "vectorized envs are not supported at the moment"

    return args

def train_agent_single_config(configuration_file):

    args =  parse_args()
    import wandb

    wandb.init(
        project='dqn',
        entity=None,
        sync_tensorboard=True,
        config=vars(args),
        name=f"{int(time.time())}",
        monitor_gym=True,
        save_code=True,
    )

    aai_env = AnimalAIEnvironment(
        seed = 123,
        file_name="/home/roma/animal-ai/env/AAI_v3.0.1_build_linux_090422.x86_64",
        arenas_configurations=configuration_file,
        play=False,
        base_port=5000,
        inference=False,
        useCamera=True,
        resolution=36,
        useRayCasts=False,
        # raysPerSide=1,
        # rayMaxDegrees = 30,
    )

    # env = UnityToGymWrapper(aai_env, uint8_visual=False, allow_multiple_obs=True, flatten_branched=False)
    # def make_env():
    #     def _thunk():
    #         env = UnityToGymWrapper(aai_env, uint8_visual=False, allow_multiple_obs=True, flatten_branched=True)
    #         return env
    #     return _thunk
    # env = DummyVecEnv([make_env()])
    env = UnityToGymWrapper(aai_env, uint8_visual=True, allow_multiple_obs=False, flatten_branched=True)
    runname = "inserrunname"

    policy_kwargs = dict(activation_fn=th.nn.ReLU)
    model = DQN("CnnPolicy", env, policy_kwargs=policy_kwargs, verbose=1, tensorboard_log=("./dqn_tensorboard/" + runname))

    no_saves = 100
    no_steps = 1000000
    reset_num_timesteps = True
    for i in range(no_saves):
        model.learn(no_steps, reset_num_timesteps=reset_num_timesteps)
        model.save("results/" + runname + "/model_" + str( (i+1)*no_steps ))
        reset_num_timesteps = False
    env.close()
    
# Loads a random competition configuration unless a link to a config is given as an argument.
if __name__ == "__main__":
    if len(sys.argv) > 1:
        configuration_file = sys.argv[1]
    else:   
        competition_folder = "/home/roma/animal-ai/configs/competition/"
        configuration_files = os.listdir(competition_folder)
        configuration_random = random.randint(0, len(configuration_files))
        configuration_file = (
            competition_folder + configuration_files[configuration_random]
        )
    train_agent_single_config(configuration_file=configuration_file)
