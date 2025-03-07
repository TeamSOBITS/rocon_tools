#!/usr/bin/env python3
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_concert/license/LICENSE
#
##############################################################################
# Imports
##############################################################################

import rospy
import rocon_interactions

##############################################################################
# Main
##############################################################################

if __name__ == '__main__':

    rospy.init_node('rocon_interactions', log_level=rospy.INFO)
    interactions_manager = rocon_interactions.InteractionsManager()
    interactions_manager.spin()
