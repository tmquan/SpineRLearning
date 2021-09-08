import os
import gym
import abc
import glob
import numpy as np
from argparse import ArgumentParser

class CustomEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    # reward_range = (0.0, 1.0)
    @abc.abstractmethod
    def __init__(self):
        self.__version__ = "0.0.1"
        print("Init CustomEnv")
        # Modify the observation space, low, high and shape values according to your custom environment's needs
        # self.observation_space = gym.spaces.Box(low=0.0, high=1.0, shape=(3,))
        # Modify the action space, and dimension according to your custom environment's needs
        # self.action_space = gym.spaces.Discrete(4)
        pass

    @abc.abstractmethod
    def step(self, action):
        """
        Runs one time-step of the environment's dynamics. The reset() method is called at the end of every episode
        :param action: The action to be executed in the environment
        :return: (observation, reward, done, info)
            observation (object):
                Observation from the environment at the current time-step
            reward (float):
                Reward from the environment due to the previous action performed
            done (bool):
                a boolean, indicating whether the episode has ended
            info (dict):
                a dictionary containing additional information about the previous action
        """
        # Implement your step method here
        # return (observation, reward, done, info)
        pass

    @abc.abstractmethod
    def reset(self):
        """
        Reset the environment state and returns an initial observation
        Returns
        -------
        observation (object): The initial observation for the new episode after reset
        :return:
        """

        # Implement your reset method here
        # return observation

    @abc.abstractmethod
    def render(self, mode='human', close=False):
        """
        :param mode:
        :return:
        """
        pass


class ImageEnv(CustomEnv):
    def __init__(self, 
        image_dirs: str = "path/to/dir", 
        label_dirs: str = "path/to/dir", 
        shape: int = 256,
        batch_size: int = 32
    ):
        super().__init__()
        self.image_dirs = image_dirs, 
        self.label_dirs = label_dirs, 
        self.batch_size = batch_size
        self.shape = shape
        
        def glob_files(folders: str=None, extension: str='*.nii.gz'):
            assert folders is not None
            paths = [glob.glob(os.path.join(folder, extension)) for folder in folders]
            files = sorted([item for sublist in paths for item in sublist])
            print(len(files))
            print(files[:1])
            return files

        self.image_files = glob_files(folders=image_dirs, extension='*.png')
        self.label_files = glob_files(folders=label_dirs, extension='*.png')    

        self.reset()


    def reset(self):
        pass

    def step(self, act):
        pass
        
    def render(self, mode='rgb_array'):
        pass

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--datadir", type=str, default='drive/MyDrive/Data/ChestXRLungSegmentation/', 
                        help="logging directory")

    hparams = parser.parse_args()
    env = ImageEnv(
        image_dirs=[
            os.path.join(hparams.datadir, 'JSRT/processed/images/'), 
            os.path.join(hparams.datadir, 'ChinaSet/processed/images/'), 
            os.path.join(hparams.datadir, 'Montgomery/processed/images/'),
        ],
        label_dirs=[
            os.path.join(hparams.datadir, 'JSRT/processed/images/'), 
            os.path.join(hparams.datadir, 'ChinaSet/processed/images/'), 
            os.path.join(hparams.datadir, 'Montgomery/processed/images/'),
        ]
    )