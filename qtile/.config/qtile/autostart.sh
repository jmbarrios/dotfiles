#!/bin/sh 
# Screen configuration
# Working with a second monitor via DP
# xrandr --output DP-0 --off \
#   --output DP-4 --primary --mode 1920x1080 --pos 1920x0 --rotate normal \
#   --output DP-1 --off \
#   --output DP-2 --off \
#   --output DP-3 --off \
#   --output HDMI-0 --off \
#   --output DVI-I-1-1 --mode 1920x1080 --pos 0x0 --rotate normal
# Working with second monitor via DVI w/DisplayLink
# xrandr --output DP-0 --off \
#   --output DP-1 --off \
#   --output DP-2 --off \
#   --output DP-3 --off \
#   --output HDMI-0 --mode 1920x1080 --pos 0x0 --rotate normal \
#   --output DP-4 --primary --mode 1920x1080 --pos 1920x0 --rotate normal
# Working with second monitor connected via HDMI
# xrandr --output DP-0 --off \
#     --output DP-1 --off \
#     --output DP-2 --off \
#     --output DP-3 --off \
#     --output HDMI-0 --mode 1920x1080 --pos 0x0 --rotate normal \
#     --output DP-4 --primary --mode 1920x1080 --pos 1920x0 --rotate normal

# Composite
# /usr/bin/picom -b

# Map esc key to caps lock
/usr/bin/setxkbmap -option "caps:swapescape"
