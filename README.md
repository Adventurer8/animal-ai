# AnimalAI 3

AAI supports interdisciplinary research to help better understand human, animal, and artificial cognition. It aims to support AI research towards unlocking cognitive capabilities and better understanding the space of possible minds.

| ![](docs/figs/animal-cyl-fail.gif) | ![](docs/figs/agent-cyl-fail.gif) |
|---|---|
| ![](docs/figs/animal-cyl-pass.gif) | ![](docs/figs/agent-cyl-pass.gif) |

## This Repo

This repo contains some introductory python scripts for interacting with the training environment as well as the [900 tasks](competition_configurations) which were used in the original Animal-AI Olympics competition and some others for demonstration purposes. Details of the tasks can be found on the [AAI website](http://animalaiolympics.com/AAI/testbed) where they can also be played and competition entries watched.

The environment is built using [Unity ml-agents](https://github.com/Unity-Technologies/ml-agents/tree/master/docs) release 2 (python package 0.26.0).

## Getting Started

To get started with the environment follow the download instructions below and then one of the following tutorials.

- [Designing Experiments](@TODO)
- [Training using Stable Baselines 3](@TODO)
- [Running psychology experiments](@TODO)
- [Watching your agent](@TODO)
- @TODO

After cloning this repo **download the environment** for your system:

| OS | Environment link |
| --- | --- |
| Linux |  [v3.0](@TODO) |
| Mac | [v3.0](@TODO) |
| Windows | [v3.0](@TODO) |

Unzip the **entire content** of the archive to the `env` folder. On linux you may have to make the file executable by running `chmod +x env/AnimalAI.x86_64`. Note that the env folder should contain the AnimalAI.exe/.x86_84/.app depending on your system and *any other folders* in the same directory in the zip file.

You will need the python package mlagents==0.26.0, protobuf==3.17.0, and, depending on usage, gym-unity==0.26.0. (Proper installation instructions will be provided for v3.0 release by Nov 12th.).0--p

The Animal-AI environment and packages are currently only tested on linux (Ubuntu 20.04.2 LTS) with python 3.8 but should also work on python 3.6+, other linux distros and Windows and Mac.

**The Unity Project** for the environment is available [here](@TODO), please check the github for contributions. 

## Manual Control

If you launch the environment directly from the executable or through the `play_config.py` script it will launch
 in player mode. Here you can control the agent with the following:

| Keyboard Key  | Action    |
| --- | --- |
| W   | move agent forwards |
| S   | move agent backwards|
| A   | turn agent left     |
| D   | turn agent right    |
| C   | switch camera       |
| R   | reset environment   |

## Citing
If you use the Animal-AI environment in your work you can cite the environment paper:

 Crosby, M., Beyret, B., Shanahan, M., Hernández-Orallo, J., Cheke, L. & Halina, M.. (2020). The Animal-AI Testbed and Competition. Proceedings of the NeurIPS 2019 Competition and Demonstration Track, in Proceedings of Machine Learning Research 123:164-176 Available [here](http://proceedings.mlr.press/v123/crosby20a.html).
```
 @InProceedings{pmlr-v123-crosby20a, 
    title = {The Animal-AI Testbed and Competition}, 
    author = {Crosby, Matthew and Beyret, Benjamin and Shanahan, Murray and Hern\'{a}ndez-Orallo, Jos\'{e} and Cheke, Lucy and Halina, Marta}, 
    booktitle = {Proceedings of the NeurIPS 2019 Competition and Demonstration Track}, 
    pages = {164--176}, 
    year = {2020}, 
    editor = {Hugo Jair Escalante and Raia Hadsell}, 
    volume = {123}, 
    series = {Proceedings of Machine Learning Research}, 
    month = {08--14 Dec}, 
    publisher = {PMLR}, 
} 
```

## Unity ML-Agents

The Animal-AI Olympics was built using [Unity's ML-Agents Toolkit.](https://github.com/Unity-Technologies/ml-agents)

Juliani, A., Berges, V., Vckay, E., Gao, Y., Henry, H., Mattar, M., Lange, D. (2018). [Unity: A General Platform for 
Intelligent Agents.](https://arxiv.org/abs/1809.02627) *arXiv preprint arXiv:1809.02627*

Further the documentation for [mlagents](https://github.com/Unity-Technologies/ml-agents) should be consulted if you want to make any changes.

## Version History

- v2.2.3
  - Now you can specify multiple different arenas in a single yml config file ant the environment will cycle through them each time it resets
- v2.2.2 
  - Low quality version with improved fps. (will work on further improvments to graphics & fps later)
- v2.2.1
  - Improve UI scaling wrt. screen size
  - Fixed an issue with cardbox objects spawning at the wrong sizes
  - Fixed an issue where the environment would time out after the time period even when health > 0 (no longer intended behaviour)
  - Improved Death Zone shader for weird Zone sizes
- v2.2.0 Health and Basic Scripts
  - Switched to health-based system (rewards remain the same).
  - Updated overlay in play mode.
  - Allow 3D hot zones and death zones and make them 3D by default in old configs.
  - Added rewards that grow/decay (currently not configurable but will be added in next update).
  - Added basic Gym Wrapper.
  - Added basic heuristic agent for benchmarking and testing.
  - Improved all other python scripts.
  - Fixed a reset environment bug when resetting during training.
  - Added the ability to set the DecisionPeriod (frameskip) when instantiating and environment.
- v2.1.1 bugfix
  - Fixed raycast length being less then diagonal length of standard arena
- v2.1 beta release
  - Upgraded to ML-Agents release 2 (0.26.0)
  - New features
    - Added raycast observations
    - Added agent global position to observations
