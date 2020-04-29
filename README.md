
# Computational Neuroscience Project

This repository is a final project for UVA cource PSYC5270 Computation Neuroscience

## Motivation
During daily life, we make many reaching movements. The first reaching movements, which emerge around 3 to 4 months of age, and can be characterized by variation and irregular, zig-zag–like trajectories. During the following months, the reaching movements rapidly become more regular and smooth. Thereafter, the fine-tuning of reaching takes many years. The motor cortex is the region of the cerebral cortex, and this said region & its neurons are responsible for the planning, control, and execution of voluntary movements. From an anatomical standpoint, the motor cortex is an area of the frontal lobe located in the posterior precentral gyrus immediately anterior to the central sulcus. As movements are fine-tuned, reaching movements in healthy adults can be characterized (in a superficial statistical sense) by a bell-shaped velocity profile that consists of an acceleration and a deceleration. It takes a long time before reaching movements have this adult configuration. As time goes on, the reaching movements become faster, straighter, and smoother. The increase in smoothness of the reaching movements is due to a decrease of the corrections of the movement path. These corrections can be seen as sub-movements of the reaching movement and are determined with the help of peaks in the velocity profile of the reaching hand. In our data-set (pmd-1), using monkeys as subjects, we looked directly at behavioral variables such as acceleration, velocity and position to understand the essential question of: what does it take for us to move, and what variables can be isolated to increase the smoothness of reaching movements? 

## Goal
The primary research goal is to identify the difference between premotor cortex and primary motor cortex when an animal performs repetitive behavior. Currently, the dataset contains information about the velocity, acceleration, position of the monkey's hand for all the trials. It also provides the number of spikes in each time bin during the reaching task. We would like to find the first onset of different neurons and determine if this onset time has changed between different trials. The difference between premotor cortex and primary motor cortex will be interesting, but it would also be exciting to locate changes in trends of different neurons of the same cortex.


## Methodology
### Linear-Nonlinear-Poisson Cascade Model
- Firstly, we found the first onset of different neurons and determined if this onset time has changed between different trials. 
- We take average of all neurons in PMd and M1 data.
- Then, we did a poisson regression for our model. 
- Finally, we generated graphs of the relationship between coefficients of M1 and PMd. 

### Smoothness of Trajectory
We wonder if the kinematic data over reaches will indicate that Monkey MT have learnt from previous experience. In the project, we use smoothness of trajectory (both position and velocity) as an indicator of proficiency.

## Usage

The main results are contained in the Jupyter Notebook in the root directory called "data exploration.ipynb". All you need to do is to put the dataset into the folder "data" and run the notebook. The retrieval of data and all the process are contained in the notebook.

Datasets should be put into the folder "data" from https://crcns.org/data-sets/motor-cortex/pmd-1 by the user.

*read_data(file_name)* is a static method in *src/io.py*. 
The parameter *file_name* should be a string that incicates the data file name, which should be one of the following:
  * MM_S1_raw.mat
  * MM_S1_processed.mat
  * MT_S1_raw.mat
  * MT_S1_processed.mat
  * MT_S2_raw.mat
  * MT_S2_processed.mat
  * MT_S3_raw.mat
  * MT_S3_processed.mat

You can test it by uncommenting the last few lines in *io.py*. No outputs for this function, but data is read and passed as return value.


