import logging
import numpy as np
from mlagents.envs import UnityEnvironment

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SimCity")

class SimCityEnv(object):

    def __init__(self, env_file_name):

        self._env = UnityEnvironment(env_file_name)
        self._brain_name = self._env.external_brain_names[0]
        brain = self._env.brains[self._brain_name]

        self._num_visual_observations = brain.number_visual_observations
        self._visual_observation_space = []
        for i in range(self._num_visual_observations):
            height = brain.camera_resolutions[i]['height']
            width = brain.camera_resolutions[i]['width']
            self._visual_observation_space.append(((height, width, 3)))
        self._vector_observation_space = (brain.vector_observation_space_size,)

        self._action_space = (brain.vector_action_space_size[0],)

        self._seed = None

    def reset(self):

        if self._seed is None:
            rseed = np.random.randint(1e6)
        else:
            rseed = self._seed
        assert isinstance(rseed, int), "random seed must be a integer"
        reset_params = dict(Seed = rseed)
        self._env.reset(config = reset_params)[self._brain_name]
        ob, reward, done, info = self.step(np.zeros(self._action_space))
        return ob, reward, done, info

    def step(self, action):

        assert isinstance(action, np.ndarray), "action must be a numpy.ndarry"
        assert action.shape == self._action_space, "action.shape doesn't match env.action_space"

        infos = self._env.step(action)[self._brain_name]
        ob, reward, done, info = self.extract_infos(infos)

        return ob, reward, done, info

    def extract_infos(self, infos):

        ob = []
        for i in range(self._num_visual_observations):
            ob.append(infos.visual_observations[i].squeeze())
        ob.append(infos.vector_observations[0][0])
        reward = infos.rewards[0]
        done = infos.local_done[0]
        info = {}

        return ob, reward, done, info

    def seed(self, seed=None):

        assert isinstance(seed, int), "random seed must be a integer"
        self._seed = seed
        logger.warn("New seed %d will be used after next reset." % self._seed)

    def close(self):
        self._env.close()

    def sample_action(self):
        return np.random.uniform(size=self._action_space)

    @property
    def num_visual_observations(self):
        return self._num_visual_observations

    @property
    def observation_space(self):
        return self._visual_observation_space + [self._vector_observation_space]

    @property
    def action_space(self):
        return self._action_space
