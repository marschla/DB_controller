#!/bin/bash

source /environment.sh

# initialize launch file
dt-launchfile-init

# YOUR CODE BELOW THIS LINE
# ----------------------------------------------------------------------------


# NOTE: Use the variable DT_REPO_PATH to know the absolute path to your code
# NOTE: Use `dt-exec COMMAND` to run the main process (blocking process)

# launching app
dt-exec roslaunch my_package nodeGotoAngle.launch
#dt-exec roslaunch my_package nodePurePursuit.launch
#dt-exec roslaunch my_package nodePID.launch
#dt-exec roslaunch my_package nodeCascadePID.launch
#dt-exec roslaunch my_package noderealPID.launch

# ----------------------------------------------------------------------------
# YOUR CODE ABOVE THIS LINE

# wait for app to end
dt-launchfile-join
