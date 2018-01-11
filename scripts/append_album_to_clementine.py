#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 21:25:42 2018

@author: mdlkxzmcp
@version: 0.1.0
"""

import sys, getopt, os, re, dbus


def displayHelpMessage():
    print("""
          Usage: append_album_to_clementine.py [options]
          Assumes: Clementine is running.
          Options:
              -h, --help        show this help message and exit.
              -p, --play        [default: False] Used to play the first track
                                from the appended list.
              -i PATH, --input=PATH
                                [default: cwd] Supply a path to the album(s)
                                you would wish to append to the current 
                                Clementine playlist.""")


def createTrackList(folder_path):
    track_list = []

    for subdir, _dirs, files in os.walk(folder_path):
        for file in files:
            file_path = subdir + os.sep + file
            if re.search("\.(mp3|ogg|flac|aac)$", file_path): # HACK
                track_list.append(file_path)

    return track_list


def appendAlbum(folder_path, play_now=False):
def appendAlbum(folder_path=os.getcwd(), play_now=False):
    track_list = createTrackList(folder_path)
    interface = createInterface()
    last_track_in_playlist_id = interface.GetLength()
    track_number = 0  # TODO: use AfterTrack value from the TrackAdded signal instead
    for track in track_list:
        if track_list[0] == track:
            interface.AddTrack(track, last_track_in_playlist_id, play_now)
            # TODO: wait for a TrackAdded signal
        else:
            interface.AddTrack(track, last_track_in_playlist_id + track_number, False)
            # TODO: wait for a TrackAdded signal again :>
        track_number += 1


def createInterface():
    session_bus = dbus.SessionBus()
    track_list = session_bus.get_object('org.mpris.MediaPlayer2.clementine', '/Tracklist')
    return dbus.Interface(track_list, dbus_interface='org.freedesktop.MediaPlayer')


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hpi:", ["help", "play_now", "input="])
    except getopt.GetoptError as err:
        print(err)
        displayHelpMessage()
        sys.exit(2)
    
    play_now = False

    for opt, arg in opts:
        if opt in ('-h', "--help"):
            displayHelpMessage()
            sys.exit()
        elif opt in ('-p', '--play_now'):
            play_now = True
        elif opt in ('-i', '--input'):
            appendAlbum(arg, play_now)
        else:
            appendAlbum()


if __name__ == "__main__":
    main()
